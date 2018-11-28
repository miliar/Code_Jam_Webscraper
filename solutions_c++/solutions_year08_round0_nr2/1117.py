/* 
 * Google CodeJam
 * Problem B. Running Trains On Time
 *
 */

#include<iostream>
#include<fstream>
#include<string>
#include<cassert>

#include<sstream>
#include<vector>
#include<algorithm>

using namespace std;


/*-----------------------------------------------------------------*/
// Event related structures.
enum EventType {DEPARTURE, ARRIVAL};

class Event {

	private:
		/* Event occurance time. 
		 * Could be float because of turnaround time. */
		float time; 
		EventType type;

	public:
		/* Time and Type must be specified. */
		Event(float time, EventType type) { 

			assert((0.0 <= time) && (time < 1440.0));
			this->time = time; 
			this->type = type;
		}

		/* Getters. */
		float get_time() { return time; }
		EventType get_event_type() { return type; }

		~Event() { }

		void print(void)
		{
			if(type == DEPARTURE)
				cout <<"DEPARTURE " << time << endl;
			else if(type == ARRIVAL)
				cout <<"ARRIVAL   " << time << endl;
		}

};

typedef vector<Event*> EventContainer;
typedef vector<Event*>::iterator EventIterator;

struct EventCmp: public binary_function<Event*, Event*, bool> 
{
	bool operator()(Event * left, Event * right) 
	{ 
		return left->get_time() < right->get_time(); 
	}
};

/*-----------------------------------------------------------------*/

class Station {

	private:
		/* timeline is set of events at the station. */
		EventContainer timeline;

		int start_train_count; /* At the start of the day. */
		int curr_train_count;

	public:
		Station() {
			/* Important init. */
			start_train_count = 0;
			curr_train_count = 0;
		}
		~Station() {
			cout << "Release timeline. " << endl;
			EventIterator iter = timeline.begin();
			for(; iter != timeline.end(); iter++) {
				delete(*iter);	
				(*iter) = NULL;
			}
		}

		void add_event(Event * event) {
			assert(event != NULL);
			timeline.push_back(event);
		}

		/* Important: */
		void sort_timeline() {
			sort(timeline.begin(), timeline.end(), EventCmp());
		}

		/* Debug timeline. */
		void print_timeline() {

			cout << endl << "# Station timeline " << endl;

			EventIterator iter = timeline.begin();
			for(; iter != timeline.end(); iter++)
				(*iter)->print();	
			cout << "TOTAL EVENTS = " << timeline.size() << endl;
		}

		/* Core logic. Simulate events at the station.
		 * Returns number of trains required at the start. */
		int simulate()
		{
			/* Visit all events in time chronological manner. */
			EventIterator iter = timeline.begin();
			for(; iter != timeline.end(); iter++)
			{
				if((*iter)->get_event_type() == ARRIVAL)
					curr_train_count++;

				else if((*iter)->get_event_type() == DEPARTURE)
				{
					/* There is depature, but no train, so 
					 * we need a train at the start of the day. */
					if(curr_train_count == 0)
						start_train_count++;
					else 
						curr_train_count--;
				}
			}

			return start_train_count;
		}
};

/*-----------------------------------------------------------------*/

/* Function declarations. */
float string_to_float(string str);
int string_to_int(string str);
int hhmm_to_mins(string hhmm_time);

/*-----------------------------------------------------------------*/
int main(int argc, char * argv[])
{
	if(argc != 3) {
		cerr << "Incorrect number of argument to " << argv[0] << endl;
		exit(-1);
	}

	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	int N; // No of test cases. 

	/* Read first line. No of test cases. */
	fin >> N;

	/* For each test case. */
	for(int tc_count = 1; tc_count <= N; tc_count++)
	{
		float ta_time = 0.0;
		int NA = 0;	// Number of trips from A to B
		int NB = 0;	// Number of trips from B to A
		Station A, B;

		fin >> ta_time;
		fin >> NA >> NB;
		cout << "NA = "<< NA <<", NB = " << NB << ", total = "<<(NA+NB)<<endl;
		cout << "Turnaround time = " << ta_time <<" mins."<< endl;

		/* DEPARTURE from A. ARRIVAL at B. */
		for(int trip_count = 1; trip_count <= NA; trip_count++)
		{
			string dep_time, arr_time;
			Event * event = NULL;
			float time = 0.0;

			fin >> dep_time >> arr_time;

			/* Create DEPARTURE event object. */
			time = hhmm_to_mins(dep_time);
			event = new Event(time, DEPARTURE);
			A.add_event(event);

			/* Create ARRIVAL event objec. Consider turnaround time.*/
			time = hhmm_to_mins(arr_time) + ta_time - 0.01;

			if(time < 1440.0) {
				event = new Event(time, ARRIVAL);
				B.add_event(event);
			}
		}

		/* DEPARTURE from B. ARRIVAL at A. */
		for(int trip_count = 1; trip_count <= NB; trip_count++)
		{
			string dep_time, arr_time;
			Event * event = NULL;
			float time = 0.0;

			fin >> dep_time >> arr_time;

			/* Create DEPARTURE event object. */
			time = hhmm_to_mins(dep_time);
			event = new Event(time, DEPARTURE);
			B.add_event(event);

			/* Create ARRIVAL event objec. Consider turnaround time.*/
			time = hhmm_to_mins(arr_time) + ta_time - 0.01;

			if(time < 1440.0) {
				event = new Event(time, ARRIVAL);
				A.add_event(event);
			}
		}

		A.sort_timeline();
		B.sort_timeline();
		A.print_timeline();
		B.print_timeline();

		fout<<"Case #"<<tc_count<<": ";
		fout<< A.simulate() <<" "<< B.simulate() << endl;
		cout<<"-------------------------------------------"<<endl;

	} // Next test case.

	return 0;
}


/* Utility: Convert string to integer. */
int string_to_int(string str)
{
	stringstream sin(str);
	int int_value;

	sin >> int_value;

	return int_value;
}

/* Utility: Convert string to float. */
float string_to_float(string str)
{
	stringstream sin(str);
	float flt_value;

	sin >> flt_value;

	return flt_value;
}


/* Convert HH:MM string to mins between 0-1439. 
 * Example:
 * 01:00 -> 60
 * 12:00 -> 720
 * 10:40 -> 640
 * */

int hhmm_to_mins(string hhmm_time)
{
	int pos = hhmm_time.find(':');

	string hrs(hhmm_time.begin(), hhmm_time.begin() + pos);
	string mins(hhmm_time.begin() + pos + 1, hhmm_time.end());

	int int_hrs = string_to_int(hrs);
	int int_mins = string_to_int(mins);

	assert(int_hrs < 24); /* 24 hrs. */
	assert(int_mins < 60); /* 60 mins. */

	int mins_time = int_hrs * 60 + int_mins;
	assert(mins_time >= 0 && mins_time < 1440);

	return mins_time;
}

