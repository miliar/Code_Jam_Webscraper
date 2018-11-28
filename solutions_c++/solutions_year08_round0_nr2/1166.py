#include <iostream>
#include <string.h>
#include <fstream>
#include <map>


using namespace std;


int i_Turnaround = 0;
int i_TripsAtoB = 0;
int i_TripsBtoA = 0;

map<int, int>	map_DepartureA;
map<int, int>	map_ReadyA;
map<int, int>	map_DepartureB;
map<int, int>	map_ReadyB;

int	i_TrainsA = 0;
int i_TrainsB = 0;

void Reset()
{
	i_Turnaround = 0;
	i_TripsAtoB = 0;
	i_TripsBtoA = 0;
	i_TrainsA = 0;
	i_TrainsB = 0;

	map_DepartureA.clear();
	map_ReadyA.clear();

	map_DepartureB.clear();
	map_ReadyB.clear();
}


// parameter format = HH:MM (24 h)
int ConvertToMinute(char *zTime)	
{
	//cout << "Convert to Min = " << zTime << endl;
	
	char *zTemp = strtok(zTime, ":");
	int iMin = atoi(zTemp) * 60;
	zTemp = strtok(NULL, " ");
	iMin += atoi(zTemp);

	return iMin;
}


int main (int argc, char **argv)
{
	if (argc != 3)
	{
		cerr << "usage: " << argv[0] << " <input file> <output file>" << endl;
		exit(-1);
	}

	ifstream input;
	input.open(argv[1]);
	ofstream output;
	output.open(argv[2]);

	int iCases;
	char zLine[20];
	input.getline(zLine, 20);
	iCases = atoi(zLine);

	int iTempTime = 0;
	char *zTemp = NULL;
	char *zTemp2 = NULL;

	for (int iCase = 1; iCase <= iCases; iCase++)
	{
		Reset();


		cout << "Test case = " << iCase << endl;
		
		input.getline(zLine, 20);
		i_Turnaround = atoi(zLine);
		cout << "Turnaround = " << i_Turnaround << endl;

		// get number of trips
		input.getline(zLine, 20);
		zTemp = strtok(zLine, " ");
		i_TripsAtoB = atoi(zTemp);
		zTemp = strtok(NULL, " ");
		i_TripsBtoA = atoi(zTemp);
		cout << "NA = " << i_TripsAtoB << ", NB = " << i_TripsBtoA << endl;

		// load trips from A to B (NA)
		for (int iNA = 0; iNA < i_TripsAtoB; iNA++)
		{
			input.getline(zLine, 20);
			zTemp = strtok(zLine, " ");
			zTemp2 = strtok(NULL, " ");

			iTempTime = ConvertToMinute(zTemp);
			map_DepartureA.insert(pair<int,int>((iTempTime * 1000) + iNA, iTempTime));
			
			iTempTime = ConvertToMinute(zTemp2);
			map_ReadyB.insert(pair<int, int>(((iTempTime + i_Turnaround) * 1000) + iNA, iTempTime + i_Turnaround));
		}		
	
		// load trips from B to A (NB)
		for (int iNB = 0; iNB < i_TripsBtoA; iNB++)
		{
			input.getline(zLine, 20);
			zTemp = strtok(zLine, " ");
			zTemp2 = strtok(NULL, " ");

			iTempTime = ConvertToMinute(zTemp);
			map_DepartureB.insert(pair<int,int>((iTempTime * 1000) + iNB, iTempTime));

			iTempTime = ConvertToMinute(zTemp2);
			map_ReadyA.insert(pair<int, int>(((iTempTime + i_Turnaround) * 1000) + iNB, iTempTime + i_Turnaround));
		}		


		// trains from A
		map<int,int>::iterator itr = map_DepartureA.begin();
		map<int,int>::iterator itrEnd = map_DepartureA.end();
		map<int,int>::iterator itrReady;
		while (itr != itrEnd)
		{

			itrReady = map_ReadyA.begin();
			if ((itrReady != map_ReadyA.end()) &&
				(itr->second >= itrReady->second))
			{
				cout << "Return Trip from A: Depart = " << itr->second << ", Ready = " << itrReady->second << endl;
				map_ReadyA.erase(itrReady);				
			}
			else
			{
				i_TrainsA++;
				cout << "New Trip from A: Depart = " << itr->second << endl;
			}

			++itr;
		}


		// trains from B
		itr = map_DepartureB.begin();
		itrEnd = map_DepartureB.end();
		while (itr != itrEnd)
		{

			itrReady = map_ReadyB.begin();
			if ((itrReady != map_ReadyB.end()) &&
				(itr->second >= itrReady->second))
			{
				cout << "Return Trip from B: Depart = " << itr->second << ", Ready = " << itrReady->second << endl;
				map_ReadyB.erase(itrReady);
			}
			else
			{
				i_TrainsB++;
				cout << "New Trip from B: Depart = " << itr->second << endl;
			}

			++itr;
		}


		output << "Case #" << iCase << ": " << i_TrainsA << " " << i_TrainsB << endl;

	}


	input.close();
	output.close();

	exit(0);
}
