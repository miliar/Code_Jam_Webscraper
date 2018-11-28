#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef int timex;
enum place {A,B,AB,BA};

struct train
{
	place current;
	timex nextReady;
	place origin;
};

vector<train> trains;
vector<pair<int,int>> scheduleA, scheduleB;

int turnaround = 0;
int cases = 0;

timex now = 0;

int charToInt(char ch)
{
	switch(ch)
	{
	case '0':
		return 0;
	case '1':
		return 1;
	case '2':
		return 2;
	case '3':
		return 3;
	case '4':
		return 4;
	case '5':
		return 5;
	case '6':
		return 6;
	case '7':
		return 7;
	case '8':
		return 8;
	case '9':
		return 9;
	}
}

void addSchedA(char times[])
{
	int h11 = charToInt(times[0]);
	int h12 = charToInt(times[1]);
	int m11 = charToInt(times[3]);
	int m12 = charToInt(times[4]);

	int h21 = charToInt(times[6]);
	int h22 = charToInt(times[7]);
	int m21 = charToInt(times[9]);
	int m22 = charToInt(times[10]); 

	pair<int,int> sched(h11*10*60+h12*60+m11*10+m12,
						h21*10*60+h22*60+m21*10+m22);

	scheduleA.push_back(sched);
}

void addSchedB(char times[])
{
	int h11 = charToInt(times[0]);
	int h12 = charToInt(times[1]);
	int m11 = charToInt(times[3]);
	int m12 = charToInt(times[4]);

	int h21 = charToInt(times[6]);
	int h22 = charToInt(times[7]);
	int m21 = charToInt(times[9]);
	int m22 = charToInt(times[10]); 

	pair<int,int> sched(h11*10*60+h12*60+m11*10+m12,
						h21*10*60+h22*60+m21*10+m22);

	scheduleB.push_back(sched);
}

void getParameters(ifstream& inFile)
{
	trains.clear();
	scheduleA.clear();
	scheduleB.clear();

	now = 0;

	char temp[100];
	int asched,bsched;

	inFile>>turnaround;
	inFile.getline(temp,100);
	
	inFile>>asched;
	inFile>>bsched;
	inFile.getline(temp,100);

	for(int i=0; i<asched; i++)
	{
		inFile.getline(temp,100);
		addSchedA(temp);
	}

	for(int i=0; i<bsched; i++)
	{
		inFile.getline(temp,100);
		addSchedB(temp);
	}
}

int existA()
{
	for(int i=0; i<trains.size(); i++)
	{
		if(trains[i].current==place::A)
			return i;
	}

	return -1;
}

int existB()
{
	for(int i=0; i<trains.size(); i++)
	{
		if(trains[i].current==place::B)
			return i;
	}

	return -1;
}

void checkSchedA()
{
	for(int i=0; i<scheduleA.size(); i++)
	{
		if(scheduleA[i].first==now)
		{
			int index = existA();

			if(index==-1)
			{
				index = trains.size();
				train newone;
				trains.push_back(newone);
				trains[index].origin = place::A;
			}
			
			trains[index].current = place::AB;
			trains[index].nextReady = scheduleA[i].second+turnaround;
		}
	}
}

void checkSchedB()
{
	for(int i=0; i<scheduleB.size(); i++)
	{
		if(scheduleB[i].first==now)
		{
			int index = existB();

			if(index==-1)
			{
				index = trains.size();
				train newone;
				trains.push_back(newone);
				trains[index].origin = place::B;
			}
			
			trains[index].current = place::BA;
			trains[index].nextReady = scheduleB[i].second+turnaround;
		}
	}
}

void updateTrains()
{
	for(int i=0; i<trains.size(); i++)
	{
		if(trains[i].nextReady==now)
		{
			trains[i].nextReady = 0;

			if(trains[i].current==place::AB)
				trains[i].current=place::B;
			else if(trains[i].current==place::BA)
				trains[i].current=place::A;
		}
	}
}

void simulate()
{
	for(now=0; now<24*60; now++)
	{
		updateTrains();
		checkSchedA();
		checkSchedB();
	}
}

int trainsAtA()
{
	int count = 0;

	for(int i=0; i<trains.size(); i++)
	{
		if(trains[i].origin==place::A)
			count++;
	}

	return count;
}

int trainsAtB()
{
	int count = 0;

	for(int i=0; i<trains.size(); i++)
	{
		if(trains[i].origin==place::B)
			count++;
	}

	return count;
}

int main()
{
	char fname[100], temp[100];

	cin.getline(fname,100);

	ifstream inFile(fname);

	string outname = fname;
	outname+= ".out";

	ofstream outFile(outname.c_str());

	inFile>>cases;
	inFile.getline(temp,100);

	for(int i=1; i<=cases; i++)
	{	
		getParameters(inFile);

		simulate();

		outFile<<"Case #"<<i<<": "<<trainsAtA()<<" "<<trainsAtB()<<endl;
		cout<<endl<<"Case #"<<i<<": "<<trainsAtA()<<" "<<trainsAtB();
	}
	
	inFile.close();
	outFile.close();

	return 0;
}