#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int ARRIVE = 0;
const int DEP = 1;
const int A = 2;
const int B = 3;

#define MINUTE(x) ((x)-('0'))

struct event {
	int time;
	int type;
	int station;

	event(string a, int offset, int _type, int _station) : type(_type), station(_station) {
		time = MINUTE(a[0])*600 + MINUTE(a[1])*60 +
			MINUTE(a[3])*10 + MINUTE(a[4]) + offset;
	}
};

int operator<(const event &a, const event &b) {
	if (a.time == b.time)
		return a.type < b.type;
	else
		return a.time < b.time;
}

vector<event> events;
int caseno = 1;

void solve() {
	int stockA = 0, stockB = 0;
	int needA = 0, needB = 0;

	for (int i = 0; i < events.size(); i++) {
		event e = events[i];

		if (e.type == ARRIVE) {
			if (e.station == A)
				stockA++;
			else
				stockB++;
		}
		else {
			if (e.station == A) {
				if (stockA == 0)
					needA++;
				else
					stockA--;
			}
			else {
				if (stockB == 0)
					needB++;
				else
					stockB--;
			}
		}
	}

	cout << "Case #" << caseno++ << ": " << needA << " " << needB << endl; 
}

int main() {
	int n, T, fromA, fromB;
	string str;

	cin >> n;
	while (n--) {
		events.clear();
		cin >> T >> fromA >> fromB;

		while (fromA--) {
			cin >> str;
			events.push_back(event(str, 0, DEP, A));
			cin >> str;
			events.push_back(event(str, T, ARRIVE, B));
		}

		while (fromB--) {
			cin >> str;
			events.push_back(event(str, 0, DEP, B));
			cin >> str;
			events.push_back(event(str, T, ARRIVE, A));
		}

		sort(events.begin(), events.end());

		solve();
       }
}

