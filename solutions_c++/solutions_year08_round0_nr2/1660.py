#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <queue>

using namespace std;

bool debug(false);
bool debugT(false);
//~ fstream fin("B-small-attempt2.in");
//~ #define cin fin

class Event
{
public:
	Event(int atime, bool arrive, bool stati)
	{
		time = atime;
		arrivalA = arrive;
		stationA = stati;
	}
	~Event() { }
	
	int  getTime() const { return time; }
	bool arrival() const { return arrivalA; }
	bool station() const { return stationA; }
private:
	int time;
	bool arrivalA; //arrival = true, departure = false
	bool stationA; //A=true, B=false
};

void getEvents(int count, vector<Event>& events, int stat)
{
	string trainstart, trainend;
	string hr, min;
	int tmpHr, tmpMin;
	int starttime, endtime;
	
	for (int j=0; j < count; j++)
	{
		cin >> trainstart >> trainend;
		
		hr = trainstart.substr(0,2);
		min = trainstart.substr(3,4);
		
		istringstream s1(hr);
		s1 >> tmpHr;
		istringstream s2(min);
		s2 >> tmpMin;

		starttime = tmpHr * 60 + tmpMin;
		Event e1(starttime, -1, stat);
		events.push_back(e1);
		
		hr = trainend.substr(0,2);
		min = trainend.substr(3,4);
		
		istringstream s3(hr);
		s3 >> tmpHr;
		istringstream s4(min);
		s4 >> tmpMin;
		
		endtime = tmpHr * 60 + tmpMin;
		cout << "!stat " << !stat << endl;
		Event e2(endtime, 1, !stat);
		events.push_back(e2);
		
	}
}

struct test_compare
: binary_function<Event*, Event*, bool>
{
	bool operator()(const Event* e1, const Event* e2) const
	{
		return (e1->getTime() > e2->getTime() ||
		(e1->getTime() == e2->getTime() && (!e1->arrival() && e2->arrival())));
	}
};

int main()
{
	int numcases, turnaround, NA, NB;
	cin >> numcases;
	
	for (int i=1; i <= numcases; i++)
	{
		cout << "Case #" << i << ": ";
		
		cin >> turnaround >> NA >> NB;
		
		priority_queue<Event*, vector<Event*>, test_compare> events;
		
		{
			string trainstart, trainend;
			string hr, min;
			int tmpHr, tmpMin;
			int starttime, endtime;
			bool stat = true;
			
			for (int j=0; j < (NA + NB); j++)
			{
				if (j >= NA) stat = false;
				
				cin >> trainstart >> trainend;
				
				hr = trainstart.substr(0,2);
				min = trainstart.substr(3,4);
				
				istringstream s1(hr);
				s1 >> tmpHr;
				istringstream s2(min);
				s2 >> tmpMin;

				starttime = tmpHr * 60 + tmpMin;

				events.push(new Event(starttime, false, stat));
				
				hr = trainend.substr(0,2);
				min = trainend.substr(3,4);
				
				istringstream s3(hr);
				s3 >> tmpHr;
				istringstream s4(min);
				s4 >> tmpMin;
				
				endtime = tmpHr * 60 + tmpMin;
	
				events.push(new Event(endtime, true, !stat));
			}	
		}
		
		int lastarrivalA = 0;
		int lastarrivalB = 0;

		priority_queue<Event*, vector<Event*>, test_compare> atrains;
		priority_queue<Event*, vector<Event*>, test_compare> btrains;

		int finalA = 0;
		int finalB = 0;
		
		while(!events.empty())
		{
			Event* curevent = events.top();
			events.pop();
			bool dt = curevent->arrival();
			string dtstr;
			if (dt) dtstr = "arrival";
			else dtstr = "departure";
			if (debugT) cout << "time= " << curevent->getTime() << " " << dtstr << endl;
			if (!curevent->arrival())
			{
				if (curevent->station())
				{
					Event* tmp = atrains.top();
					if (!atrains.empty() && ((curevent->getTime() - tmp->getTime()) >= turnaround))
					{
						if (debug) cout << "a trains-- " << curevent->getTime() << endl;
						atrains.pop();
					}
					else
					{ 
						finalA++; 
						if (debug) cout << "a++ " << curevent->getTime() << endl;
					}
				}
				else
				{					Event* tmp = btrains.top();
					if (!btrains.empty() && ((curevent->getTime() - tmp->getTime()) >= turnaround))
					{
						if (debug) cout << "b trains-- " << curevent->getTime() << endl;
						btrains.pop();
						
					}
					else
					{ 
						finalB++; 
						if (debug) cout << "b++ " << curevent->getTime() << endl;
					}					
				}
			}
			else
			{
				if (!curevent->station())
				{
					btrains.push(new Event(curevent->getTime(), false, false));
					if (debug) cout << "b trains++ " << curevent->getTime() << endl;
				}
				else
				{
					atrains.push(new Event(curevent->getTime(), false, false));
					if (debug) cout << "a trains++ " << curevent->getTime() << endl;
				}	
			}
		}
		cout << finalA << " " << finalB << endl;
		
	}
	
	
	
}
