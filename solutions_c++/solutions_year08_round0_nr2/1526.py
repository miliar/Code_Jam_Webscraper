#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef pair<int, int> Time;

bool operator < (const Time &t1, const Time &t2) {
	if (t1.first != t2.first) return t1.first < t2.first;
	return t1.second < t2.second;
}

struct Journey {
	Time departure, arrival;
};

istream& operator >> (istream &in, Journey &j) {
	char s[10];
	in >> s;
	j.departure.first = (s[0] - '0') * 10 + (s[1] - '0');
	j.departure.second = (s[3] - '0') * 10 + (s[4] - '0');

	in >> s;
	j.arrival.first = (s[0] - '0') * 10 + (s[1] - '0');
	j.arrival.second = (s[3] - '0') * 10 + (s[4] - '0');
	return in;
}

struct ArrivalComparer {
	bool operator () (const Journey &j1, const Journey &j2) {
		return j1.arrival < j2.arrival;
	}
};

struct DepartureComparer {
	bool operator () (const Journey &j1, const Journey &j2) {
		return j1.departure < j2.departure;
	}
};

void AddMinutes(Time &t, int mins) {
	t.second += mins;
	t.first += t.second / 60;
	t.second = t.second % 60;
}

int main() {
	int N;
	cin >> N;

	for (int caseNumber = 1; caseNumber <= N; ++caseNumber) {
		int T, NA, NB;
		cin >> T;
		cin >> NA >> NB;

		vector<Journey> va1(NA), va2(NA), vb1(NB), vb2(NB);
		for (int i = 0; i < NA; ++i) {
			cin >> va1[i];
			AddMinutes(va1[i].arrival, T);
			va2[i] = va1[i];
		}
		for (int i = 0; i < NB; ++i) {
			cin >> vb1[i];
			AddMinutes(vb1[i].arrival, T);
			vb2[i] = vb1[i];
		}

		sort(va1.begin(), va1.end(), DepartureComparer());
		sort(va2.begin(), va2.end(), ArrivalComparer());
		sort(vb1.begin(), vb1.end(), DepartureComparer());
		sort(vb2.begin(), vb2.end(), ArrivalComparer());

		while (vb2.size() && va1.size()) {
			if (vb2.back().arrival <= va1.back().departure)
				va1.pop_back();
			vb2.pop_back();
		}
		while (va2.size() && vb1.size()) {
			if (va2.back().arrival <= vb1.back().departure)
				vb1.pop_back();
			va2.pop_back();
		}

		cout << "Case #" << caseNumber << ": " << va1.size() << ' ' << vb1.size() << endl;
	}
}
