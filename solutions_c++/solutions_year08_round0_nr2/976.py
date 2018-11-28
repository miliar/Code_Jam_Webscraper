#include <algorithm>
#include <iostream>

using namespace std;

#define MAXE 1000

struct Tschd {
	bool fromA, dep;
	int tm;
};

struct comp {
	bool operator ()(const Tschd &a, const Tschd &b) {
		if (a.tm != b.tm) return a.tm < b.tm;
			else return a.dep < b.dep;
	}
};

Tschd events[MAXE];
int kel, na, nb, n, t;

void read() {
	scanf(" %d %d %d", &t, &na, &nb);
	int dh, dm, ah, am;
	kel = 0;
	for (int i = 0; i < na + nb; i++) {
		scanf("%2d:%2d %2d:%2d\n", &dh, &dm, &ah, &am);
		events[kel + 1].tm = ah * 60 + am + t;
		events[kel].tm = dh * 60 + dm;
		events[kel + 1].fromA = events[kel].fromA = i < na;
		events[kel + 1].dep = false;
		events[kel].dep = true;
		kel += 2;
	}
}

void solve(int tst) {
	int costa = 0, costb = 0,  tra = 0, trb = 0;
	for (int x = 0; x < kel; x++)
		if (!events[x].dep) {
			if (events[x].fromA) trb++;
				else tra++;
		}
			else {
				if (events[x].fromA) {
					if (tra > 0) tra--;
						else costa++;
				}
					else {
						if (trb > 0) trb--;
							else costb++;
					}
			}
	printf("Case #%d: %d %d\n", tst, costa, costb);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf(" %d", &n);
	for (int t = 1; t <= n; t++) {
		read();
 		sort(events, events + kel, comp());
		solve(t);
	}
	return 0;
}
