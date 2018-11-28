#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>
#include <numeric>

using namespace std;

#define INF (2000000000)

#pragma comment(linker, "/STACK:167772160")

const int nmax = 1 << 21;

int R, S;

struct Segm
{
	double L;
	double W;

	Segm(double LL = 0.0, double WW = 0.0): L(LL), W(WW) {}
	bool operator<(const Segm& s) const 
	{
		return W < s.W;
	}
};

Segm s[nmax];

void solveTest()
{
	int X;
	double t;
	int n;
	scanf("%d%d%d%lf%d", &X, &S, &R, &t, &n);
	int cnt = 0;
	int Lf = 0, Rg;
	for(int i = 0; i < n; ++i)
	{
		int b, e, w;
		scanf("%d%d%d", &b, &e, &w);
		Rg = b;
		s[cnt] = Segm(Rg - Lf, 0);
		++cnt;
		s[cnt] = Segm(e - b, w);
		++cnt;
		Lf = e;
	}
	Rg = X;
	s[cnt] = Segm(Rg - Lf, 0);
	++cnt;

	sort(s, s + cnt);
	double res = 0.0;
	int next = cnt;
	for(int i = 0; i < cnt; ++i)
	{
		double tt = s[i].L / (s[i].W + R);
		if (tt < t)
		{
			res += tt;
			t -= tt;
		}
		else
		{
			s[i].L -= (s[i].W + R) * t;
			res += t;
			t = 0.0;

			res += s[i].L / (s[i].W + S);

			next = i + 1;
			break;
		}
	}
	for(int i = next; i < cnt; ++i)
	{
		res += s[i].L / (s[i].W + S);
	}
	printf("%.9lf\n", res);
}

int main()
{
	int t;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	for(int i = 0; i < t; ++i)
	{
		printf("Case #%d: ", i + 1);
		solveTest();
		cerr << i + 1 << " Done!\n";
	}
	return 0;
}
