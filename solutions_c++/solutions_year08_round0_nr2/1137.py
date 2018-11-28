
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>
#include <list>

using namespace std;

struct Time {

	// fields
	int hour;
	int min;

	// default constructor
	Time() {
		hour = 99;
		min = 99;
	}

	// add time
	Time operator+(Time t) {
		t.min += min;
		t.hour += hour + (t.min / 60);
		t.min = t.min % 60;
		return t;
	}

	// add time
	Time operator+(int mins) {
		Time t = *this;
		t.min += mins;
		t.hour += (t.min / 60);
		t.min = t.min % 60;
		return t;
	}

	bool operator<=(Time const & t) {
		return hour < t.hour || (hour == t.hour && min < t.min) || (hour == t.hour && min == t.min);
	}
};

ostream& operator<<(ostream& stream, Time& t) {
	stream << t.hour << ":" << t.min;
	return stream;
}

void readTimes(string str, Time& t1, Time& t2) {
	stringstream ss(str);
	ss >> t1.hour;
	char c;
	ss >> c;
	ss >> t1.min;
	ss >> t2.hour;
	ss >> c;
	ss >> t2.min;
}

struct Ride {
	bool A;
	Time start;
	Time stop;
};


// plan a route
bool planRoute(list<Ride> & rides) {

	// find the first ride
	Time minTime;
	list<Ride>::iterator first = rides.end();
	for (list<Ride>::iterator it = rides.begin(); it != rides.end(); ++it) {
		if (first == rides.end() || (*it).start <= (*first).start) {
			first = it;
		}
	}

	// remove this ride from the list, it is our starting point
	Ride current = (*first);
	//cout << "Starting with train at " << current.A << " from " << current.start << " to " << current.stop << endl;
	bool A = current.A;
	rides.erase(first);

	// now find the first ride with the same train
	while (true) {

		list<Ride>::iterator next = rides.end();
		for (list<Ride>::iterator it = rides.begin(); it != rides.end(); ++it) {

			// candidate
			if (current.A != (*it).A && current.stop <= (*it).start) {

				// best candidate
				if (next == rides.end() || (*it).start <= (*next).start) {
					next = it;
				}
			}
		}

		// no candidate found, break up
		if (next == rides.end()) break;

		// candidate found, proceed
		current = (*next);
		//cout << "Proceeding with train at " << current.A << " from " << current.start << " to " << current.stop << endl;
		rides.erase(next);
	}

	return A;
}



// find train count for one case
void findTrains(ifstream& in, int& ATrains, int& BTrains) {

	string str;
	getline(in, str);

	// get the turnaround time
	int turnAround = atoi(str.c_str());

	// get the number of trips in either direction
	getline(in, str);
	stringstream ss(str);
	int nA, nB;
	ss >> nA >> nB;

	// initialize time table arrays
	list<Ride> rides;

	// initialize "already taken" arrays
	bool* ATaken = new bool[nA];
	bool* BTaken = new bool[nB];

	// read them in
	string timestr;
	Time mintime;
	Ride ride;
	for (int i = 0; i < nA; ++i) {
		ride.A = true;
		getline(in, str);
		readTimes(str, ride.start, ride.stop);
		ride.stop = ride.stop + turnAround;
		rides.push_back(ride);
	}
	for (int i = 0; i < nB; ++i) {
		ride.A = false;
		getline(in, str);
		readTimes(str, ride.start, ride.stop);
		ride.stop = ride.stop + turnAround;
		rides.push_back(ride);
	}

	// now start scheduling, starting with the earliest train
	ATrains = 0;
	BTrains = 0;
	while (rides.size() > 0) {
		bool A = planRoute(rides);
		//cout << "Planned a route starting at " << A << endl;
		if (A)
			++ATrains;
		else
			++BTrains;
	}
}



int main(int argc, char **argv) {

	// load file
	ifstream stream("B-large.in");

	// open write file
	ofstream out("output.txt");

	// read lines from file
	string str;
	getline(stream, str);

	// get the number of cases
	int nCases = atoi(str.c_str());

	// for each case
	int ATrains, BTrains;
	for (int i = 0; i < nCases; ++i) {
		findTrains(stream, ATrains, BTrains);
		out << "Case #" << (i+1) << ": " << ATrains << " " << BTrains << endl;
		cout << "Case #" << (i+1) << ": " << ATrains << " " << BTrains << endl;
	}
	return 0;
};
