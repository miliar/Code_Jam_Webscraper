#include <cstdio>
#include <vector>
#include <string>
#include <queue>

using namespace std;

class CTTime
{
public:
	int hour;
	int min;

public:
	CTTime() : hour(0), min(0) {}
	CTTime(int hour, int min) : hour(hour), min(min) {}

	CTTime &operator +(const CTTime &a)
	{
		hour += a.hour;
		min += a.min;

		if (min >= 60)
		{
			min -= 60;
			++hour;
		}

		return *this;
	}

	bool operator <(const CTTime &a) const
	{
		if (hour == a.hour)
		{
			return min > a.min;
		}

		return hour > a.hour;
	}

	bool operator ==(const CTTime &a)
	{
		return (hour == a.hour && min == a.min);
	}
};

class CEEvent : public CTTime
{
public:
	int eventType;
	int station;
	int index;

public:
	CEEvent(const CTTime &a) : CTTime(a), eventType(0), station(0), index(0) {}

	bool operator <(const CEEvent &a) const
	{
		if (hour == a.hour && min == a.min)
		{
			return (eventType < a.eventType);
		}

		return CTTime::operator <(a);
	}
};

typedef pair<CTTime, CTTime> Schedule;

int itime;
CTTime ttime;
int na, nb;
vector<Schedule> scheduleA, scheduleB;
priority_queue<CEEvent> eventQueue;
int trainA, trainB;

int sola, solb;

void solve(void)
{
	while (!eventQueue.empty())
	{
		CEEvent now = eventQueue.top();
		eventQueue.pop();

		if (now.eventType == 0) // departure
		{
			if (now.station == 0)
			{
				if (trainA == 0)
				{
					++sola;
				}
				else
				{
					--trainA;
				}

				CEEvent next = CEEvent(scheduleA[now.index].second + ttime);
				next.eventType = 1;
				next.station = 1;
				next.index = -1;

				eventQueue.push(next);
			}
			else
			{
				if (trainB == 0)
				{
					++solb;
				}
				else
				{
					--trainB;
				}

				CEEvent next = CEEvent(scheduleB[now.index].second + ttime);
				next.eventType = 1;
				next.station = 0;
				next.index = -1;

				eventQueue.push(next);
			}
		}
		else if (now.eventType == 1) // arrive & ready
		{
			if (now.station == 0)
			{
				++trainA;
			}
			else
			{
				++trainB;
			}
		}
	}
}

int main(void)
{
	FILE *fin = fopen("b.in", "r");
	FILE *fout = fopen("b.out", "w");

	int T;
	fscanf(fin, "%d ", &T);
	for (int t = 1 ; t <= T ; ++t)
	{
		scheduleA.clear();
		scheduleB.clear();
		while (!eventQueue.empty()) eventQueue.pop();
		trainA = trainB = 0;
		sola = solb = 0;

		fscanf(fin, "%d ", &itime);
		ttime = CTTime(itime/60, itime%60);

		fscanf(fin, "%d %d ", &na, &nb);
		for (int i = 0 ; i < na ; ++i)
		{
			int dh, dm, ah, am;
			fscanf(fin, "%d:%d %d:%d ", &dh, &dm, &ah, &am);

			CTTime departure(dh, dm), arrive(ah, am);
			scheduleA.push_back(Schedule(departure, arrive));

			CEEvent devent(departure);
			devent.eventType = 0;
			devent.station = 0;
			devent.index = i;

			eventQueue.push(devent);
		}

		for (int i = 0 ; i < nb ; ++i)
		{
			int dh, dm, ah, am;
			fscanf(fin, "%d:%d %d:%d ", &dh, &dm, &ah, &am);

			CTTime departure(dh, dm), arrive(ah, am);
			scheduleB.push_back(Schedule(departure, arrive));

			CEEvent devent(departure);
			devent.eventType = 0;
			devent.station = 1;
			devent.index = i;

			eventQueue.push(devent);
		}

		solve();

		fprintf(fout, "Case #%d: %d %d\n", t, sola, solb);
	}

	fclose(fin);
	fclose(fout);
}