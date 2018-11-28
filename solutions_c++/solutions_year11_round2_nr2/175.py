#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <cassert>
#include <fstream>
#include <sstream>
#include <bitset>
#include <stack>
#include <list>
#define debug1(x) cout << #x" = " << x << endl;
#define debug2(x, y) cout << #x" = " << x << " " << #y" = " << y << endl;
#define debug3(x, y, z) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << endl;
#define debug4(x, y, z, w) cout << #x" = " << x << " " << #y" = " << y << " " << #z" = " << z << " " << #w" = " << w << endl;
using namespace std;

int T; int testid;

int C;
double D;
vector<double> ps;

bool isOK(double t)
{
	double last = ps[0] - t;
	for (int i = 1; i < ps.size(); ++i)
	{
		double now = ps[i];
		double newlast;
		if (now >= last + D)
		{
			newlast = max(last + D, now - t);
		}
		else
		{
			newlast = min(last + D, now + t);
		}

		if (newlast - last < D) return false;
		last = newlast;
	}
	return true;
}

void york()
{
	double l = 0;
	double r = 1e12;
	
	for (int iter = 0; iter <= 200; ++iter)
	{
		double mid = (l + r) / 2;
		//debug3(l, r, mid);
		if (isOK(mid)) r = mid;
		else l = mid;
	}

	printf("Case #%d: %.10f\n", testid, l);
}

void init()
{
	scanf("%d%lf", &C, &D);
	ps.clear();
	for (int i = 0; i < C; ++i)
	{
		int p, v;
		scanf("%d%d", &p, &v);
		for (int j = 0; j < v; ++j)
			ps.push_back(p);
	}

	sort(ps.begin(), ps.end());
}

int main()
{
	scanf("%d", &T);
	for (testid = 1; testid <= T; ++testid)
	{
		init();
		york();
	}
	return 0;
}