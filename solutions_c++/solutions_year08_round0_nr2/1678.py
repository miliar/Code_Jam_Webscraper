#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <vector>
#include <stdio.h>


using namespace std;

int s2i(string s) {
	istringstream iss(s);
	int i;
	iss >> i;
	return i;
} 

struct Route {
	bool ab;
	int departure;
	int arrival;
	Route(bool _ab, int _d, int _a) : ab(_ab), departure(_d), arrival(_a) {}
};

struct Train {
	bool ab;
	int arrival;
	Train(bool _ab, int _ar): ab(_ab), arrival(_ar) {}
};

bool compare_times(Route first, Route second) {
	if (first.departure > second.departure)
		return false;	

	return true;
}


int main() {
	string s;
	list<Route> timetable;
	vector<Train> trains;

	//num cases
	getline(cin, s);
	int n = s2i(s);
		
	for (int c = 0; c < n; c++) {
		int dmin, amin;
		int abcount = 0, bacount = 0;
		timetable.clear();
		trains.clear();
		//turnaround
		getline(cin, s);
		int turnaround = s2i(s);

		//num ab ba
		getline(cin, s);
		int ab, ba;
		sscanf(s.c_str(), "%d %d", &ab, &ba);

		for (int i = 0; i < ab; i++) {
			getline(cin, s);
			int d[2], a[2];
			sscanf(s.c_str(), "%d:%d %d:%d", &d[0], &d[1], &a[0], &a[1]);
			dmin = d[0] * 60 + d[1];
			amin = a[0] * 60 + a[1] + turnaround;
			timetable.push_back(Route(true, dmin, amin));
		}

		for (int i = 0; i < ba; i++) {
			getline(cin, s);
			int d[2], a[2];
			sscanf(s.c_str(), "%d:%d %d:%d", &d[0], &d[1], &a[0], &a[1]);
			dmin = d[0] * 60 + d[1];
			amin = a[0] * 60 + a[1] + turnaround;
			timetable.push_back(Route(false, dmin, amin));
		}

		timetable.sort(compare_times);
		for (list<Route>::iterator it = timetable.begin(); it != timetable.end(); it++) {
			bool skip = false;

			for (int i = 0; i < trains.size(); i++) {
				if (trains[i].arrival <= it->departure && trains[i].ab == !it->ab) {
					trains[i].arrival = it->arrival;
					trains[i].ab = it->ab;
					skip = true;
					break;
				}
			}

			if (skip)
				continue;


			it->ab ? abcount++ : bacount++;
			trains.push_back(Train(it->ab, it->arrival));			
		}

		cout << "Case #" << (c + 1) << ": " << abcount << " " << bacount << endl;
	}

	return 0;
}
