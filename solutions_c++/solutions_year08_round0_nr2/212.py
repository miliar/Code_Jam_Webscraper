#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

ifstream cin("B-large.in");
ofstream cout("B-large.out");

#define SZ(a) ((int)a.size())

#define A 0
#define B 1
#define ADD 0
#define REMOVE 1

struct evnt {
	int time;
	int station;
	int type;
	evnt(int time, int station, int type) {
		this->time = time;
		this->station = station;
		this->type = type;
	}
	friend bool operator < (evnt a, evnt b) {
		return a.time < b.time || a.time == b.time && a.type < b.type;
	}
};

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		vector <evnt> events;
		int ta;
		cin >> ta;
		int na, nb;
		cin >> na >> nb;
		for (int j = 0; j < na; j++) {
			int hour1;
			int min1;
			cin >> hour1;
			cin.ignore();
			cin >> min1;
			int time1 = hour1 * 60 + min1;
			events.push_back(evnt(time1, A, REMOVE));
			int hour2;
			int min2;
			cin >> hour2;
			cin.ignore();
			cin >> min2;
			int time2 = hour2 * 60 + min2;
			events.push_back(evnt(time2 + ta, B, ADD));
		}
		for (int j = 0; j < nb; j++) {
			int hour1;
			int min1;
			cin >> hour1;
			cin.ignore();
			cin >> min1;
			int time1 = hour1 * 60 + min1;
			events.push_back(evnt(time1, B, REMOVE));
			int hour2;
			int min2;
			cin >> hour2;
			cin.ignore();
			cin >> min2;
			int time2 = hour2 * 60 + min2;
			events.push_back(evnt(time2 + ta, A, ADD));
		}
		sort(events.begin(), events.end());
 		vector <int> inital(2);
		vector <int> current(2);
		for (int j = 0; j < SZ(events); j++) {
			int station = events[j].station;
			if (events[j].type == ADD)
				current[station]++;
			else {
				if (current[station] == 0)
					inital[station]++;
				else
					current[station]--;
			}
		}
		cout << "Case #" << (i + 1) << ": " << inital[A] << ' ' << inital[B] << endl;
	}
	return 0;
}