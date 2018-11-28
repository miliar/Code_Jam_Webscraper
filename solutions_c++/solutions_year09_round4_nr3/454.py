#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "gcj";

int N,n,K,cnt;
int t[200][100];
bool a[200][200];
bool b[200][200];

pair<int,int> x[200];

bool f[200];

int getroot(int v)
{
	for (int i=0; i<n; ++i)
		if (a[x[i].second][x[v].second] && f[x[i].second])
			return getroot(i);
	return v;
}

void rec(int v, int lev)
{
	if (lev >= cnt)
		return;

	f[x[v].second] = false;
	bool f1 = true;
	for (int i=0; i<n; ++i)
		if (f[x[i].second] && a[x[v].second][x[i].second])
		{
			f1 = false;
			rec(i, lev);
		}

	if (f1)
	{
		int t = -1;
		for (t=0; t<n; ++t)
			if (f[x[t].second])
			{
				break;
			}
		if (t == n)
			cnt = min(cnt, lev);
		else
			rec(getroot(t), lev+1);
	}

	f[x[v].second] = true;
}

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &N);
	for (int I=1; I<=N; ++I)
	{
		scanf("%d%d", &n, &K);
		for (int i=0; i<n; ++i)
			for (int j=0; j<K; ++j)
				scanf("%d", &t[i][j]);

		for (int i=0; i<n; ++i)
		{
			x[i].first = 0;
			x[i].second = i;
		}

		for (int i=0; i<n; ++i)
			for (int j=0; j<n; ++j)
			{
				bool f = true;
				for (int l=0; l<K; ++l)
					f = f && (t[i][l] < t[j][l]);
				a[i][j] = f;
				if (f)
				{
					x[i].first -= 1000;
					//x[j].first -= 1;
				}
			}

		sort(&x[0], &x[n]);
		memset(f, true, sizeof f);
		
		cnt = 1000;
		rec(getroot(0), 0);

		printf("Case #%d: %d\n", I, cnt+1);
	}

	return 0;
} 