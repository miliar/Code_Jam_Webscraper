#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
const int INF = 1000000000;

typedef pair<int, int> pii;

#define all(s) s.begin(), s.end()

struct ship
{
	int x, y, z, p;
};
vector<ship> a;
double tern2 (double x);
double tern3 (double x, double y);

const double EPS1 = 1E-6, EPS2 = 1E-6 /3 , EPS3 = 1E-7;

double tern1 ()
{
	double best = 1E+16;
	double l = -1, r = 1000000;
	while (r - l > EPS1)
	{
		double m1 = (r - l) / 3 + l, m2 = (r - l) * 2 / 3 + l;
		double res1 = tern2(m1), res2 = tern2(m2);
		if (res1 < res2)
			r = m2;
		else
			l = m1;
		best = min(best, res1);
	}
	return best;
}

double tern2 (double x)
{
	double best = 1E+16;
	double l = -1, r = 1000000;
	while (r - l > EPS2)
	{
		double m1 = (r - l) / 3 + l, m2 = (r - l) * 2 / 3 + l;
		double res1 = tern3(x, m1), res2 = tern3(x, m2);
		if (res1 < res2)
			r = m2;
		else
			l = m1;
		best = min(best, res1);
	}
	return best;
}

int n;
double tern3 (double x, double y)
{
	double best = 1E+16;
	double l = -1, r = 1000000;
	while (r - l > EPS3)
	{
		double m1 = (r - l) / 3 + l, m2 = (r - l) * 2 / 3 + l;
		double res1 = 0, res2 = 0;
		for (int i = 0; i < n; ++i)
			res1 = max(res1, (abs(a[i].x - x) + abs(a[i].y - y) + abs(a[i].z - m1)) / a[i].p);
		for (int i = 0; i < n; ++i)
			res2 = max(res2, (abs(a[i].x - x) + abs(a[i].y - y) + abs(a[i].z - m2)) / a[i].p);

		if (res1 < res2)
			r = m2;
		else
			l = m1;		
		best = min(best, res1);
	}
	return best;
}


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		cerr << test << endl;
		cin >> n;
		a.resize(n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d%d%d", &a[i].x, &a[i].y, &a[i].z, &a[i].p);
		printf("Case #%d: %.6f\n", test, tern1());
	}

}