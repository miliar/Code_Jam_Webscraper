/*
 * $File: a.cpp
 * $Date: Sat May 26 22:37:19 2012 +0800
 * $Author: Xinyu Zhou <zxytim@gmail.com>
 */

#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define Ford(i, n) for (int i = n - 1; i >= 0; i --)
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T> void checkmax(T &a, T b) { if (b > a) a = b; }
template<typename T> void checkmin(T &a, T b) { if (b < a) a = b; }

typedef pair<int, int> pii;
typedef vector<pii> vpii;

void solve(int case_id);

int main()
{
	int ncase;
	scanf("%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		printf("Case #%d: ", id);
		solve(id);
	}
	return 0;
}

const int N = 10005;
int n;
int dist[N], len[N];
int D;
double f[N];
bool can[N];
void solve(int case_id)
{ scanf("%d", &n);
	for (int i = 1; i <= n; i ++)
		scanf("%d%d", &dist[i], &len[i]);
	scanf("%d", &D);
	dist[n + 1] = D;
	
	memset(f, 0, sizeof(f));
	memset(can, 0, sizeof(can));
	f[1] = min(dist[1], len[1]);
	can[0] = true;
	for (int i = 1; i <= n; i ++)
	{
		if (!f[i])
			continue;
		for (int j = i + 1; j <= n + 1; j ++)
		{
			int d = dist[j] - dist[i];
			if (d <= f[i] || (i == n && d <= f[i] + 1e-6))
			{
				f[j] = max(f[j], (double)min(d, len[j]));
				can[j] = true;
			}
		}
	}
	puts(can[n + 1] ? "YES" : "NO");

//	for (int i = 1; i <= n; i ++)
//		printf("%d: %lf\n", i, f[i]);
}

