#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10000000

int *g_Passenger;

long solve(long int round, long int k, long int ngroups) {
	long int currentSize, position = 0L, count;
	long int money = 0L;
	
	for(long int i=0L; i<ngroups; ++i) {
		scanf("%d", &g_Passenger[i]);
	}

	for(long int i=0L; i<round; ++i) {
		currentSize = count = 0L;
		do {
			if ( currentSize + g_Passenger[position] <= k ) {
				currentSize += g_Passenger[position];
				money += g_Passenger[position];
				if ( position < ngroups-1 ) {
					++position;
				} else {
					position = 0;
				}
				if ( ++count >= ngroups ) {
					break;
				}
			} else {
				break;
			}
		} while(1);
	}
	return money;
}

int main() {
	long int t, round, k, groups;

	scanf("%ld", &t);

	g_Passenger = (int *)malloc(sizeof(int) * MAX_SIZE);
	for(long int i=1L; i <= t; ++i) {
		scanf("%ld %ld %ld", &round, &k, &groups);
		printf("Case #%ld: %ld\n", i, solve(round, k, groups));
	}
	free(g_Passenger);

	return 0;
}
