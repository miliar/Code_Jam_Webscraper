#include <iostream>
#include <fstream>
#include <list>
using namespace std;

class p_queue {
	public:
	list<int> impl;

	p_queue() {}

	void insert(int t) {
		impl.insert(impl.begin(), t);
		impl.sort();
	}

	bool empty() {
		return impl.empty();
	}

	int front() {
		return impl.front();
	}

	void pop_front() {
		impl.pop_front();
	}
};

class trip {
	public:
	trip(int dir, int dep, int arr) :
		direction(dir), departure(dep), arrival(arr) {}

	int direction;
	int departure;
	int arrival;
};

bool operator<(const trip& t1, const trip& t2) {
	return t1.departure < t2.departure;
}

int get_time(ifstream& infile) {
	int hours;
	infile >> hours;
	infile.ignore();
	int minutes;
	infile >> minutes;
	cerr << hours*60+minutes << endl;
	return hours*60 + minutes;
}

int main(int argc, char** argv) {
	ifstream infile(argv[1]);

	int num_cases;
	infile >> num_cases;

	for(int i = 0; i < num_cases; i++) {
		cout << "Case #" << i+1 << ": ";

		int turn_time;
		infile >> turn_time;

		list<trip> trips;

		int AtoB, BtoA;
		infile >> AtoB >> BtoA;

		for(int j = 0; j < AtoB; j++) {
			int dep = get_time(infile);
			int arr = get_time(infile);
			trip new_trip(0, dep, arr);
			trips.push_back(new_trip);
		}
		for(int j = 0; j < BtoA; j++) {
			int dep = get_time(infile);
			int arr = get_time(infile);
			trip new_trip(1,dep,arr);
			trips.push_back(new_trip);
		}
		trips.sort();

		//p_queue A;
		//p_queue B;
		p_queue q[2];
		int init[2];
		init[0] = init[1] = 0;

		int t = 0;
		while(!trips.empty()) {
			trip cur_trip = trips.front();
			trips.pop_front();

			t = cur_trip.departure;
			cerr << "t: " << t << ", going from " << ((cur_trip.direction == 0) ? "a" : "b") << endl;

			if(!q[cur_trip.direction].empty() && q[cur_trip.direction].front() <= t) {
				cerr << "train was ready at " << q[cur_trip.direction].front() << endl;
				q[cur_trip.direction].pop_front();
				q[1-cur_trip.direction].insert(cur_trip.arrival + turn_time);
			} else {
				cerr << "train not ready" << endl;
				init[cur_trip.direction]++;
				q[1-cur_trip.direction].insert(cur_trip.arrival + turn_time);
			}
		}
		cout << init[0] << " " << init[1] << endl;
	}

	return 0;
}
