#include <iostream>
#include <sstream>
#include <algorithm>
#include <list>
using namespace std;


enum stationT {
	A, B
};

struct tripT {
	unsigned start;
	unsigned end;
	stationT station;
};

unsigned getUnsigned(string number) {
	stringstream converter;
	converter << number;
	unsigned result;
	converter >> result;
	return result;
}

unsigned getUnsigned() {
	string number;
	cin >> number;
	return getUnsigned(number);
}

unsigned getTime(string time) {
	int split = time.find(':');
	return getUnsigned(time.substr(0, split)) * 60 +
		   getUnsigned(time.substr(split + 1));
	
}

tripT getTrip(stationT station, unsigned turnaround) {
	pair<string, string> line;
	cin >> line.first >> line.second;
	tripT trip = {getTime(line.first), getTime(line.second) + turnaround, station};
	return trip;
}

bool tripCmp(const tripT &one, const tripT &two) {
	return one.start < two.start;
}

void minTrains(list<tripT> & schedule, int & a, int & b) {
	a = 0;
	b = 0;
	
	schedule.sort(tripCmp);
	while (!schedule.empty()) {
		tripT trip = schedule.front();
		schedule.pop_front();
		if (trip.station == A) {
			a++;
		} else {
			b++;
		}
		unsigned time = trip.end;
		for (list<tripT>::iterator it = schedule.begin(); it != schedule.end(); ++it) {
			if (it->station != trip.station && it->start >= time) {
				trip = *it;
				time = trip.end;
				it = schedule.erase(it);
				--it;
			}
		}
	}
	
}

int main() {
	unsigned nCases = getUnsigned();
	for (unsigned n = 1; n <= nCases; n++) {
		unsigned turnaround = getUnsigned();
		unsigned nA = getUnsigned();
		unsigned nB = getUnsigned();
		
		list<tripT> schedule;
		for (unsigned i = 0; i < nA; i++) {
			schedule.push_back(getTrip(A, turnaround));
		}
		for (unsigned i = 0; i < nB; i++) {
			schedule.push_back(getTrip(B, turnaround));
		}
		
		int a, b;
		minTrains(schedule, a, b);
		cout << "Case #" << n << ": " << a << " " << b << endl;
	}
	
	return 0;
}

