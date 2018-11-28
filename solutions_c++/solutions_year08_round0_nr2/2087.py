#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream infile("input.txt");
ofstream outfile("output.txt");

inline int timeToMinutes(string time)
{
	// time = "11:22";

	return atoi( time.substr(0,2).c_str() ) * 60 + atoi( time.substr(3,2).c_str() );
}

inline int timeNeededInMinutes(string timeDeparture, string timeArrival, int turnaround)
{
	return timeToMinutes(timeArrival) - timeToMinutes(timeDeparture) + turnaround;
}

inline int timeReady(string timeArrival, int turnaround)
{
	return timeToMinutes(timeArrival) + turnaround;
}

struct Trajet
{
	short int type;	// 1 for A->B, 2 for B->A
	int departure;	// in min
	int ready;		// in min (counting turnaround)
};

class TrainQueue
{
private:
	int size;
	int train[200];

public:
	TrainQueue();
	void insert(int);
	bool check(int);
	bool remove(int);
};

TrainQueue::TrainQueue()
{
	size = 0;
}

bool TrainQueue::check(int min)
{
	for (int i=0; i<size; i++)
	{
		if ( train[i] <= min )
			return true;
	}

	return false;
}

bool TrainQueue::remove(int min)
{
	for (int i=0; i<size; i++)
	{
		if ( train[i] <= min )
		{
			train[i] = train[size-1];
			size--;

			return true;
		}
	}

	return false;
}
	
void TrainQueue::insert(int min)
{
	if (size < 199)
	{
		size++;
		train[size-1] = min;
	}
	else
	{
		cout << "Train size exceeded 200!" << endl;
	}
}

class Timetable
{
private:
	int numTrajets;
	Trajet * ptr;
	int numTrainsA;
	int numTrainsB;
	int turnaround;
	int NA;
	int NB;
	TrainQueue trainQueueA;
	TrainQueue trainQueueB;
	int ID;

public:
	Timetable(int);
	void sort();
	void calculate();
	void output();
};

Timetable::Timetable(int myID)
{
	ID = myID;

	string tempDeparture, tempArrival;

	infile >> turnaround >> NA >> NB;
	
	numTrajets = NA + NB;

	ptr = new Trajet [numTrajets];

	for (int i=0; i<NA; i++)
	{
		infile >> tempDeparture >> tempArrival;
		
		ptr[i].departure = timeToMinutes(tempDeparture);
		ptr[i].ready = timeReady(tempArrival, turnaround);
		ptr[i].type = 1;
	}

	for (int i=NA; i<numTrajets; i++)
	{
		infile >> tempDeparture >> tempArrival;

		ptr[i].departure = timeToMinutes(tempDeparture);
		ptr[i].ready = timeReady(tempArrival, turnaround);
		ptr[i].type = 2;
	}

	numTrainsA = 0;
	numTrainsB = 0;

	sort();
	calculate();
	output();
}

void Timetable::sort()
{
	int i, j;
	bool flag = true;
	Trajet temp;
	
	for (i = 1; (i <= numTrajets) && flag; i++)
	{
		flag = false;
		
		for (j=0; j < numTrajets - 1; j++)
		{
			if ( ptr[j+1].departure < ptr[j].departure )
			{
				temp = ptr[j];
				ptr[j] = ptr[j+1];
				ptr[j+1] = temp;
				flag = true;
			}
		}
	}
}

void Timetable::calculate()
{
	for (int i=0; i<numTrajets; i++)
	{
		if ( ptr[i].type == 1 )
		{
			if ( ! trainQueueA.remove(ptr[i].departure) )
				numTrainsA++;

			trainQueueB.insert( ptr[i].ready );
		}
		else
		{
			if ( ! trainQueueB.remove(ptr[i].departure) )
				numTrainsB++;

			trainQueueA.insert( ptr[i].ready );
		}
	}
}

void Timetable::output()
{
	outfile << "Case #" << ID << ": " << numTrainsA << " " << numTrainsB << endl;
}

int main()
{
	int N;

	infile >> N;

	for (int i=1; i<=N; i++)
		Timetable a(i);

	infile.close();
	outfile.close();

	return 0;
}