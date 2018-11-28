#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <cassert>

using namespace std;

/*
When there is nothing left to burn
you have to set yourself on fire.
 */

class Event
{
public:
	Event(int t, int i) : time(t), ID(i) {}
	int time;
	int ID;
	bool operator<(const Event &other) const
	{
		if(time == other.time)
			return ID < other.ID;
		else return time > other.time;
	}
};

const int departA = 0;
const int departB = 1;
const int arriveA = 2;
const int arriveB = 3;

int timetoi(string time)
{
	return 10*60*time[0]+60*time[1]+10*time[3]+time[4];
}

int main(int argc, char *argv[])
{
	assert(argc > 1);
	ifstream ifile(argv[1]);
	
	int cases=0;
	ifile >> cases;
	for(int caseno=1; caseno<=cases; caseno++)
	{
		int turntime=0;
		ifile >> turntime;
		int NA=0, NB=0;
		ifile >> NA >> NB;
		priority_queue<Event> q;
		for(int i=0; i<NA; i++)
		{
			string time1, time2;
			ifile >> time1 >> time2;
			q.push(Event(timetoi(time1), departA) );
			q.push(Event(timetoi(time2)+turntime, arriveB) );
		}

		for(int i=0; i<NB; i++)
		{
			string time1, time2;
			ifile >> time1 >> time2;
			q.push(Event(timetoi(time1), departB) );
			q.push(Event(timetoi(time2)+turntime, arriveA) );
		}
		
		int trainsA=0, trainsB=0;
		int needA=0, needB=0;
		while(!q.empty())
		{
			Event e = q.top();
			q.pop();
			switch(e.ID)
			{
			case arriveA:
				trainsA++;
				break;
			case arriveB:
				trainsB++;
				break;
			case departA:
				if(trainsA > 0)
					trainsA--;
				else
					needA++;
				break;
			case departB:
				if(trainsB > 0)
					trainsB--;
				else
					needB++;
				break;
			default:
				assert(false);
			}
		}

		cout << "Case #" << caseno << ": " << needA << " " << needB << endl;
	}
	
	
}