#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Event 
{
	int time; // in minutes
	enum Kind { ToA, ToB, FromA, FromB } kind;
	friend bool operator<(const Event& lhs, const Event& rhs) { 
		if (lhs.time < rhs.time) return true;
		if (lhs.time > rhs.time) return false;
		if ((unsigned)(lhs.kind) < (unsigned)(rhs.kind)) return true;
		return false;
	}
	Event(int time, Kind kind) : time(time), kind(kind) { }
};

int main() 
{
	int N;
	cin >> N;

	for (int X=1; X<=N; ++X) {
		int T, NA, NB;
		vector<Event> t;
		cin >> T >> NA >> NB >> ws;
		for (int i=0; i<NA; ++i) {
			int hfrom, mfrom, hto, mto; char c;
			cin >> hfrom >> c >> mfrom >> hto >> c >> mto;
			t.push_back(Event(hfrom * 60 + mfrom, Event::FromA));
			t.push_back(Event(hto * 60 + mto + T, Event::ToB));
		}
		for (int i=0; i<NB; ++i) {
			int hfrom, mfrom, hto, mto; char c;
			cin >> hfrom >> c >> mfrom >> hto >> c >> mto;
			t.push_back(Event(hfrom * 60 + mfrom, Event::FromB));
			t.push_back(Event(hto * 60 + mto + T, Event::ToA));
		}

		sort(t.begin(), t.end());
		int na = 0, nb = 0, mina = 0, minb = 0, posa = 0, posb = 0;

		for (int i=0; i<t.size(); ++i) {
			Event e = t[i];
			if (e.kind == Event::FromA) {
				if (na == 0) { ++na; ++mina; }
				--na;
			} else if (e.kind == Event::FromB) {
				if (nb == 0) { ++nb; ++minb; }
				--nb;
			} else if (e.kind == Event::ToA) {
				++na;
			} else if (e.kind == Event::ToB) {
				++nb;
			}
		}

		cout << "Case #" << X << ": " << mina << " " << minb << endl;
	}

	return 0;
}
