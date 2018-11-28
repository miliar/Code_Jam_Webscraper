#include <iostream>
#include <string>
#include <set>
#include <list>
#include <algorithm>
#include <vector>
#include <map>
#include <limits.h>

using namespace std;

#define debug if(0) cout

int parse_time(string time)
{
	time[2] = 0;
	return atoi(time.c_str())*60 + atoi(time.c_str() + 3);
}

typedef enum {AtoB = 0, BtoA = 1} Direction;
class Train
{
public:   
	pair<int, int> course;
	Direction direction;
	enum {Turnarounding, Staying} state;
};

static int _id;
typedef enum {Departure, Arrival} EventType;
class Event
{
public:
	int id;
	int timestamp;
	Direction direction;
	EventType type;
	Event(int _timestamp, Direction _direction, EventType _type) :
		timestamp(_timestamp), direction(_direction), type(_type) { id = _id++;};
};

bool operator<(const Event &a, const Event &b) { return (a.timestamp == b.timestamp)?(a.type > b.type):(a.timestamp < b.timestamp); }

int main()
{
	int cases;

	cin >> cases;
	debug << "Number of cases " << cases << endl;
	
	for(int j = 0;j < cases;j++) {
		int turnaround;
		cin >> turnaround;
		debug << "Turnaround " << turnaround << endl;

		vector<pair<int, int> > abtrains;
		vector<pair<int, int> > batrains;
		vector<Event> events;


		int cnt1, cnt2;
		cin >> cnt1 >> cnt2;
		debug << "From A to B (" << cnt1 << ")"<< endl;
		while(cnt1--) {
			int from, to;
			string timestr;
			cin >> timestr;
			from = parse_time(timestr);
			debug << "Train " << timestr << "(" << from << ") - "; 

			cin >> timestr;
			to = parse_time(timestr);
			debug << timestr << "(" << to << ")" << endl; 

			abtrains.push_back(make_pair(from, to));

			events.push_back(Event(from, AtoB, Departure));
			events.push_back(Event(to + turnaround, AtoB, Arrival));
		}

		debug << "From B to A (" << cnt2 << ")" << endl;
		while(cnt2--) {
			int from, to;
			string timestr;
			cin >> timestr;
			from = parse_time(timestr);
			debug << "Train " << timestr << "(" << from << ") - "; 

			cin >> timestr;
			to = parse_time(timestr);
			debug << timestr << "(" << to << ")" << endl; 

			batrains.push_back(make_pair(from, to));

			events.push_back(Event(from, BtoA, Departure));
			if((*--events.end()).direction == AtoB) 
				cout << "Added A to B" << endl;
			events.push_back(Event(to + turnaround, BtoA, Arrival));
		}

		sort(events.begin(), events.end());


		int createdA = 0;
		int createdB = 0;

		int A_trains = 0;
		int AtoB_trains = 0;
		int B_trains = 0;
		int BtoA_trains = 0;

		for(vector<Event>::iterator i = events.begin();i != events.end();++i) {
			Event e = *i;
			debug << "Event("<<e.id <<")" << " at " << e.timestamp << " ";
			if(e.direction == AtoB) {
				
				debug << "A to B";
				if(e.type == Departure)
				{
					if(A_trains)
						A_trains--;
					else {
						createdA++;
						debug << " (++)";
					}
					AtoB_trains++;
					debug << " Departure";
				}
				else {
					AtoB_trains--;
					B_trains++;
					debug << " Arrival";
				}

				debug << endl;
			}
			else {
				debug << "B to A";
				if(e.type == Departure)
				{
					if(B_trains)
						B_trains--;
					else {
						createdB++;
						debug << " (++)";
					}
					BtoA_trains++;
					debug << " Departure";
				}
				else {
					BtoA_trains--;
					A_trains++;
					debug << " Arrival";
				}

				debug << endl;

			}
		}




		cout << "Case #" << j + 1 << ": "<< createdA << " " << createdB << endl;
	}
	return 0;
}
