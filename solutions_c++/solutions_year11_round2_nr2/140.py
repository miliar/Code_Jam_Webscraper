#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <cassert>
#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;

int TEST;
void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

int c;
lint d;
vector< double > x;

bool good(double t)
{
	double free = -1e30;
	for (int i = 0; i < x.size(); i++)
	{
		double shift = max(free - x[i], -t);
		if (shift > t)
			return false;
		free = x[i] + shift + (double)d;
	}
	return true;
}

bool solve()
{
	cerr << TEST << endl;

	TEST++;

	x.clear();

	scanf("%d%lld", &c, &d);
	for (int i = 0; i < c; i++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		for (int j = 0; j < b; j++)
			x.pb((double)a);
	}

	sort(x.begin(), x.end());

	double l = 0.0, r = 1e12;
	for (int k = 0; k < 150; k++)
	{
		double x = (l + r) * 0.5;
		if (good(x))
			r = x;
		else
			l = x;
	}
	printf("Case #%d: %.6lf\n", TEST, l);

	return false;
}

int main()
{
	prepare();
	int tn;
	TEST = 0;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}