#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()

typedef unsigned long long ull;
typedef long long lint;
typedef pair < int , int > pii;
typedef long double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#else
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
}

const int nmax = 205;
int n;
double J[nmax];
double X;

bool LOSE(int id,double y)
{
	double cur = J[id] + X * y;
	double ssum = y;

	for (int i = 0; i < n; i ++)
	{
		if (i != id)
		{
			double mn = max( 0.0, (cur - J[i]) / X);
			ssum += mn;
		}
	}

	return ssum <= 1.0;
}

bool solve()
{
	X = 0;
	cin >> n;
	for (int i = 0; i < n; i ++)
	{
		cin >> J[i];
		X += J[i];
	}

	for (int it = 0; it < n; it ++)
	{
		double l = 0,r = 1.0;
		for (int iters = 0; iters < 300; iters ++ )
		{
			double mid = (l + r) / 2.0;
			if (LOSE(it,mid))
				l = mid;
			else
				r = mid;
		}
		printf(" %.6lf",r * 100);
	}
	printf("\n");
	return false;
}

int main()
{
	prepare();
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
	{
		printf("Case #%d:",i + 1);
		solve();
	}
	return 0;
}