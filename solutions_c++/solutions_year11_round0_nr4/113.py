/*
	ID: lkq19921
	PROG: d
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

int ori[MAXN];
int srt[MAXN];
int n;

void Solve()
{
	int i, j, re, tmp;
	double d;
	scanf("%d", &n);
	memset (ori, 0, sizeof ori);
	memset (srt, 0, sizeof srt);
	for (i = 0, re = 0; i < n; i++)
	{
		scanf("%d", &ori[i]);
		srt[i] = ori[i];
	}
	sort (srt, srt + n);
	for (i = 0; i < n; i++)
		re += srt[i] == ori[i] ? 0 : 1;
	d = re;
	//printf("%d\n", re);
	printf("%.6f\n", d);
}

int main()
{
	#ifdef DEBUG
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
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


