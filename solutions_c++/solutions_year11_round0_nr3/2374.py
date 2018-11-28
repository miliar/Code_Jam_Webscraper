#include <cstdio>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define MIN(a,b) ((a)<(b) ? (a):(b))

using namespace std;

int v[1010], T, N;
int dp[1010][1010];

int main() {
	int t, tt, m;
	
	scanf("%d", &T);
	FOR(i,0,T) {
		m = 1111111;
		t = tt = 0;
		scanf("%d", &N);
		FOR(j,0,N) {
			scanf("%d", &v[j]);
			t ^= v[j]; tt += v[j]; m = MIN(v[j], m);
		}
		if (t != 0)
			printf("Case #%d: NO\n", i+1);
		else
			printf("Case #%d: %d\n", i+1, tt-m);
	}
	return 0;
}