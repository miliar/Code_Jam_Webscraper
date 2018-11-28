
#include "stdafx.h"
#include "stdio.h"
#include <list>
#pragma warning(disable : 4996)

int GetTimeInMinutes(FILE *stream) {
	int hours=0, minutes=0;
	fscanf(stream, "%d:%d ", &hours, &minutes);
	return 60 * hours + minutes;
}

enum Action {kDepart, kArrive};
enum Station {kStationA, kStationB};

class Event {
public:
	Event(int time, Action action, Station station) : m_time(time), m_action(action), m_station(station) {};
	int m_time;		// In minutes.
	Action m_action;
	Station m_station;
	bool Before(const Event& rhs) const;
	void Print() const {printf("Event: (%d) %s %s\n", m_time, m_action ? "Arrive" : "Depart", m_station ? "B" : "A");}
};

bool Event::Before(const Event &rhs) const {
	if (m_time < rhs.m_time)
		return true;
	if (m_time > rhs.m_time)
		return false;
	return m_action == kArrive;		// Arrivals come before departures, because they are ready for immediate departure in case of a tie.
}

typedef std::list<Event> EventList;

void AddEvent(EventList &list, const Event &evt) {
	for (EventList::iterator i = list.begin(); i!=list.end(); ++i)
		if (evt.Before(*i)) {
			list.insert(i, evt);
			return;
		}
	list.push_back(evt);
}

void ProcessCase(FILE *stream, int caseNum) {
	int turnAround = 0;
	fscanf(stream, "%d ", &turnAround);
	int firstDir=0, secondDir=0;
	fscanf(stream, " %d %d ", &firstDir, &secondDir);
	int i;
	EventList sched;
	for (i=0; i<firstDir; ++i) {
		AddEvent(sched, Event(GetTimeInMinutes(stream), kDepart, kStationA));
		AddEvent(sched, Event(GetTimeInMinutes(stream)+turnAround, kArrive, kStationB));
	}
	for (i=0; i<secondDir; ++i) {
		AddEvent(sched, Event(GetTimeInMinutes(stream), kDepart, kStationB));
		AddEvent(sched, Event(GetTimeInMinutes(stream)+turnAround, kArrive, kStationA));
	}
	int availA=0, availB=0, neededA=0, neededB=0;
	for (EventList::const_iterator i=sched.begin(); i!=sched.end(); ++i) {
		Event evt = *i;
		if (evt.m_action == kDepart) {
			if (evt.m_station == kStationA) {
				if (availA)
					--availA;
				else
					++neededA;
			} else {	// kStationB
				if (availB)
					--availB;
				else
					++neededB;
			}
		} else {	// Arrive
			if (evt.m_station == kStationA) {
				++availA;
			} else {	// kStationB
				++availB;
			}
		}
	}
	printf("Case #%d: %d %d\n", caseNum, neededA, neededB);
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 1;
	FILE *stream = fopen(argv[1], "r");
	if (!stream)
		return 1;

	int numCases;
	fscanf(stream, "%d ", &numCases);
	for (int i=0; i<numCases; ++i)
		ProcessCase(stream, i+1);

	return 0;
}

