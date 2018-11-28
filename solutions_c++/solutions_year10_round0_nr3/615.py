// themepark.cpp --  Sat May 08 2010
#include <stdio.h>
#include <memory.h>
typedef unsigned long long ull;

class ThemePark {
public:
	void read_input() {
		scanf(" %u %u %u", &total_rounds, &coaster_size, &num_groups);
		for(unsigned u = 0; u < num_groups; ++u) scanf(" %u", &g[u]);
	}
	
	ull calc_money() {
		// Reset memos
		memset(last_visit_time, 0, sizeof(last_visit_time));
		memset(next_group, 0, sizeof(next_group));
		memset(span_for_group, 0, sizeof(span_for_group));

		// Begin simulation until we start cycling
		unsigned t = 1;
		unsigned curr_group = 0;
		ull people_served = 0;
		
		for(t = 1; t <= total_rounds; ++t) {
			if(last_visit_time[curr_group] != 0) {
				// This is the T-point of the sigma
				unsigned time_left = total_rounds - t + 1;
				unsigned cycle_time = t - last_visit_time[curr_group];
				ull cycle_span = 0;
				{ // Calc cycle span
					unsigned w = curr_group;
					do { cycle_span += span_for_group[w]; w = next_group[w]; } while(w != curr_group);
				}
				unsigned complete_cycles = time_left/cycle_time;
				people_served += cycle_span * static_cast<ull>(complete_cycles);

				// Simulate the remainder
				for(t += complete_cycles*cycle_time; t <= total_rounds; ++t) {
					people_served += span_for_group[curr_group];
					curr_group = next_group[curr_group];
				}
				
				break;
			} else {
				last_visit_time[curr_group] = t;
				
				// Calc the "span" and the next-starting-group
				unsigned span = g[curr_group];
				unsigned next = (curr_group+1)%num_groups;
				for(; next != curr_group; next = (next+1)%num_groups) {
					unsigned ss = span + g[next];
					if(ss > coaster_size) break;
					span = ss;
				}

				next_group[curr_group] = next;
				span_for_group[curr_group] = span;
				people_served += span;
				curr_group = next;
			}
		}
		
		return people_served;
	}

private:

	unsigned total_rounds /*R*/, coaster_size /*k*/, num_groups /*N*/;
#define MAX_N 1001
	unsigned g[MAX_N];
	unsigned last_visit_time[MAX_N];
	unsigned next_group[MAX_N];
	unsigned span_for_group[MAX_N];
};
	
int main(void) {
	unsigned t; scanf(" %u", &t);
	for(unsigned j = 1; j <= t; ++j) {
		ThemePark tp /* toiletpaper? */;
		tp.read_input();
		printf("Case #%u: %llu\n", j, tp.calc_money());
	}
	return 0;
}

