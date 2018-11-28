#pragma comment (linker, "/STACK:64000000")
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

#define maxn 2100
#define maxk 12
#define inf 500000000

int dp[maxn][maxk];
int cnt[maxn], cost[maxn];
int p, N, D;

int calc(int v, int k)
{
	int &res = dp[v][k];
	if (res == -1)
	{
		res = inf;
		if (v < N)
		{			
			res = min(res, calc(2*v, k+1) + calc(2*v+1, k+1) + cost[v]);
			res = min(res, calc(2*v, k) + calc(2*v+1, k));
		}
		else
		{
			if (k >= cnt[v])
				res = 0;
			else
				res = inf;
		}
	}
	return res;
}

void solvecase() {
	scanf("%d", &p);	
	N = 1<<p;
	for (int i = 0; i < N; i++)
	{
		int t;
		scanf("%d", &t);
		cnt[N+N-i-1] = p - t;
	}
	for (int i = N-1; i > 0; i--)
	{
		scanf("%d", &cost[i]);
	}
	CLR(dp, -1);
	int res = calc(1, 0);
	printf("%d", res);
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	//freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}