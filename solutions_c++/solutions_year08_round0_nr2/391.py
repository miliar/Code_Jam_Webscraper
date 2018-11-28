#include <stdio.h>
#include <stdlib.h>

#define ARRIVAL 0
#define DEPARTURE 1
#define DIR_A 0
#define DIR_B 1

struct event {
	int time;
	char type;
	char dir;
};
typedef struct event event;

int T,NA,NB,event_count;
int available[2], needed[2];
event events[401];

int compare(const void *a, const void *b) {
	if(((event*)a)->time > ((event*)b)->time) {
		return 1;
	}
	if(((event*)a)->time < ((event*)b)->time) {
		return -1;
	}
	return (int)(((event*)a)->type - ((event*)b)->type);
}

void print_events() {
	int i;
	for(i=0; i<event_count; i++) {
		printf("%02d:%02d ",(int)(events[i].time/60),(int)(events[i].time%60));
		if(events[i].type == ARRIVAL) {
			printf("ARRIVAL ");
		} else {
			printf("DEPARTURE ");
		}
		if(events[i].dir == DIR_A) {
			printf("A\n");
			//printf("A (%d %d %d)\n",events[i].time,events[i].type,events[i].dir);
		} else {
			printf("B\n");
			//printf("B (%d %d %d)\n",events[i].time,events[i].type,events[i].dir);
		}
	}
}

void solve(int case_number) {
	//printf("before sort: \n"); print_events();
	qsort(events, event_count, sizeof(event), compare);
	//printf("after sort: \n"); print_events();
	
	available[DIR_A] = 0;
	available[DIR_B] = 0;
	needed[DIR_A] = 0;
	needed[DIR_B] = 0;
	
	int i;
	for(i=0; i<event_count; i++) {
		if(events[i].type == ARRIVAL) {
			available[events[i].dir] ++;
		} else {
			if(available[events[i].dir] > 0) {
				available[events[i].dir] --;
			} else {
				needed[events[i].dir] ++;
			}
		}
	}
	
	printf("Case #%d: %d %d\n", case_number, needed[DIR_A], needed[DIR_B]);
}

int main(void) {
	freopen("B-large.in","rt",stdin);
	freopen("B.out", "wt", stdout);
	
	int N,i,j,h1,m1,h2,m2,t1,t2;
	scanf("%d\n",&N);
	for(i=0; i<N; i++) {
		event_count = 0;
		scanf("%d\n",&T);
		scanf("%d %d\n",&NA,&NB);
		for(j=0; j<NA; j++) {
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			t1 = h1*60 + m1;
			t2 = h2*60 + m2;
			events[event_count].time = t1;
			events[event_count].type = DEPARTURE;
			events[event_count].dir = DIR_A;
			event_count++;
			
			events[event_count].time = t2 + T;
			events[event_count].type = ARRIVAL;
			events[event_count].dir = DIR_B;
			event_count++;
		}
		for(j=0; j<NB; j++) {
			scanf("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
			t1 = h1*60 + m1;
			t2 = h2*60 + m2;
			events[event_count].time = t1;
			events[event_count].type = DEPARTURE;
			events[event_count].dir = DIR_B;
			event_count++;
			
			events[event_count].time = t2 + T;
			events[event_count].type = ARRIVAL;
			events[event_count].dir = DIR_A;
			event_count++;
		}
		solve(i+1);
	}
	
	return 0;
}