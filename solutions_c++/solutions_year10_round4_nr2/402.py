#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define INF 999999999999LL

int P;
long long M[2048];
long long cost[11][2048];

long long cache[11][2048][12]; // row, matchup, missed


int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		scanf("%d",&P);
		for (int i = 0; i < (1<<P); i++) scanf("%lld",&M[i]);
		for (int i = 0; i < P; i++) {
			for (int j = 0; j < (1<<(P-1-i)); j++) {
				scanf("%lld",&cost[i][j]);
			}

		}

		for (int round = 0; round < P; round++) {
		for (int match = 0; match < (1<<(P-1-round)); match++) {
		for (int k = 0; k <= P; k++) {
			if (round == 0) {
				if (M[match*2] >= k+1 && M[match*2+1] >= k+1) {
					cache[round][match][k] = 0;
				} else if (M[match*2] >= k && M[match*2+1] >= k) {
					cache[round][match][k] = cost[round][match];
				} else {
					cache[round][match][k] = INF;
				}
			} else {
				cache[round][match][k] = INF;
				cache[round][match][k] = min(cache[round][match][k],cache[round-1][match*2][k]+cache[round-1][match*2+1][k]+cost[round][match]);
				if (k+1 <= P) cache[round][match][k] = min(cache[round][match][k],cache[round-1][match*2][k+1]+cache[round-1][match*2+1][k+1]);
			}
		}
		}
		}
		
		printf("Case #%d: %lld\n",test,cache[P-1][0][0]);
	}
}
