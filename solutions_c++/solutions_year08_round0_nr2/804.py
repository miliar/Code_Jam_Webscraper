#include <iostream>
#include <queue>
#include <functional>
using namespace std;


enum EventType
{
	EVENT_REQUEST_DEPARTURE,
	EVENT_ARRIVAL
};

struct Event
{
	Event () {}
	Event (EventType etype, int time, int add) : eventType (etype), eventTime (time), additional (add) {}
	EventType eventType;
	int eventTime;
	int additional;

	bool operator > (const Event& other) const
	{
		if (eventTime != other.eventTime)
			return eventTime > other.eventTime;
		return eventType < other.eventType;

	}
};


//read the time in hh:mm format and returns the time in minutes after 00:00
int readTime (istream& stream)
{
	int hours;
	stream >> hours;
	
	char delim;
	stream >> delim;

	int minutes;
	stream >> minutes;

	return hours*60 + minutes;
}



int main (int argc, char* argv[])
{
	if (argc >= 2)
		freopen (argv[1], "r", stdin);
	if (argc >= 3)
		freopen (argv[2], "w", stdout);

	int N;
	cin >> N;
	for (int t = 0; t < N; ++t)
	{
		int T;
		cin >> T;


		int NA, NB;
		cin >> NA >> NB;

		priority_queue <Event, vector<Event>, greater<Event> > events;
		for (int i = 0; i < NA + NB; ++i)
		{
			int from = (i >= NA), to = 1 - from;
			int departure = readTime (cin);
			int arrival = readTime (cin) + T; //since the train is unusable until it turns around

			events.push (Event (EVENT_REQUEST_DEPARTURE, departure, from) );
			events.push (Event (EVENT_ARRIVAL, arrival, to) );
		}

		int trains[2] = {0, 0};
		int total[2] = {0, 0};

		while (!events.empty ())
		{
			Event ev = events.top ();
			events.pop ();

			switch (ev.eventType)
			{
			case EVENT_REQUEST_DEPARTURE:
				if (trains[ev.additional] == 0)
					++total[ev.additional];
				else
					--trains[ev.additional];
				break;
			case EVENT_ARRIVAL:
				++trains[ev.additional];
			}
		}
		cout << "Case #" << t + 1 << ": " << total[0] << ' ' << total[1] << '\n';
	}

	return 0;
}
