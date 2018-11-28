#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

typedef long long llong;

const llong INF = 1LL<<60;
const int N = 12;

llong dp[1<<N][N];
int m[1<<N], n, p, price[1<<N];

// maxv: the largest number of uncovered is maxv
llong go(int depth, int id, int maxv)
{
	if(maxv >= p) return 0;
	
	// if(depth == p)printf(".... %d %d %d %lld\n", depth, id, maxv, (maxv >= p-m[id-n]) ? 0 : INF);
	
	if(depth == p) return (maxv >= p-m[id+1-n]) ? 0 : INF;
	
	llong& res = dp[id][maxv];
	if(res != -1) return res;
	res = INF;
	// try to get it
	res = min(res, go(depth+1, 2*id+1, maxv+1) + go(depth+1, 2*id+2, maxv+1) + price[id]);
	// not to get it
	res = min(res, go(depth+1, 2*id+1, maxv) + go(depth+1, 2*id+2, maxv));
	
	// printf("%d %d %d %lld\n", depth, id, maxv, res);
	
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		scanf("%d", &p);
		n = 1<<p;
		for(int i = 0; i < n; i++) scanf("%d", &m[i]);
		int sum = 0;
		for(int i = 0; i < p; i++) {
			int num = 1<<(p-i-1);
			for(int j = 0; j < num; j++) scanf("%d", &price[j+sum]);
			for(int j = 0; j+j < num; j++) swap(price[j+sum], price[num-1-j+sum]);
			sum += num;
		}
		for(int i = 0; i+i < sum; i++) swap(price[i], price[sum-1-i]);
		
		// for(int i = 0; i < sum; i++) printf("%d ", price[i]); printf("\n");
		
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %lld\n", t+1, go(0, 0, 0));
	}
	return 0;
}

