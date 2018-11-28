#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<int, int> Answer;

struct Event {
	enum {
		ARRV_A, ARRV_B, READY_A, READY_B, DEPT_A, DEPT_B,
	};
	int type;
	int time;
	Event(int tp, int tm) : type(tp), time(tm) {}
	bool operator<(const Event& rhs) const {
		if (time != rhs.time) return time < rhs.time;
		return type < rhs.type;
	}
};

typedef vector<Event> evec;

Answer solve(evec events)
{
	sort(events.begin(), events.end());
	Answer ans(0, 0);
	int ta = 0, tb = 0; // # of trains at sta. a, bB
	evec::const_iterator eend = events.end();
	for (evec::const_iterator ei = events.begin(); ei != eend; ++ei) {
		switch (ei->type) {
		case Event::DEPT_A:
			cerr << "DEPT_A" << endl;
			if (ta > 0) --ta;
			else ++ans.first;
			break;
		case Event::DEPT_B:
			cerr << "DEPT_B" << endl;
			if (tb > 0) --tb;
			else ++ans.second;
			break;
		case Event::READY_A:
			cerr << "READY_A" << endl;
			++ta;
			break;
		case Event::READY_B:
			cerr << "READY_B" << endl;
			++tb;
			break;
		}
	}
	return ans;
}

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for (int n = 0; n < N; ++n) {
		int T;
		cin >> T;
		int NA, NB;
		cin >> NA >> NB;
		vector<Event> events;
		char ch;
		int hour, min;
		for (int na = 0; na < NA; ++na) {
			cin >> hour >> ch >> min;
			min = hour * 60 + min;
			events.push_back(Event(Event::DEPT_A, min));
			cin >> hour >> ch >> min;
			min = hour * 60 + min;
			events.push_back(Event(Event::ARRV_B, min));
			events.push_back(Event(Event::READY_B, min + T));
		}
		for (int nb = 0; nb < NB; ++nb) {
			cin >> hour >> ch >> min;
			min = hour * 60 + min;
			events.push_back(Event(Event::DEPT_B, min));
			cin >> hour >> ch >> min;
			min = hour * 60 + min;
			events.push_back(Event(Event::ARRV_A, min));
			events.push_back(Event(Event::READY_A, min + T));
		}

		Answer ans = solve(events);
		cout << "Case #" << (n + 1) << ": " << ans.first << " " << ans.second << endl;
	}
}