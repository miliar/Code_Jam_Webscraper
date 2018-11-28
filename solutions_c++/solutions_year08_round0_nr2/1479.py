#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Event {
	int time;
public:
	bool station; //0=A ; 1=B;
	enum EventType {
		arrival,
		ready
	} eventType;
	Event(EventType et=arrival, int time=0, bool station=false): eventType(et), time(time), station(station) {}
	bool operator < (const Event & b) const {
		if (this->time != b.time)
			return this->time < b.time;
		else
			return this->eventType > b.eventType;
	}
};

int main() {
	int N;
	int nCase = 1;
	for (cin >> N; N; N--) {
		char colon;
		int T;
		cin >> T;
		int NA, NB;
		cin >> NA >> NB;
		vector<Event> events(2*(NA+NB));
		for (int i=0; i<NA; i++) {
			int time, timeTemp; //time = hour , timeTemp = minute
			cin >> time;
			cin >> colon;
			cin >> timeTemp;
			time = time*60 + timeTemp;
			
			events[2*i] = Event(Event::arrival, time, false);

			cin >> time;
			cin >> colon;
			cin >> timeTemp;
			time = time*60 + timeTemp;
			
			events[2*i+1] = Event(Event::ready, time + T, true);
		}

		for (int i=NA; i<NA+NB; i++) {
			int time, timeTemp; //time = hour , timeTemp = minute
			cin >> time;
			cin >> colon;
			cin >> timeTemp;
			time = time*60 + timeTemp;
			
			events[2*i] = Event(Event::arrival, time, true);

			cin >> time;
			cin >> colon;
			cin >> timeTemp;
			time = time*60 + timeTemp;
			
			events[2*i+1] = Event(Event::ready, time + T, false);
		}
		
		sort(events.begin(), events.end());

		int trainsOnA = 0, trainsOnB = 0;
		int trainsStartOnA = 0, trainsStartOnB = 0;

		for (vector<Event>::const_iterator it = events.begin(); it != events.end(); it++) {
			if (it->station == false) { //A trains is getting ready or a train MUST GO (A)
				if (it->eventType == Event::ready) //new train ready to go
					trainsOnA++;
				else { //A train MUST GO
					if (trainsOnA == 0) {
						trainsStartOnA++;
					} else
						trainsOnA--;
				} 
			} else { //A trains is getting ready or a train MUST GO (B)
				if (it->eventType == Event::ready) //new train ready to go
					trainsOnB++;
				else { //A train MUST GO
					if (trainsOnB == 0) {
						trainsStartOnB++;
					} else
						trainsOnB--;
				} 
			}
		}
		cout << "Case #" << nCase++ << ": " << trainsStartOnA << ' ' << trainsStartOnB << '\n';
	}
}