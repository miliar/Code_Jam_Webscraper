using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (LL)1e18
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;

int main() {
	int kases = GI+1;
	LL r, k, g[1002];
	int n;
	FOR(kase, 1, kases) {
		r = GI, k = GI, n = GI;
		REP(i,n) g[i] = GI;
		int next[n];
		LL canTake[n];
		
		REP(i,n) {
			LL sum = 0;
			next[i] = -1, canTake[i] = 0;
			int seen[n];
			REP(j,n) seen[j] = 0;
			for(int j = i; !seen[j] && sum <= k; j = (j+1)%n) {
				seen[j] = 1;
				sum += g[j];
				if(sum <= k) {
					canTake[i] = sum;
					next[i] = (j+1)%n;
				}
			}
//			cout << i <<" to " << next[i] <<" taking " << canTake[i] << endl;
		}		
		int cur = 0;
		LL taken = 0LL;
		while(r--) {
			taken += canTake[cur];
			cur = next[cur];
		}
		printf("Case #%d: %Ld\n", kase, taken);
	}
}
