#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_GROUP 1024

int group_size[MAX_GROUP];

// index is group id $gid;
// n_people_in_same_round[$gid] stores the number of people playing on coaster when group $gid is the first group to go on the coaster
long long int n_people_in_same_round[MAX_GROUP]; 

// index is round number $r;
// cumulative[$r] stores cumulative number of people played on coaster, from round 0 to round $r
long long int cumulative[MAX_GROUP]; 

// index is group id $gid;
// next_group[$gid] stores the group id in next round when group $gid is the first group to go on the coaster
short next_group[MAX_GROUP];

// index is group id $gid;
// first_occurrence[$gid] stores the round number when group $gid is the first group to go on the coaster
short first_occurrence[MAX_GROUP];

char hit[MAX_GROUP], TRUE;

//#define DEBUG 1

int main()
{
	//puts ("1");
	//puts ("100000000 1000000000 1000");
	//printf ("10000000");
	//for (int i=1; i<1000; ++i)
	//	printf (" 10000000");
	//puts ("");
	//return 0;

	int serial=1, kase,
		n_round, n_seat, n_group,
		group_on_coaster,
		gid, r, next,
		cycle_start_at_round, cycle_start_gid, cycle_length, n_cycle;
	long long int people_on_coaster, soln, cum,
		n_people_in_cycle;
	int *ptr;
	bool no_cycle_today;

	scanf ("%d", &kase);
	while (kase--)
	{
		// BEGIN test case

		if (++TRUE == 100) {
			memset (hit, 0, sizeof (hit));
			TRUE = 0;
		}

		scanf ("%d %d %d", &n_round, &n_seat, &n_group);
		for (int i=0; i<n_group; ++i) {
			scanf ("%d", group_size+i);
		}

		next_group[0] = 0;
		people_on_coaster = group_size[0];
		group_on_coaster = 1;

		ptr = group_size + 1;
		for (int i=1; i<n_group; ++i, ++ptr) {
			++group_on_coaster;

			if ((people_on_coaster += *ptr) > n_seat) {
				people_on_coaster -= *ptr;
				--group_on_coaster;
				next_group[0] = i;
				break;
			}
		}

		n_people_in_same_round[0] = people_on_coaster;

		for (int i=1; i<n_group; ++i) {
			people_on_coaster -= group_size[i-1];
			--group_on_coaster;
			next = next_group[i-1];
			while (group_on_coaster < n_group && people_on_coaster + group_size[next] <= n_seat) {
				++group_on_coaster;
				people_on_coaster += group_size[next];
				if (++next >= n_group) {
					next = 0;
				}
			}

			n_people_in_same_round[i] = people_on_coaster;
			next_group[i] = next;
		}

#ifdef DEBUG
		puts ("");
		printf ("Case #%d\n", serial);
		for (int i=0; i<n_group; ++i) {
			printf ("Group %2d: %10lld %10d\n", i, n_people_in_same_round[i], next_group[i]);
			if (n_people_in_same_round[i] > n_seat) {
				printf("Error 2, %lld > %d fails\n", n_people_in_same_round[i], n_seat);
			}
		}
#endif

		// Found if there is cycle
		gid = 0; // group id
		r = 0; // current round number
		cum = 0;

		no_cycle_today = false;

#ifdef DEBUG
		printf ("Sequence:");
#endif

		do {
#ifdef DEBUG
			printf (" %d", gid);
#endif
			hit [gid] = TRUE;
			first_occurrence[gid] = r;
			cum += n_people_in_same_round[gid];
			cumulative[r] = cum;

			// Advance to next round
			if (++r >= n_round) {
				no_cycle_today = true;
				break;
			}

			gid = next_group[gid];
			if (hit [gid] == TRUE) { // cycle found
#ifdef DEBUG
				printf (" %d[cycle detected]", gid);
#endif;
				cycle_start_at_round = first_occurrence[gid];
				cycle_start_gid = gid;
				cycle_length = r - cycle_start_at_round;
				if (cycle_start_at_round == 0) {
					n_people_in_cycle = cumulative[r-1];
				}
				else {
					n_people_in_cycle = cumulative[r-1] - cumulative[cycle_start_at_round-1];
				}
				break;
			}
		}
		while (true);

#ifdef DEBUG
			puts ("");
#endif

		if (no_cycle_today) {
#ifdef DEBUG
			puts ("No cycle");
#endif
			soln = cumulative[n_round-1];
		}
		else {
#ifdef DEBUG
			printf ("cycle length = %d, start at round %d, group %d; n_people_in_cycle %d\n", cycle_length, cycle_start_at_round, cycle_start_gid, n_people_in_cycle);
#endif
			if (cycle_start_at_round == 0) {
				soln = 0;
			}
			else {
				soln = cumulative[cycle_start_at_round-1];
				n_round -= cycle_start_at_round;
			}

			n_cycle = n_round / cycle_length;
			soln += n_people_in_cycle * n_cycle;

			if ((n_round %= cycle_length) > 0) {
				gid = cycle_start_gid;
				for (int i=0; i<n_round; ++i) {
					soln += n_people_in_same_round[gid];
					gid = next_group[gid];
				}
			}
		}

		printf ("Case #%d: %lld\n", serial++, soln);

		// END test case
	}

	return 0;
}