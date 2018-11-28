#include <stdlib.h>
#include <stdio.h>

struct Flight
{
	int Departure;
	int Arrival;
	int Start; // 0 = starts from A; 1=Starts from B
};

struct ListLink
{
	int ReadyTime;
	ListLink* Next;
};

void SortFlights (Flight* Flights, int FlightsNum)
{
	int MinPos;
	Flight tmp;
	for (int i=0; i<FlightsNum-1; i++)
	{
		MinPos = i; 
		for (int j=i+1; j<FlightsNum; j++)
		{
			if (Flights[j].Departure <Flights[MinPos].Departure)
				MinPos = j;
		} 
		tmp = Flights[i];
		Flights[i] = Flights[MinPos];
		Flights[MinPos] = tmp;
	}
}

void InsertLink(ListLink *&Pool, int MyReadyTime)
{
	if (Pool == NULL)
	{
		Pool = new ListLink;
		Pool->ReadyTime = MyReadyTime;
		Pool->Next = NULL;
	}
	else
	{
		if (MyReadyTime < Pool->ReadyTime)
		{
			ListLink* newLink = new ListLink;
			newLink->ReadyTime = MyReadyTime;
			newLink->Next = Pool;
			Pool = newLink;
		}
		else
		{
			ListLink *tmp = Pool;
			while ((tmp->Next != NULL) && (tmp->Next->ReadyTime < MyReadyTime))
			{
				tmp = tmp->Next;
			}
			ListLink* newLink = new ListLink;
			newLink->ReadyTime = MyReadyTime;
			newLink->Next = tmp->Next;
			tmp->Next = newLink;

		}
	}
}

void main()
{
	FILE *InFile, *OutFile;
	InFile = fopen("input.txt", "a+");
	OutFile = fopen("output.txt", "a+");

	int CaseNum;
	fscanf(InFile, "%d", &CaseNum);

	int FromA, FromB;
	int TimeAround;
	int TrainsFromA, TrainsFromB;
	Flight* Flights;

	for (int i=0; i<CaseNum; i++)
	{
		FromA = 0;
		FromB = 0;
		
		fscanf(InFile, "%d", &TimeAround);
		fscanf(InFile, "%d %d", &TrainsFromA, &TrainsFromB);
		Flights = new Flight[TrainsFromA+TrainsFromB];

		for (int k=0; k<TrainsFromA+TrainsFromB; k++)
		{
			int a1, a2, a3, a4;
			fscanf(InFile, "%d:%d %d:%d", &a1, &a2, &a3, &a4);
			Flights[k].Departure = a1*60+a2;
			Flights[k].Arrival = a3*60+a4;
			if (k<TrainsFromA)
				Flights[k].Start = 0;
			else
				Flights[k].Start = 1;
		}
		SortFlights(Flights, TrainsFromA+TrainsFromB);

		ListLink *APool = NULL;
		ListLink *BPool = NULL;

		for (int k=0; k<TrainsFromA+TrainsFromB; k++)
		{
			if (Flights[k].Start == 0)
			{
				if ((APool == NULL) || (APool->ReadyTime > Flights[k].Departure))
					FromA++;
				else
				{
					ListLink *tmp = APool;
					APool = APool->Next;
					delete tmp;
				}
				InsertLink(BPool, Flights[k].Arrival+TimeAround);
			}
			else
			{
				if ((BPool == NULL) || (BPool->ReadyTime > Flights[k].Departure))
					FromB++;
				else
				{
					ListLink *tmp = BPool;
					BPool = BPool->Next;
					delete tmp;
				}
				InsertLink(APool, Flights[k].Arrival+TimeAround);
			}
		}
		

		delete [] Flights;
		fprintf(OutFile, "Case #%d: %d %d\n", i+1, FromA, FromB);
	}

	fclose(InFile);
	fclose(OutFile);
}