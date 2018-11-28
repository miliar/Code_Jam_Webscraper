#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

#define inf 2000000001
#define ll long long
#define minim(a, b) ((a < b) ? a : b)
#define maxim(a, b) ((a > b) ? a : b)
#define pii pair<int, int>
#define x first
#define y second
#define pb push_back
#define mp make_pair

int N;
char m[128][128], aux[128];
double wp[128], owp[128], oowp[128];

double comp_wp(int team)
{
	int j, win, total;
	win = total = 0;
	for (j = 0; j < N; ++j)
	{
		if (m[team][j] == '1')
			++win;
		if (m[team][j] != '.')
			++total;
	}
	return (double)win/total;
}

double comp_owp(int team)
{
	int j, total = 0;
	double sum = 0;
	
	for (j = 0; j < N; ++j)
		if (m[team][j] != '.')
			++total;
		
	for (j = 0; j < N; ++j)
	{
		aux[j] = m[j][team];
		m[j][team] = '.';
	}

	for (j = 0; j < N; ++j)
		if (m[team][j] != '.')
			sum += comp_wp(j);
	
	for (j = 0; j < N; ++j)
		m[j][team] = aux[j];

	return sum/total;
}

int main()
{
	int T, t, i, j;
	int total;
	
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		printf("Case #%d:\n", t);
		
		memset(m, 0, sizeof(m));
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));
		
		scanf("%d", &N);
		for (i = 0; i < N; ++i)
			scanf("%s", m[i]);
		for (i = 0; i < N; ++i)
		{
			wp[i] = comp_wp(i);
			owp[i] = comp_owp(i);
		}
	
		for (i = 0; i < N; ++i)
		{
			total = 0;
			for (j = 0; j < N; ++j)
			{
				if (m[i][j] != '.')
				{
					++total;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= (double)total;
		}
		
		for (i = 0; i < N; ++i)
			printf("%.9lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	
	return 0;
}
