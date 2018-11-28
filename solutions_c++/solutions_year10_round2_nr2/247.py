#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)

using namespace std;

long long X[100];
long long V[100];

int cost[100];
bool reaches[100];
bool queues[100][100];

int main() {
	long long C, N, K, B, T;
	
	scanf("%lld\n", &C);
	
	FOR(nCase, C) {
		scanf("%lld %lld %lld %lld\n", &N, &K, &B, &T);
		
		FOR(i, N) scanf("%lld", &X[i]);
		FOR(i, N) scanf("%lld", &V[i]);
		
		for(int i = N-1; i >= 0; i--) {
			reaches[i] = X[i] + V[i]*T >= B;
			if(!reaches[i]) continue;
			
			cost[i] = 0;
			for(int j = i+1; j < N; j++) {
				if(reaches[j]) {
					if(V[i] >= V[j] && X[i] + V[i]*T >= X[j] + V[j]*T) { // chick i queues behind chick j
						cost[i] += cost[j];
						break;
					} else { // chick i is slower than chick j
						// try next chick
					}
				} else {
					cost[i]++;
				}
			}
		}
		
		int ans = 0, reach = 0;
		for(int i = N-1; i >= 0 && reach < K; i--) {
			if(!reaches[i]) continue;
			reach++;
			ans += cost[i];
		}
		
		if(reach < K)
			printf("Case #%d: IMPOSSIBLE\n", nCase+1);
		else
			printf("Case #%d: %d\n", nCase+1, ans);
	}
}
