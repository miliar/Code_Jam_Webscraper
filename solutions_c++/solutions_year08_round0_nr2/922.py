// Problem Set: Qualifying
// Problem Number: 003

// A train line has two stations on it, A and B. Trains can take trips from A to B or from B 
// to A multiple times during a day. When a train arrives at B from A (or arrives at A from 
// B), it needs a certain amount of time before it is ready to take the return journey - this 
// is the turnaround time. For example, if a train arrives at 12:00 and the turnaround time 
// is 0 minutes, it can leave immediately, at 12:00.

// A train timetable specifies departure and arrival time of all trips between A and B. The 
// train company needs to know how many trains have to start the day at A and B in order to 
// make the timetable work: whenever a train is supposed to leave A or B, there must actually 
// be one there ready to go. There are passing sections on the track, so trains don't 
// necessarily arrive in the same order that they leave. Trains may not travel on trips that 
// do not appear on the schedule. 

#include <cstdlib>
#include <iostream>
#include <algorithm>

int const MAX_TRAINS = 300;

typedef struct
{
	char station_s;
	int time_s, time_e;
}
TRAIN_SCHEDULE;

// int representing the time it is available
typedef int TRAIN;

void make_schedule(TRAIN_SCHEDULE* t, char s, int txh, int txm, int tyh, int tym)
{
	t->station_s = s;
	t->time_s = txh * 60 + txm;
	t->time_e = tyh * 60 + tym;
}

bool sched_compare(TRAIN_SCHEDULE a, TRAIN_SCHEDULE b)
{ return (a.time_s == b.time_s) ? a.time_e < b.time_e : a.time_s < b.time_s; };

int main()
{
	int testcases, tcase, i, j;
	scanf("%d\r\n", &testcases);
	
	int turnaround, na, nb, trainsa, trainsb;
	int txh, txm, tyh, tym;
	
	TRAIN_SCHEDULE* sched; int sched_size;
	TRAIN stationa[MAX_TRAINS], stationb[MAX_TRAINS];
	
	tcase = 0;
	while (tcase++ < testcases)
	{
		// get input data
		scanf("%d\r\n", &turnaround);
		scanf("%d %d\r\n", &na, &nb);
		
		sched_size = na + nb;
		sched = (TRAIN_SCHEDULE*) malloc(sched_size * sizeof(TRAIN_SCHEDULE));
		
		for (i = 0; i < na; ++i)
		{
			scanf("%d:%d %d:%d\r\n", &txh, &txm, &tyh, &tym);
			make_schedule(sched + i, 'a', txh, txm, tyh, tym);
		};
		for (; i < sched_size; ++i)
		{
			scanf("%d:%d %d:%d\r\n", &txh, &txm, &tyh, &tym);
			make_schedule(sched + i, 'b', txh, txm, tyh, tym);
		};
		
		std::sort(sched, sched + sched_size, sched_compare);
		
		trainsa = 0; trainsb = 0; na = 0; nb = 0;
		for (i = 0; i < sched_size; ++i)
		{
			std::sort(stationa, stationa + trainsa);
			std::sort(stationb, stationb + trainsb);
			
			// STATION A
			if (sched[i].station_s == 'a')
			{
				// if there are trains in this station
				if (trainsa)
				{
					// if there are no trains available
					if (sched[i].time_s < *stationa)
					{
						// invent one and account for it in this station
						stationb[trainsb++] = sched[i].time_e + turnaround;
						++na;
					}
					// if there are trains available
					else
					{
						// put a new train in the other station with the correct properties
						stationb[trainsb++] = sched[i].time_e + turnaround;
						
						// remove this train from the current station
						memmove(stationa, stationa + 1, --trainsa * sizeof(TRAIN));
						//for (j = 1; j < trainsa; ++j) stationa[j - 1] = stationa[j]; --trainsa;
					};
				}
				// if there are no trains in this station
				else
				{
					// invent one and account for it in this station
					stationb[trainsb++] = sched[i].time_e + turnaround;
					++na;
				};
			}
			// STATION B
			else
			{
				// if there are trains in this station
				if (trainsb)
				{
					// if there are no trains available
					if (sched[i].time_s < *stationb)
					{
						// invent one and account for it in this station
						stationa[trainsa++] = sched[i].time_e + turnaround;
						++nb;
					}
					// if there are trains available
					else
					{
						// put a new train in the other station with the correct properties
						stationa[trainsa++] = sched[i].time_e + turnaround;
						
						// remove this train from the current station
						memmove(stationb, stationb + 1, --trainsb * sizeof(TRAIN));
						//for (j = 1; j < trainsb; ++j) stationb[j - 1] = stationb[j]; --trainsb;
					};
				}
				// if there are no trains in this station
				else
				{
					// invent one and account for it in this station
					stationa[trainsa++] = sched[i].time_e + turnaround;
					++nb;
				};
			};
		};
		
		printf("Case #%d: %d %d\n", tcase, na, nb);
		free(sched);
	};
};
