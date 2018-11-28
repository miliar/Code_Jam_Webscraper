#include <stdio.h>
#include <stdlib.h>

#define MAX_N 100+2

enum Station {
	STATION_A,
	STATION_B
};

struct Time {
	int hour;
	int minute;
};

bool operator > (const Time& t1, const Time& t2)
{
	if (t1.hour > t2.hour)
		return true;
	else if (t1.hour == t2.hour && t1.minute > t2.minute)
		return true;
	else if (t1.hour == t2.hour && t1.minute == t2.minute)
		return false;
	else
		return false;
}

bool Add_time(Time& time, short minutes)
{
	time.minute += minutes;
	if (time.minute >= 60) {
		time.minute -= 60;
		time.hour += 1;
	}
	if (time.hour >= 24)
		return false;
	else
		return true;
}

struct Trip {
	Time leave_time;
	Time arrive_time;
	Station from_station;
};


// sort in leave_time
void Add_queue(Trip wait_queue[], short& queue_size, const Trip& a_trip)
{
	for (int i = 0; i < queue_size && a_trip.leave_time > wait_queue[i].leave_time ; i++) {
		;
	}
	if (i < queue_size) {
		for (int j = queue_size; j > i; j--) {
			wait_queue[j] = wait_queue[j-1];
		}
	}
	wait_queue[i] = a_trip;
	queue_size++;
}

bool check_if_enough_trains_waiting(Trip queue[], short& queue_size, const Trip& a_trip)
{
	Trip waiting_train;
	bool remove_top(Trip queue[], short& queue_size, Trip& a_trip);

	if (queue_size <= 0)
		return false;
	if (queue[0].leave_time > a_trip.leave_time) {
		return false;		
	} else
		return remove_top(queue, queue_size, waiting_train);
}

bool remove_top(Trip queue[], short& queue_size, Trip& a_trip)
{
	if (queue_size <= 0)
		return false;
	a_trip = queue[0];
	for (int i = 1; i < queue_size; i++) {
		queue[i-1] = queue[i];
	}
	queue_size--;

	return true;
}


short turn_round_time;
short schedule_size;
Trip all_schedule[MAX_N+MAX_N];	// the leave time is the time that there must  one train leave

short num_trains_A;
short queue_size_A;
Trip wait_queue_A[MAX_N];	// the leave_time in this queue is the earliest time that train can leave

short num_trains_B;
short queue_size_B;
Trip wait_queue_B[MAX_N];

bool check_if_time_not_expired(const Trip& current_trip, Trip& new_waiting_trip)
{
	new_waiting_trip.leave_time = current_trip.arrive_time;
	
	return Add_time(new_waiting_trip.leave_time, turn_round_time);
}



void ini_trips()
{
	schedule_size = 0;
	turn_round_time = 0;
	num_trains_A = 0;
	queue_size_A = 0;
	num_trains_B = 0;
	queue_size_B = 0;
}



void do_trains_schedule()
{
	Trip current_trip;
	while (remove_top(all_schedule, schedule_size, current_trip)) {
		Trip new_waiting_trip;
		if (current_trip.from_station == STATION_A) {
			if (check_if_enough_trains_waiting(wait_queue_A, queue_size_A, current_trip)) {
				;
			} else {
				num_trains_A++;// add a new train.
			}

			// add to peer station's waiting list
			if (check_if_time_not_expired(current_trip, new_waiting_trip)) {
				Add_queue(wait_queue_B, queue_size_B, new_waiting_trip);
			} else {
				; // this train died
			}

		} else if (current_trip.from_station == STATION_B) {
			
			if (check_if_enough_trains_waiting(wait_queue_B, queue_size_B, current_trip)) {
				;
			} else {
				num_trains_B++;// add a new train.
			}

			// add to peer station's waiting list
			if (check_if_time_not_expired(current_trip, new_waiting_trip)) {
				Add_queue(wait_queue_A, queue_size_A, new_waiting_trip);
			} else {
				; // this train died
			}

		} else {
			printf("error!!!!\n");
		}
	}
}


void main()
{
	FILE *fin, *fout;
	int num_case = 0;
	int NA, NB;

	fin = fopen("D:\\B-large.in.txt", "r");
	fout = fopen("D:\\B-large.out.txt", "w");

	if (fin == NULL || fout == NULL) {
		fprintf(stderr, "file open error\n");
		exit(-1);
	}

	fscanf(fin, "%d", &num_case);
	for (int i = 1; i <= num_case; i++) {
		ini_trips();

		fscanf(fin, "%d", &turn_round_time);
		
		fscanf(fin, "%d %d", &NA, &NB);

		for (int j = 0; j < NA; j++) {
			Trip temp;
			temp.from_station = STATION_A;
			fscanf(fin, "%d:%d %d:%d", &temp.leave_time.hour, &temp.leave_time.minute,
										&temp.arrive_time.hour, &temp.arrive_time.minute);

			Add_queue(all_schedule, schedule_size, temp);
		}

		for (int k = 0; k < NB; k++) {
			Trip temp;
			temp.from_station = STATION_B;
			fscanf(fin, "%d:%d %d:%d", &temp.leave_time.hour, &temp.leave_time.minute,
										&temp.arrive_time.hour, &temp.arrive_time.minute);
			
			Add_queue(all_schedule, schedule_size, temp);
		}

		do_trains_schedule();

		fprintf(fout, "Case #%d: %d %d\n", i, num_trains_A, num_trains_B);
	}

	fclose(fin);
	fclose(fout);
}