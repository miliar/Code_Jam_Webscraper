#include <cstdio>
#include <queue>

#define nmax 10000000
using namespace std;
int Q [nmax], A [nmax];
int cost, i, T, R, k, N, a, sum, j, front, back, ind1, ind,  begin;
int main () {
	freopen ("qc.in", "r", stdin);
	freopen ("qc.out", "w", stdout);
	scanf ("%d\n", &T);
	for (i = 1; i <= T; i++) {
		back = 0;
		scanf ("%d%d%d\n", &R, &k, &N);
		for (j = 1; j <= N; j++) {
			scanf ("%d", &a);
			Q [++back] = a;
		}
		cost = 0;begin = 1;
		for (j = 1; j <= R; j++) {
			sum = 0;
			front = 1;
			while (sum <= k) {
				if (sum + Q [front] <= k) {
					sum += Q [front];
					++front;
					if (front == back + 1) break;
				}
				else break;
				//if (i == 2) printf ("%d\n", sum);
			}
			if (front != back + 1) {
				ind1 = 0;
				for (ind = front; ind <= back; ind++)
					A [++ind1] = Q [ind];
				for (ind = 1; ind <= front; ind++)
					A [++ind1] = Q [ind];
				for (ind = 1; ind <= back; ind++)
					Q [ind] = A [ind];
			}
		//	if (i == 2) printf ("%d\n", sum);
			cost += sum;
		}
		printf ("Case #%d: %d\n", i, cost);
	}
	return 0;
}

