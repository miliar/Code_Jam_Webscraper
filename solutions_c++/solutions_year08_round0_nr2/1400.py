// Train TimeTable.cpp : Defines the entry point for the console application.
#include <iostream>
#include <fstream>

using namespace std;

enum STATION{A, B};

struct Schedule
{
	int departure;
	int arrival;
	STATION dest;
	Schedule* nextSche;
};

struct Train
{
	int readyTime;
	STATION dest;
};

int readNextField(ifstream& input, char* field)
{
	if(input.eof())
		return 0;

	char temp;
	int index = 0;

	input.read(&temp, 1);
	while(!input.eof() && temp != ' ' && temp != '\n'){		
		field[index] = temp;
		index++;
		input.read(&temp, 1);
	}
	return index;
}

int skipNextField(ifstream& input)
{
	if(input.eof())
		return 0;

	char temp;
	int index = 0;

	input.read(&temp, 1);
	while(!input.eof() && temp != ' ' && temp != '\n'){		
		index++;
		input.read(&temp, 1);
	}
	return index;
}

int main()
{
	ifstream inputFile("B-large.in", ios::in);

	if(!inputFile)
	{
		cerr<<"File could not be opened"<<endl;
		exit(1);
	}

	//read number of cases
	int numberOfCase;
	inputFile>>numberOfCase;

	int turnaround;
	int na;
	int nb;
	Schedule* scheduleHead = NULL;
	for(int i=1;i<=numberOfCase;i++)
	{
		inputFile>>turnaround;
		inputFile>>na;
		inputFile>>nb;
		//system("pause");

		//skipNextField(inputFile);

		//read the A to B schedule		
		for(int j=0;j<na;j++)
		{
			Schedule* sche = new Schedule();
			int timeTemp;
			//readNextField(inputFile, sche->departure);
			//sche->departure[5] = 0;
			//system("pause");

			//read departure time
			inputFile>>timeTemp;
			sche->departure = timeTemp*60;
			char input;
			inputFile.read(&input, 1);
			inputFile>>timeTemp;
			sche->departure += timeTemp;

			//read arrival time
			inputFile>>timeTemp;
			sche->arrival = timeTemp*60;			
			inputFile.read(&input, 1);
			inputFile>>timeTemp;
			sche->arrival += timeTemp;

			sche->dest = B;

			//sort the schedule in increasing order
			Schedule* temp = scheduleHead;
			Schedule* prev = NULL;			
			if(temp != NULL)
			{
				while(sche->departure >= temp->departure)
				{
					prev = temp;
					if(temp->nextSche != NULL)
						temp = temp->nextSche;
					else
					{
						temp = NULL;
						break;
					}
				}
				if(prev == NULL)
				{
					sche->nextSche = scheduleHead;
					scheduleHead = sche;
				}
				else
				{
					sche->nextSche = temp;
					prev->nextSche = sche;
				}
			}
			else
			{
				sche->nextSche = NULL;
				scheduleHead = sche;				
			}			
		}

		//read the B to A schedule				
		for(int j=0;j<nb;j++)
		{
			Schedule* sche = new Schedule();
			int timeTemp;
			//readNextField(inputFile, sche->departure);
			//sche->departure[5] = 0;
			//system("pause");

			//read departure time
			inputFile>>timeTemp;
			sche->departure = timeTemp*60;
			char input;
			inputFile.read(&input, 1);
			inputFile>>timeTemp;
			sche->departure += timeTemp;

			//read arrival time
			inputFile>>timeTemp;
			sche->arrival = timeTemp*60;			
			inputFile.read(&input, 1);
			inputFile>>timeTemp;
			sche->arrival += timeTemp;

			sche->dest = A;

			//sort the schedule in increasing order
			Schedule* temp = scheduleHead;
			Schedule* prev = NULL;			
			if(temp != NULL)
			{
				while(sche->departure >= temp->departure)
				{
					prev = temp;
					if(temp->nextSche != NULL)
						temp = temp->nextSche;
					else
					{
						temp = NULL;
						break;
					}
				}
				if(prev == NULL)
				{
					sche->nextSche = scheduleHead;
					scheduleHead = sche;
				}
				else
				{
					sche->nextSche = temp;
					prev->nextSche = sche;
				}
			}
			else
			{
				sche->nextSche = NULL;
				scheduleHead = sche;				
			}			
		}	

		//calculate number of trains at A and B		
		Train trains[200];
		int numberOfTrain = 0;
		int trainAtA = 0;
		int trainAtB = 0;
		int totaln = na+nb;		
		Schedule* calTemp = scheduleHead;		
		for(int k=0;k<totaln;k++)
		{
			if(calTemp->dest == A)
			{
				bool haveTrain = false;
				for(int m=0;m<numberOfTrain;m++)
				{
					if((trains[m].dest == B) && (trains[m].readyTime <= calTemp->departure))
					{
						haveTrain = true;
						trains[m].readyTime = calTemp->arrival + turnaround;
						trains[m].dest = calTemp->dest;
						break;
					}
				}
				if(!haveTrain)
				{
					numberOfTrain++;
					trainAtB++;
					trains[numberOfTrain-1].readyTime = calTemp->arrival + turnaround;
					trains[numberOfTrain-1].dest = A;
				}
			}
			else
			{
				bool haveTrain = false;
				for(int m=0;m<numberOfTrain;m++)
				{
					if((trains[m].dest == A) && (trains[m].readyTime <= calTemp->departure))
					{
						haveTrain = true;
						trains[m].readyTime = calTemp->arrival + turnaround;
						trains[m].dest = calTemp->dest;
						break;
					}
				}
				if(!haveTrain)
				{
					numberOfTrain++;
					trainAtA++;
					trains[numberOfTrain-1].readyTime = calTemp->arrival + turnaround;
					trains[numberOfTrain-1].dest = B;
				}
			}
			calTemp = calTemp->nextSche;
		}

		cout<<"Case #"<<i<<": "<<trainAtA<<" "<<trainAtB<<endl;

		Schedule* deleteTemp = scheduleHead;
		Schedule* deleteNext = NULL;
		while(deleteTemp!=NULL)
		{
			deleteNext = deleteTemp->nextSche;
			delete deleteTemp;
			deleteTemp = deleteNext;
		}
		scheduleHead = NULL;
	}

	system("pause");
	return 0;
}
