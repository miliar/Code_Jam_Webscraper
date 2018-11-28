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

#define maxn 105
#define inf 1000000000

int D, I, M, n;
int a[maxn];
int dp[maxn][300];

int add_cost(int a, int b)
{
	if (a == 256)
		return 0;
	if (a == b) return 0;
	if (M == 0) return inf;
	if (a > b)
		swap(a, b);
	return ((b - a - 1) / M) * I;
}

int calc(int n_used, int last)
{
	int &res = dp[n_used][last];
	if (res == -1)
	{
		if (n_used == n)
			res = 0;
		else
		{
			// delete
			res = calc(n_used + 1, last) + D;
			// modify
			for (int i = 0; i < 256; i++)
				res = min(res, calc(n_used + 1, i) + (int)labs(a[n_used] - i) + add_cost(last, i));
		}
	}
	return res;
}

void solvecase() {
	scanf("%d%d%d%d", &D, &I, &M, &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &a[i]);
	CLR(dp, -1);
	int res = calc(0, 256);
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