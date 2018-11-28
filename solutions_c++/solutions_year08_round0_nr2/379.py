/*
FROM: GCJ (Google Code Jam) Qualification Round 2008
PROB: B Train Timetable
KEYW: greedy, heap

LANG: GNU C++ (g++ (GCC) 4.3.1 20080612 (Red Hat 4.3.1-2))
OPT: -lm -O2
*/

#include <cstdio>
#include <algorithm>
#include <queue>
#include <cassert>
#include <functional>

const int MAXN = 1 << 7;

int read_time () {
	int h, m;
	scanf ("%d:%d", &h, &m);
	return h * 60 + m;
}

struct trip_info {
	int dep;
	int arr;
	bool st;
	bool operator < (const trip_info &ti) const {return dep < ti.dep;}
};

int ps;
trip_info pool[MAXN * 2];

int main () {
	int tc;
	scanf ("%d", &tc);

	for (int ctc = 1; ctc <= tc; ++ctc) {
		int t, na, nb;
		scanf ("%d", &t);
		scanf ("%d %d", &na, &nb);
		ps = 0;
		//printf ("init!\n");
		for (int i = 0; i < na + nb; ++i) {
			int dep = read_time ();
			int arr = read_time () + t;
			pool[ps++] = (trip_info) {dep, arr, i >= na};
		}
		//printf ("read!\n");
		std::sort (pool, pool + ps);
		//printf ("sorted!\n");
		assert (ps == na + nb);

		std::priority_queue <int, std::vector <int>, std::greater <int> > w[2];
		int s[2] = {0};//the answer

		for (int i = 0; i < ps; ++i) {
			//printf ("--%d\n", i);
			if (!w[pool[i].st].empty ()
			 && pool[i].dep >= w[pool[i].st].top ()) {
				w[pool[i].st].pop ();
			} else {
				++s[pool[i].st];
			}
			w[1-pool[i].st].push (pool[i].arr);
		}
		printf ("Case #%d: %d %d\n", ctc, s[0], s[1]);
	}

	return 0;
}
