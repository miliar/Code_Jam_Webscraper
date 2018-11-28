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

#define maxn 1005

int r, k, n;
int g[maxn];
bool f[maxn];
int when[maxn];
LL v[maxn];

LL go()
{
	LL sum = 0;
	for (int i = 0; i < n; i++)
		sum += g[i];
	if (sum <= k)
		return sum * r;

	LL cur = 0;
	CLR(f, 0);
	int p = 0;
	int day = 0;
	while (!f[p])
	{
		f[p] = true;
		when[p] = day;
		v[p] = cur;
		if (day == r)
			return cur;
		int have = 0;
		while (have + g[p] <= k)
		{
			have += g[p];
			p = (p+1) % n;
		}
		cur += have;
		day++;
	}

	r -= day;
	int len = day - when[p];
	LL x = cur - v[p];

	cur += x * (r / len);
	r %= len;

	for (int i = 0; i < r; i++)
	{
		int have = 0;
		while (have + g[p] <= k)
		{
			have += g[p];
			p = (p+1) % n;
		}
		cur += have;
	}

	return cur;
}

void solvecase() {
	scanf("%d%d%d", &r, &k, &n);
	for (int i = 0; i < n; i++) scanf("%d", &g[i]);
	LL res = go();
	printf("%lld", res);
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
	//freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}