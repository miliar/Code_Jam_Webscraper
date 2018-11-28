#include <cstdlib>
#include <iostream>
#include <string>
#include <map>


using namespace std;

enum Action  { Action_Depart, Action_Arrive };
enum Station { Station_A, Station_B };

typedef struct
{
    Action action;
    Station station;
} TripInfo;

//typedef int Timestamp;
typedef float Timestamp;
typedef multimap<Timestamp, TripInfo *> TripInfoTable;

TripInfoTable g_TripInfoTable;


// Time format is HH:MM
Timestamp ConvertTime(const string &time)
{
    return ((time[0] - '0') * 10 + (time[1] - '0')) * 60 +
           ((time[3] - '0') * 10 + (time[4] - '0'));
}

void InsertTripInfoTable(Timestamp timestamp, Action action, Station station)
{
    TripInfo *tripInfo = new TripInfo;
    tripInfo->action = action;
    tripInfo->station = station;

	if (action == Action_Depart)
	{
		// Cheat!
		timestamp += 0.1;
	}

    g_TripInfoTable.insert(TripInfoTable::value_type(timestamp, tripInfo));
}

void ClearTripInfoTable()
{
    for (TripInfoTable::const_iterator iter = g_TripInfoTable.begin();
         iter != g_TripInfoTable.end();
         iter++)
    {
        delete iter->second;
    }

    g_TripInfoTable.clear();
}

void DumpTripInfoTable()
{
	cout << endl;

    for (TripInfoTable::const_iterator iter = g_TripInfoTable.begin();
         iter != g_TripInfoTable.end();
         iter++)
    {
        cout << iter->first
             << ": ("
             << ((iter->second->action == Action_Depart) ? "Depart" : "Arrive")
             << ", "
             << ((iter->second->station == Station_A) ? "A" : "B")
             << ")"
             << endl;
    }
}

void ReadInput()
{
    Timestamp turnaroundTime;
    cin >> turnaroundTime;

    int NA;
    int NB;
    cin >> NA >> NB;

    for (int i=0; i<NA; i++)
    {
        string departure, arrival;
        cin >> departure >> arrival;

        InsertTripInfoTable(ConvertTime(departure), Action_Depart, Station_A);
        InsertTripInfoTable(ConvertTime(arrival) + turnaroundTime,
                            Action_Arrive,
                            Station_B);
    }

    for (int i=0; i<NB; i++)
    {
        string departure, arrival;
        cin >> departure >> arrival;

        InsertTripInfoTable(ConvertTime(departure), Action_Depart, Station_B);
        InsertTripInfoTable(ConvertTime(arrival) + turnaroundTime,
                            Action_Arrive,
                            Station_A);
    }

    //DumpTripInfoTable();
}

void Run()
{
    ReadInput();

    int NumTrainsAtA = 0;
    int NumTrainsAtB = 0;
    int NumTrainsShouldStartAtA = 0;
    int NumTrainsShouldStartAtB = 0;

    for (TripInfoTable::const_iterator iter = g_TripInfoTable.begin();
         iter != g_TripInfoTable.end();
         iter++)
    {
        Action action = iter->second->action;
        Station station = iter->second->station;

        if (action == Action_Depart)
        {
            if (station == Station_A)
            {
                if (NumTrainsAtA > 0)
                {
                    NumTrainsAtA--;
                }
                else
                {
                    NumTrainsShouldStartAtA++;
                }
            }
            else // Station_B
            {
                if (NumTrainsAtB > 0)
                {
                    NumTrainsAtB--;
                }
                else
                {
                    NumTrainsShouldStartAtB++;
                }
            }
        }
        else // Action_Arrive
        {
            if (station == Station_A)
            {
                NumTrainsAtA++;
            }
            else // Station_B
            {
                NumTrainsAtB++;
            }
        }
    }

    cout << NumTrainsShouldStartAtA << " " << NumTrainsShouldStartAtB << endl;

    // Table cleanup
    ClearTripInfoTable();
}

int main(int argc, char *argv[])
{
    int N;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        Run();
    }

    return 0;
}
