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

#define maxn 300

int k, s;
int a[maxn][maxn];

void load()
{
	int st = k-1;
	int cnt = 1;
	for (int i = 0; i < k; i++)
	{
		for (int j = 0; j < cnt; j++)
			scanf("%d", &a[i][st+2*j]);
		st--;
		cnt++;
	}
	st = 1;
	cnt = k-1;
	for (int i = k; i < 2*k-1; i++)
	{
		for (int j = 0; j < cnt; j++)
			scanf("%d", &a[i][st+2*j]);
		st++;
		cnt--;
	}
}

void print()
{
	int s = 2*k-1;
	for (int i = 0; i < s; i++)
	{
		for (int j = 0; j < s; j++)
			printf("%d", a[i][j]);
		printf("\n");
	}
}

int f(int k)
{
	return k*k;
}

inline bool bad(int x, int y)
{
	return x != -1 && y != -1 && x != y;
}

void solvecase() {
	scanf("%d", &k);
	CLR(a, -1);
	load();
	//print();
	s = 2*k-1;
	// ver
	int szy = 1000;
	for (int i = 0; i < s; i++)
	{
		bool ok = true;
		for (int d = 1; i - d >= 0 && i + d < s; d++)
		{
			for (int j = 0; j < s; j++)
				if (bad(a[i-d][j], a[i+d][j]))
					ok = false;
		}
		if (ok)
		{
			int x = abs(k - (i+1));
			szy = min(x, szy);
		}
	}
	// hor
	int szx = 1000;
	for (int i = 0; i < s; i++)
	{
		bool ok = true;
		for (int d = 1; i - d >= 0 && i + d < s; d++)
		{
			for (int j = 0; j < s; j++)
				if (bad(a[j][i-d], a[j][i+d]))
					ok = false;
		}
		if (ok)
		{
			int x = abs(k - (i+1));
			szx = min(x, szx);
		}
	}

	int sz = k + szx + szy;
	int res = f(sz) - f(k);
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
	//freopen("A-small-attempt1.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}