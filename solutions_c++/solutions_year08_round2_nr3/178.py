//* Problem  : Mousetrap
//* Contest  : Google Code Jam 2008. Online Round 1B
//* Date     : 2008.07.26
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

#define int64 long long
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define FORSZ(i, a) FOR(i, SZ(a))
#define INF 1000*1000*1000
#define INFLL ((long long)INF*INF)
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()

#define int64 long long

#define PI (2.0 * acos(0.0))

int k, n, r[5024], it, nt;

int f[5024];

int a[5000];

int ii = 0;

/*
struct tree_item{
	int val;
	int used;
	int l, r;
	int count;
} aa[100010]; int plist;

int build(int l, int r)
{
	if (l > r) return 0;
	int m = (l + r) / 2;
	int p = ++plist;
	aa[p].val = m;
	aa[p].count = r - l + 1;
	aa[p].l = build(l, m - 1);
	aa[p].r = build(m + 1, r);
	return p;
}

int get(int k, int v)
{
	aa[k].count--;
	int c = aa[aa[k].l].count;
	if (c + 1 == v)
	{
		if (!aa[k].used)
		{
			aa[k].used = 1;
			return aa[k].val;
		}
		else
		{
			return get(aa[k].r, v - c);
		}
	}
	else if (c >= v)
		return get(aa[k].l, v);
	else
		return get(aa[k].r, v - c - !aa[k].used);
	return 0;
}
*/

int next[5024], prev[5024];

void calc(int v)
{
	for (int c = 0; c < v - 1; c++)
	{
		//while (a[ii]) ii = (ii + 1) % n;
		//ii = (ii + 1) % n;
		ii = next[ii];
	}
	//while (a[ii]) ii = (ii + 1) % n;
	int t = ii;
	int n = next[ii];
	int p = prev[ii];
	next[p] = n;
	prev[n] = p;
	ii = n;
	a[t] = v;
}

void solve()
{
	ii = 0;
	memset(a, 0 ,sizeof(a));
	for (int i = 0; i < n; i++)
	{
		next[i] = (i + 1) % n;
		prev[i] = (i - 1 + n) % n;
	}		
	for (int i = 1; i <= n; i++)
		calc(i);
//	for (int i = 0; i < n; i++)
//		r[a[i]] = i + 1;
}

void result()
{
	printf("Case #%d:", it);
	for (int i = 0; i < k; i++)
			printf(" %d", a[r[i]-1]);
	printf("\n");
}


int main()
{
//#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("A-small.out", "w", stdout);	
//#endif
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		memset(f, 0, sizeof(f));
		memset(r, 0, sizeof(r));
		scanf("%d%d", &n, &k);
		FOR(i,k)
		{
			scanf("%d", &r[i]);
		}
		solve();
		result();
	}
	return 0;
}

