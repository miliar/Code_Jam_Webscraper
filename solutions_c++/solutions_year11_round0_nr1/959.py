#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>

#define ALL(s) (s).begin(), (s).end()
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define REP(i, a) for (int i = 0; i < a; i++)

#define SZ(x) ((int) (x).size())
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

using namespace std;

typedef pair<char, int> Button;
typedef vector<Button> Sequence;
Sequence s;

void solve() {
	int time = 1;
	int nbuttons = s.size();
	Sequence os = Sequence(nbuttons);
	Sequence bs = Sequence(nbuttons);
	
	int oi = 0, bi = 0;
	REP (i, nbuttons) {
		// separate sequences
		if (s[i].first == 'O') {
			os[oi++] = s[i];
		} else {
			bs[bi++] = s[i];
		}
	}
	
	int opos = 1, bpos = 1;
	int si = 0; oi = 0; bi = 0;
	
	while (si < nbuttons) {
		bool button_was_pressed = false;
	
		// orange robot
		if (opos == os[oi].second) {
			if (s[si].first == 'O' && s[si].second == opos) {
				// press the button
				button_was_pressed = true;
				oi++;
			}
		}
		else if (opos < os[oi].second) {
			opos++;
		}
		else if (opos > os[oi].second) {
			opos--;
		}
		
		// blue robot
		if (bpos == bs[bi].second) {
			if (s[si].first == 'B' && s[si].second == bpos) {
				// press the button
				button_was_pressed = true;
				bi++;
			}
		}
		else if (bpos < bs[bi].second) {
			bpos++;
		}
		else if (bpos > bs[bi].second) {
			bpos--;
		}
		
		// if someone pressed the button, advance sequence
		if (button_was_pressed) {
			si++;
		}
		
		// elapse time
		time++;
	}
	
	printf("%d", time - 1);
}

int main(int argc, char ** argv) {
	int ncases;
	cin >> ncases;

	FOR(t, 1, ncases) {
		printf("Case #%d: ", t);
		
		s = vector<Button>();
		int nbuttons;
		cin >> nbuttons;
		
		s.resize(nbuttons);
		
		REP (i, nbuttons) {
			char robot;
			int pos;
			cin >> robot;
			cin >> pos;
			
			Button b = Button(robot, pos);
			s[i] = b;
		}
		
		solve();
		
		printf("\n");
	}
}
