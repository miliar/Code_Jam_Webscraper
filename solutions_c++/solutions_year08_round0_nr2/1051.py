#define  _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <stdlib.h>
#include <bitset>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

#define MAX_TRAINS 100
#define MINUTES_IN_DAY (60*24)
#define ORIG 1

struct TrainRec {
	unsigned start, end;
	bool exec;
};

struct start_t_compare_p {
	bool operator()(const TrainRec& lhs, const TrainRec& rhs) {
#if ORIG
		return lhs.start < rhs.start;
#else
		return lhs.end < rhs.end;
#endif
	}
};

class Timetable {
	unsigned turnaround_t;
	unsigned n[2];
	static TrainRec t[2][MAX_TRAINS];
	unsigned read_time() {
		unsigned hh, mm;
		scanf(" %u:%u", &hh, &mm);
		return hh*60+mm;
	}
	void read_tt(unsigned u) {
		for(unsigned j = 0; j < n[u]; ++j) {
			t[u][j].start = read_time();
			t[u][j].end = read_time();
			t[u][j].exec = false;
		}
		sort(t[u], t[u] + n[u], start_t_compare_p());
	}
public:
	Timetable() {
		scanf(" %u %u %u", &turnaround_t, &n[0], &n[1]);
		read_tt(0);
		read_tt(1);
	}

	void get_min_trains() {
		unsigned next[2] = {0, 0};
		unsigned p[2];
		unsigned num_execed[2] = {0, 0};
		unsigned u;
		unsigned num_trains[2] = {0, 0};
		unsigned next_time;
		while(num_execed[0] < n[0] && num_execed[1] < n[1]) {
			// Invariant: n[0] ... next[0]-1 trains have been executed etc.
			// In all, num_execed[j] beginning from station j have been executed
			// Find the next train we must exec
			while(t[0][next[0]].exec) ++next[0];
			while(t[1][next[1]].exec) ++next[1];
#if ORIG
			u = t[0][next[0]].start <= t[1][next[1]].start ? 0 : 1;
#else
			u = t[0][next[0]].end <= t[1][next[1]].end ? 0 : 1;
#endif
			++num_trains[u];
			
			// Exec the t[next[u]] train and follow its consequence
			p[0] = next[0], p[1] = next[1];
			for(bool found = true; found; ) {
				t[u][p[u]].exec = true; ++num_execed[u];
				next_time = t[u][p[u]].end + turnaround_t;
				++p[u];
				// Find a train leaving from station 1-u at time >= next_time
				// that we've not already executed
				unsigned v = 1 - u;
				found = false;
				for(; p[v] < n[v]; ++p[v]) {
					if(t[v][p[v]].start >= next_time && !t[v][p[v]].exec) {
						found = true;
						break;
					}
				}
				u = v;
			}
		}
		printf("%u %u\n"
			, num_trains[0] + (n[0] - num_execed[0])
			, num_trains[1] + (n[1] - num_execed[1]));
	}
};

TrainRec Timetable::t[2][MAX_TRAINS];

int main(int argc, char* argv[]) {
	unsigned num_tests;
	scanf(" %u", &num_tests);
	for(unsigned j = 0; j < num_tests; ++j) {
		Timetable TT;
		printf("Case #%u: ", j + 1);
		TT.get_min_trains();
	}
	return 0;
}

