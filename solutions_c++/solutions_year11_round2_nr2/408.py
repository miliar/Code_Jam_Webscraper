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
#define eps 1e-8

#define NMax 1000006

int C, D, N;
int v[NMax];
double sv[NMax];

inline double modul(double x)
{ return x < 0 ? -x : x; }

inline int check(double d)
{
	int i;
	
	for (i = 1; i <= N; ++i)
		sv[i] = v[i];
	
	sv[N] += d;
	for (i = N-1; i; --i)
	{
		sv[i] = minim(sv[i+1] - D, sv[i] + d);
		if (modul(sv[i] - v[i]) > d + 1e-7)
			return 0;
	}
	return 1;
}

int main()
{
	int T, t, i, x, y;
	double st, dr, mid, sol;
	
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		fprintf(stderr, "Solving %d/%d\n", t, T);
		
		scanf("%d %d", &C, &D);
		
		N = 0;
		memset(v, 0, sizeof(v));
		
		for (i = 1; i <= C; ++i)
		{
			scanf("%d %d", &x, &y);
			for (; y; --y)
				v[++N] = x;
		}
		
		st = 0; dr = 1000000000000LL;
		
		check(1);
		
		while (st + eps < dr)
		{
			mid = (st + dr) / 2;
			if (check(mid))
				sol = mid, dr = mid - eps;
			else
				st = mid + eps;
		}
		
		printf("Case #%d: %.7lf\n", t, sol);		
	}
	
	return 0;
}
