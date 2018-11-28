/* Compile using g++ main.cpp -o main -O2 */
#include <iostream>
#include <stdio.h>

#define NA_MAX 100
#define NB_MAX 100

/* Keeps track of one individual trip arrival and departrue times min minutes */
typedef struct trip {
	int departure;
	int arrival;
	bool used;
} TRIP;

using namespace std;

/* Get minutes and hours form a time format */
int get_hour(char *time);
int get_min(char *time);
TRIP  *sort_by_arr(TRIP trip[],int size);
TRIP  *sort_by_dep(TRIP trip[],int size);

int main() {
	/* Declare all the variables that are needed across the whole program */
	int num_cases;
	scanf("%d\n", &num_cases);	
	for(int casee=1; casee<=num_cases; casee++) {
		int turn_around,na,nb,ab_trips,ba_trips;
		scanf("%d\n", &turn_around);
		scanf("%d %d\n", &na, &nb);
		TRIP *trips_ab = new TRIP[na];
		TRIP *trips_ba = new TRIP[nb];
		/* Read trips from A to B */
		for(int i=0; i<na; i++) {
			char a_time[5];
			char d_time[5];
			scanf("%s %s\n",d_time,a_time);
			trips_ab[i].departure = 60*get_hour(d_time)+get_min(d_time);
			trips_ab[i].arrival = 60*get_hour(a_time)+get_min(a_time);
			trips_ab[i].used = false;
		}
		/* Read trips from B to A */
		for(int i=0; i<nb; i++) {
			char a_time[5];
			char d_time[5];
			scanf("%s %s\n",d_time,a_time);
			trips_ba[i].departure = 60*get_hour(d_time)+get_min(d_time);
			trips_ba[i].arrival = 60*get_hour(a_time)+get_min(a_time);
			trips_ba[i].used = false;
		}
		
		/* Algorithm solving the problem */
		ab_trips = na;
		ba_trips = nb;
		trip *trips_ab_arr_sorted = sort_by_arr(trips_ab, na);
		trip *trips_ab_dep_sorted = sort_by_dep(trips_ab, na);
		trip *trips_ba_arr_sorted = sort_by_arr(trips_ba, nb);
		trip *trips_ba_dep_sorted = sort_by_dep(trips_ba, nb);
		for(int i=0; i<na; i++) {
			for(int j=0; j<nb; j++) {
				if(trips_ab_arr_sorted[i].arrival+turn_around <= trips_ba_dep_sorted[j].departure && trips_ba_dep_sorted[j].used == false) {
					ba_trips--;
					trips_ba_dep_sorted[j].used = true;
					break;
				}
			}
		}
		for(int i=0; i<nb; i++) {
			for(int j=0; j<na; j++) {
				if(trips_ba_arr_sorted[i].arrival+turn_around <= trips_ab_dep_sorted[j].departure && trips_ab_dep_sorted[j].used == false) {
					ab_trips--;
					trips_ab_dep_sorted[j].used = true;
					break;
				}
			}
		}
		
		/* Report the desired result */
		printf("Case #%d: %d %d\n", casee, ab_trips, ba_trips);
		delete trips_ab;
		delete trips_ba;
		delete trips_ab_arr_sorted;
		delete trips_ab_dep_sorted;
		delete trips_ba_arr_sorted;
		delete trips_ba_dep_sorted;
	}
	return 0; 
}

/* Simply decide what to do with the leading zeros */
int get_hour(char *time) {
	if(*time == '0') {
		return atoi((time+1));
	} else {
		char *hours = (char*)malloc(2*sizeof(char));
		hours[0] = *time;
		hours[1] = *(time+1);
		int hour = atoi(hours);
		delete hours;
		return hour;
	}
}

/* Simply decide what to do with the leading zeros */
int get_min(char *time) {
	if(*(time+3) == '0') {
		return atoi((time+4));
	} else {
		char *min = (char*)malloc(2*sizeof(char));
		min[0] = *(time+3);
		min[1] = *(time+4);
		int minute = atoi(min);
		delete min;
		return minute;
	}
}

/* Sort the list by arrival times */
TRIP *sort_by_arr(TRIP trip[],int size) {
	TRIP *sorted = new TRIP[size];
	for(int i=0; i<size; i++) {
		int current_min=24*60+59;
		int current_min_index=0;
		for(int j=0; j<size; j++) {
			if(trip[j].arrival < current_min && trip[j].used == false) {
				current_min = trip[j].arrival;
				current_min_index = j;
			}
		}
		sorted[i].arrival = trip[current_min_index].arrival;
		sorted[i].departure = trip[current_min_index].departure;
		sorted[i].used = false;
		trip[current_min_index].used = true;
	}
	for(int i=0;i<size;i++) {
		trip[i].used = false;
	}
	return sorted;
}

/* Sort by departure times */
TRIP *sort_by_dep(TRIP trip[],int size) {
	TRIP *sorted = new TRIP[size];
	for(int i=0; i<size; i++) {
		int current_min=24*60+59;
		int current_min_index=0;
		for(int j=0; j<size; j++) {
			if(trip[j].departure <= current_min && trip[j].used == false) {
				current_min = trip[j].departure;
				current_min_index = j;
			}
		}
		sorted[i].arrival = trip[current_min_index].arrival;
		sorted[i].departure = trip[current_min_index].departure;
		sorted[i].used = false;
		trip[current_min_index].used = true;
	}
	for(int i=0;i<size;i++) {
		trip[i].used = false;
	}
	return sorted;
}
