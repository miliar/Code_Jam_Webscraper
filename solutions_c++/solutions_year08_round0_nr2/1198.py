
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;



//-----------------------------------------------------------------------------
class TrainEvent
{
public:
	TrainEvent(int time, int event)	{
		_time = time;
		_event = event;
	}

	TrainEvent(const TrainEvent& evt) {
		_time = evt._time;
		_event = evt._event;
	}

	TrainEvent& operator = (const TrainEvent& evt) {
		_time = evt._time;
		_event = evt._event;
		return *this;
	}

	int time(void) const { return _time; }
	int event(void) const { return _event; }

protected:
	int _time;
	int _event;
};


//-----------------------------------------------------------------------------
bool operator < (const TrainEvent& lhs, const TrainEvent& rhs)
{
	// It is important that arrival events take precedence over departure events
	if (lhs.time() == rhs.time()) {

		// Must return false if both events are the same
		if (lhs.event() == rhs.event()) {
			return false;
		}

		if (lhs.event() == 1) {
			return true;

		} else {
			return false;
		}
	}

    return lhs.time() < rhs.time();
}



//-----------------------------------------------------------------------------
void dbgprint(const vector<TrainEvent>& events)
{
	for (int i=0; i < events.size(); i++) {
		cout << "t: " << events[i].time() << " e: " << events[i].event() << endl;
	}
}


//-----------------------------------------------------------------------------
int initialTrainsNeeded(vector<TrainEvent>& station)
{

	// Sort
	sort(station.begin(), station.end());
	//dbgprint(station);

	// Run through the vector
	int trains = 0;
	int needed = 0;

	for (unsigned int i=0; i < station.size(); i++) {

		// Train.event is 1 for arrival of a train, -1 for departure
		trains += station[i].event();
		if (trains < needed) {
			needed = trains;
		}
	}

	// We need as many initial trains as this is in the negative
	if (needed < 0) {
		return abs(needed);

	} else {
		return 0;
	}
}




//-----------------------------------------------------------------------------
int timeToMinutes(const string& time)
{
	string hr;
	string mn;

	int separator = time.find(':');

	hr = time.substr(0, separator);
	mn = time.substr(separator+1);

	return (atoi(hr.c_str()) * 60) + atoi(mn.c_str());
}



//-----------------------------------------------------------------------------
void testCase(int iteration)
{
	int turnaroundTime;
	int tripsFromA;
	int tripsFromB;

	vector<TrainEvent> stationA;
	vector<TrainEvent> stationB;

	// Read turnaround time
	cin >> turnaroundTime;

	// Read Trip Count
	cin >> tripsFromA;
	cin >> tripsFromB;


	// Parse station A events
	for (int i=0; i < tripsFromA; i++) {
		string departureTime;
		string arrivalTime;

		cin >> departureTime;
		cin >> arrivalTime;	

		// At departure, a train leaves A
		stationA.push_back(TrainEvent(timeToMinutes(departureTime), -1));

		// At arrival plus turnaround time, a train "technically" arrives at B
		stationB.push_back(TrainEvent(timeToMinutes(arrivalTime) + turnaroundTime, 1));
	}


	// Parse station B events
	for (int i=0; i < tripsFromB; i++) {
		string departureTime;
		string arrivalTime;

		cin >> departureTime;
		cin >> arrivalTime;	

		// At departure, a train leaves B
		stationB.push_back(TrainEvent(timeToMinutes(departureTime), -1));

		// At arrival plus turnaround time, a train "technically" arrives at A
		stationA.push_back(TrainEvent(timeToMinutes(arrivalTime) + turnaroundTime, 1));
	}


	// Now we can calculate trains needed
	int trainsNeededAtA = initialTrainsNeeded(stationA);
	int trainsNeededAtB = initialTrainsNeeded(stationB);


	// Output
	cout << "Case #" << (iteration + 1) << ": " << trainsNeededAtA << " " << trainsNeededAtB << endl;
}


//-----------------------------------------------------------------------------
int main(int argc, char* argv[])
{
	int testCases;
	cin >> testCases;
	for (int i=0; i < testCases; i++) {
		testCase(i);
	}

	return 0;
}

