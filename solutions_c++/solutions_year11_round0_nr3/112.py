/*
	ID: lkq19921
	PROG: c
	LANG: C++
*/
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#define INF 2111222333
#define MAX(a, b)    ((a) > (b) ? (a) : (b))
#define MIN(a, b)    ((a) < (b) ? (a) : (b))
#define eps 1e-8
#define MAXN 1010
#define DEBUG

using namespace std;

int n;

void Solve()
{
	int i, tmp, xr, minv = INF, sum;
	cin >> n;
	for (i = 0, xr = 0, sum = 0; i < n; i++)
	{
		cin >> tmp;
		xr ^= tmp;
		sum += tmp;
		minv = MIN(minv, tmp);
	}
	if (xr != 0)
		printf("NO\n");
	else
		printf("%d\n", sum - minv);
}

int main()
{
	#ifdef DEBUG
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	#endif
	int t, f;
	cin >> t;
	for (f = 1; f <= t; f++)
	{
		printf("Case #%d: ", f);
		Solve();
	}
	return 0;
}


