#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXN 10005

struct Vine {
	int len, dist;
};

Vine v[MAXN];
int N;

int dp[MAXN];

bool solve() {
	int i, j, d;
	memset(dp, -1, sizeof(dp));
	for(i=1;i<=N;i++) {
		if(v[i].dist <= v[0].dist + v[0].dist) {
			dp[i] = 0;
		}
	}
	for(i=1;i<N; i++) if(dp[i] > -1) {
		d = v[i].dist - v[dp[i]].dist;
		d = min(d, v[i].len);
		for(j=i+1;j<=N;j++) {
			if(v[j].dist <= v[i].dist + d) {
				if(dp[j] == -1) dp[j] = i;
				else dp[j] = min(dp[j], i);
			}
		}
	}
	if(dp[N] == -1) return false;
	return true;
}

int main() {
	int T, kase=1;
	int i;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d",&N);
		rep(i, N) {
			scanf(" %d %d", &v[i].dist, &v[i].len);
		}
		scanf(" %d",&v[N].dist);

		if(solve()) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
