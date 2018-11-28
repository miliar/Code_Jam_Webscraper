#include <fstream>
#include <stdlib.h>
using namespace std;


typedef struct timePair
{
	int departure, arrival;
}timePair;

int compareTimePairDeparture(const void* a1, const void* b1)
{
	timePair *a, *b;
	a = (timePair*)a1;
	b = (timePair*)b1;

	if(a->departure < b->departure)
		return -1;
	else if(a->departure == b->departure)
	{
		if(a->arrival < b->arrival)
			return -1;
		else if(a->arrival == b->arrival)
			return 0;
		else
			return 1;
	}
	else
		return 1;
}

int compareTimePairArrival(const void* a1, const void* b1)
{
	timePair *a, *b;
	a = (timePair*)a1;
	b = (timePair*)b1;

	if(a->arrival < b->arrival)
		return -1;
	else if(a->arrival == b->arrival)
	{
		if(a->departure < b->departure)
			return -1;
		else if(a->departure == b->departure)
			return 0;
		else
			return 1;
	}
	else
		return 1;
}

void main(int argc, char* argv[])
{
	ifstream fin;
	ofstream fout;
	int N;	//#test cases

	fin.open(argv[1], ios::in);
	fout.open(argv[2], ios::out);

	fin>>N;

	for(int index=1;index<=N;index++)
	{
		int turnAroundTime, NA, NB;
		char tempTime[6];
		int tempHours, tempMinutes;
		timePair *stationA, *stationB;

		//parse input

		fin>>turnAroundTime;
		fin>>NA;
		fin>>NB;

		stationA = new timePair[NA];
		stationB = new timePair[NB];

		for(int i=0;i<NA;i++)
		{
			fin>>tempTime;
			tempHours = 10*(tempTime[0]-'0') + (tempTime[1] - '0');
			tempMinutes = 10*(tempTime[3]-'0') + (tempTime[4] - '0');
			stationA[i].departure = tempHours*60 + tempMinutes;
			
			fin>>tempTime;
			tempHours = 10*(tempTime[0]-'0') + (tempTime[1] - '0');
			tempMinutes = 10*(tempTime[3]-'0') + (tempTime[4] - '0');
			stationA[i].arrival = tempHours*60 + tempMinutes;
		}

		for(int i=0;i<NB;i++)
		{
			fin>>tempTime;
			tempHours = 10*(tempTime[0]-'0') + (tempTime[1] - '0');
			tempMinutes = 10*(tempTime[3]-'0') + (tempTime[4] - '0');
			stationB[i].departure = tempHours*60 + tempMinutes;
			
			fin>>tempTime;
			tempHours = 10*(tempTime[0]-'0') + (tempTime[1] - '0');
			tempMinutes = 10*(tempTime[3]-'0') + (tempTime[4] - '0');
			stationB[i].arrival = tempHours*60 + tempMinutes;
		}

		
		
		//process trains arriving at B
		qsort((void*)stationA, NA, sizeof(timePair), &compareTimePairArrival);
		qsort((void*)stationB, NB, sizeof(timePair), &compareTimePairDeparture);

		int trainsCountB = NB;
		
		int indexA = 0;
		int indexB = 0;
		while( indexA<NA && indexB<NB )
		{
			if( (stationA[indexA].arrival + turnAroundTime) <= stationB[indexB].departure )
			{
				trainsCountB--;
				indexA++;
				indexB++;
			}
			else
			{
				indexB++;
			}

		}


		//process trains arriving at A
		qsort((void*)stationB, NB, sizeof(timePair), &compareTimePairArrival);
		qsort((void*)stationA, NA, sizeof(timePair), &compareTimePairDeparture);

		int trainsCountA = NA;

		indexA = 0;
		indexB = 0;
		while( indexA<NA && indexB<NB )
		{
			if( (stationB[indexB].arrival + turnAroundTime) <= stationA[indexA].departure )
			{
				trainsCountA--;
				indexA++;
				indexB++;
			}
			else
			{
				indexA++;
			}

		}

		//write output
		fout<<"Case #"<<index<<": "<<trainsCountA<<" "<<trainsCountB<<"\n";
	}

	fin.close();
	fout.close();
}