#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <stack>

using namespace std;

class Event {
public:
	int		tid;		// Train ID
	int		type;		// 0: departure, 1: arrival
	int		dir;		// 0: A->B, 1: B->A
	int		time;		// Minutes from 00:00
	Event	*pArrival;	// Used by departure event: its correspondant arrival event
};

char* trim (char *str) {
	while(strlen(str) > 0 && (str[strlen(str)-1] == '\n' || str[strlen(str)-1] == '\r')) {
		str[strlen(str)-1] = '\0';
	}
	return str;
}

int compareEvent (const void *elem1, const void *elem2) {
	const Event	*e1 = *((Event**)elem1), *e2 = *((Event**)elem2);
	if(e1->time < e2->time)
		return -1;
	else if(e1->time > e2->time)
		return 1;
	else {
		// Arrival event should be handled first
		if(e1->type == 1)
			return -1;
		else if(e2->type == 1)
			return 1;
		else
			return 0;
	}
}

pair<int, int> processCase (FILE *fp) {
	int				T, NA, NB;
	char			buffer[1024];
	pair<int, int>	result;
	Event			*events, **event_order;
	stack<int>		a_trains, b_trains;

	fscanf(fp, "%d\n", &T);
	fscanf(fp, "%d %d\n", &NA, &NB);

	if(NA == 0 && NB == 0) {
		return make_pair(0, 0);
	}

	int	event_count = (NA+NB) * 2;
	events = new Event[event_count];
	event_order = new Event*[event_count];

	int	cur = 0;
	for(int i=0; i<NA; i++) {
		int	dh, dm, ah, am;
		fscanf(fp, "%d:%d %d:%d\n", &dh, &dm, &ah, &am);
		//printf("%d:%d %d:%d\n", dh, dm, ah, am);
		events[cur].tid 		= -1;
		events[cur].type		= 0;
		events[cur].dir			= 0;
		events[cur].time		= 60 * dh + dm;
		events[cur].pArrival	= events + cur + 1;
		event_order[cur]		= events + cur;
		cur++;
		events[cur].tid 		= -1;
		events[cur].type		= 1;
		events[cur].dir			= 0;
		events[cur].time		= 60 * ah + am + T;
		events[cur].pArrival	= NULL;
		event_order[cur]        = events + cur;
		cur++;

		a_trains.push(NA-i);
	}

	for(int i=0; i<NB; i++) {
		int	dh, dm, ah, am;
		fscanf(fp, "%d:%d %d:%d\n", &dh, &dm, &ah, &am);
		//printf("%d:%d %d:%d\n", dh, dm, ah, am);
		events[cur].tid 		= -1;
		events[cur].type		= 0;
		events[cur].dir			= 1;
		events[cur].time		= 60 * dh + dm;
		events[cur].pArrival	= events + cur + 1;
		event_order[cur]        = events + cur;
		cur++;
		events[cur].tid 		= -1;
		events[cur].type		= 1;
		events[cur].dir			= 1;
		events[cur].time		= 60 * ah + am + T;
		events[cur].pArrival	= NULL;
		event_order[cur]        = events + cur;
		cur++;

		b_trains.push(-(NB-i));
	}

	if(cur != event_count)
		throw "cur != event_count";

	qsort(event_order, event_count, sizeof(Event*), compareEvent);

	for(int i=0; i<event_count; i++) {
		Event		&event = *(event_order[i]);

		if(event.type == 0)	{
			// Departure
			if(event.dir == 0) {
				// A->B
				int	train = a_trains.top();
				a_trains.pop();
				if(train > 0 && train > result.first)
					result.first = train;
				event.tid = event.pArrival->tid = train;
			} else {
				// B->A
				int	train = b_trains.top();
				b_trains.pop();
				if(train < 0 && -train > result.second)
					result.second = -train;
				event.tid = event.pArrival->tid = train;
			}
		} else {
			// Arrival
			if(event.dir == 0) {
				// A->B
				b_trains.push(event.tid);
			} else {
				// B->A
				a_trains.push(event.tid);
			}
		}

		//printf("Event %d:\n  tid\t= %d\n  type\t= %s\n  dir\t= %s\n  time\t= %d\n", 
		//		i, event.tid, event.type==0?"departure":"arrival", event.dir==0?"A->B":"B->A", event.time);
	}

	delete [] events;
	delete [] event_order;

	return result;
}

int main (int argc, char **argv) {
	if(argc != 2) {
		printf("Usage: a.out input_file\n");
		return -1;
	}

	// Read input
	FILE	*fp = fopen(argv[1], "r");
	int		N, result;
	
	try {
		fscanf(fp, "%d\n", &N);
		for(int i=0; i<N; i++) {
			pair<int, int>	result = processCase(fp);
			printf("Case #%d: %d %d\n", i+1, result.first, result.second);
		}
	} catch (const char *msg) {
		printf("Error: %s\n", msg);
		return -1;
	}

	fclose(fp);

	return 0;
}

