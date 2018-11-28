// Google Code Jam 2010
// Gilberto Stankiewicz
// May 08, 2010

#include <stdio.h>
#define MAX 1002

int T; // number of test cases
int R; // times roller coaster runs
int K; // people roller coaster can hold
int N; // number of groups
int groups[MAX];
int n;
int sum;
int total;

int main() {
	int k;
	
	scanf("%d", &T);
	
	for (int i = 1; i <= T; i++) {
		// input
		scanf("%d %d %d", &R, &K, &N);
		for (int j = 0; j < N; j++) {
			scanf("%d", &(groups[j]));
		}
		
		// simulation
		k = 0;
		total = 0;
		
		for (int j = 0; j < R; j++) {
			sum = 0;
			n = 0;
			while (sum + groups[k] <= K && n < N) {
				sum += groups[k];
				
				n++;
				k++;
				if (k == N) {
					k = 0;
				}
			}
			total += sum;
		}
		
		printf("Case #%d: %d\n", i, total);
	}
	
	return 0;
}
