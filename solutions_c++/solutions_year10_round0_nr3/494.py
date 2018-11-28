#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#define MAXN 1024
#define NEXT(j,N) ((j)+1==(N)?0:(j)+1)
#define LL long long
using namespace std;
LL solve(LL R, LL k, int N, LL g[]) {
	int vis[MAXN], pos = 0, prepos = N, j;
	LL euro[MAXN];
	memset(vis, -1, sizeof(vis));
	memset(euro, 0, sizeof(euro));
	LL gsum = 0;
	for(int i = 0; i < N; ++i)
		gsum += g[i];
	for(int i = 0; i < R; ++i) {
		LL sum = 0;
		if(k >= gsum) {
			j = pos;
			sum = gsum;
		}
		else
			for(j = pos; sum + g[j] <= k; j = NEXT(j, N)) {
				sum += g[j];
			}
		if(vis[pos] != -1) {
			LL eurodiff = euro[prepos] + sum - euro[pos];
			int idiff = i - vis[pos];
			LL ret = euro[prepos] + (R - 1 - i) / idiff * eurodiff;
			int rem = vis[pos] + (R - 1 - i) % idiff;
			for(int j = 0; j < N; ++j)
				if(vis[j] == rem) {
					ret += euro[j];
					break;
				}
			for(int j = 0; j <= N; ++j)
				if(vis[j] == vis[pos] - 1)
					return ret - euro[j];
		}
		vis[pos] = i;
		euro[pos] = euro[prepos] + sum;
		prepos = pos;
		pos = j;
	}
	return euro[prepos];
}
int main() {
	int T;
	scanf("%d", &T);
	for(int cs = 1; cs <= T; ++cs) {
		int N;
		LL R, k, g[MAXN];
		scanf("%lld%lld%d", &R, &k, &N);
		for(int i = 0; i < N; ++i)
			scanf("%lld", &g[i]);
		printf("Case #%d: %lld\n", cs, solve(R, k, N, g));
	}
	return 0;
}
