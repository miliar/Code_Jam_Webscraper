#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define all(v) v.begin(), v.end()

using namespace std;

struct event {
	int a, b;
	int typ;

	event(int a, int b, int typ): a(a), b(b), typ(typ) {
	}
};

bool operator < (const event& e1, const event& e2) {
	if (e1.b != e2.b) return e1.b < e2.b;
	if (e1.a != e2.a) return e1.a > e2.a;
	if (e1.typ != e2.typ) return e1.typ < e2.typ;
	return false;
}

int read_time() {
	int hh, mm;
	scanf("%d:%d", &hh, &mm);
	return mm + hh * 60;
}

void solve(int tst) {
	int t;
	scanf("%d", &t);		
	int na, nb;
	scanf("%d%d", &na, &nb);

	vector<event> e;
	forn (i, na) {
		int a = read_time();
		int b = read_time();
		e.pb(event(a, b, 1));						
	}	

	forn (i, nb) {
		int a = read_time();
		int b = read_time();
		e.pb(event(a, b, 2));						
	}	

	sort(all(e));

	vector<int> atA, atB;

	int ansA = 0, ansB = 0;

	forn (i, e.size()) {
		int st = e[i].a;
		int fin = e[i].b;		

		int typ = e[i].typ;

		if (typ == 1) {
			int best = -1;
			forn (i, atA.size())
				if (atA[i] <= st) {
					if (best == -1) best = i;
					if (atA[i] > atA[best]) best = i;
				}
			if (best == -1) {
				best = atA.size();
				atA.pb(st);
				++ansA;
			}
			atB.pb(fin + t);
			atA.erase(atA.begin() + best, atA.begin() + best + 1);			
		} else {
			int best = -1;
			forn (i, atB.size())
				if (atB[i] <= st) {
					if (best == -1) best = i;
					if (atB[i] > atB[best]) best = i;
				}
			if (best == -1) {
				best = atB.size();
				atB.pb(st);
				++ansB;
			}
			atA.pb(fin + t);
			atB.erase(atB.begin() + best, atB.begin() + best + 1);			
		}	
	}

	printf("Case #%d: %d %d\n", tst, ansA, ansB);
}

int main() {

	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

	int tst;
	scanf("%d", &tst);

	forn (i, tst) solve(i + 1);

	return 0;
}