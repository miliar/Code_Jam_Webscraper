#include <cstdio>
#include <cmath>
#include <cstring>

#define MAXN 10000

using namespace std;

int dist[MAXN];
int len[MAXN];
int best[MAXN];
int n, end;

int min(int x, int y) {
	if ( x < y)
		return x;
	return y;
}

int solve() {

	int last = 0;
	int curlen, tmp, cur;

	memset(best,-1,sizeof(best));

	best[0] = dist[0];

	for (int i = 0; i <= last; ++i) {
		curlen = best[i];
		cur = i;

		if (curlen + dist[cur] >= end)
			return 1;
		
		for (int j = last+1; j < n; ++j) {
			if (curlen+dist[cur] < dist[j])
				break;

			last = j;
			tmp = min(dist[j]-dist[cur],len[j]);
			if (best[j] < tmp)
			       best[j] = tmp;	
		}
	}

	return -1;
}

int main() {

	int t;

	scanf("%d",&t);

	for (int tc = 0; tc < t; ++tc) {
		scanf("%d",&n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d",dist+i,len+i);
		}

		scanf("%d",&end);

		int res = solve();
		if ( res < 0)
			printf("Case #%d: NO\n",tc+1);
		else
			printf("Case #%d: YES\n",tc+1);
	}

	return 0;
}

