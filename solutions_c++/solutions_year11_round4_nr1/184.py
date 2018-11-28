/*
 * 2011-06-04  Martin  <Martin@Martin-desktop>

 * 
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#ifndef TEMPLATE_BY_TOKEN
//Part1
#define pi 3.1415926535897932384626433832795028841971693993715058209749445923078164062862089986280348253421170679
//Part2
#define ll long long
#define pii pair <int, int>
#define cmplxd complex <double>
//Part3
template <class T> inline T checkmin(T &a, T b)
{
	return (a < b) ? a : a = b;
}

template <class T> inline T checkmax(T &a, T b)
{
	return (a > b) ? a : a = b;
}

template <class T> inline T sqr(T x)
{
	return x * x;
}

template <class T> inline T Lowbit(T x)
{
	return x & (- x);
}

template <class T> T GCD(T a, T b)
{
	if (a < 0)
		return GCD(- a, b);
	if (b < 0)
		return GCD(a, - b);
	return (a == 0) ? b : GCD(b % a, a);
}

template <class T> T LCM(T a, T b)
{
	if (a < 0)
		return LCM(- a, b);
	if (b < 0)
		return LCM(a, - b);
	return (a == 0 || b == 0) ? 0 : a / GCD(a, b) * b;
}

template <class T> T ExtGCD(T a, T b, T &x, T &y)
{
	if (a < 0)
	{
		T c = ExtGCD(- a, b, x, y);
		x = - x;
		return c;
	}
	if (b < 0)
	{
		T c = ExtGCD(a, - b, x, y);
		y = - y;
		return c;
	}
	if (a == 0)
	{
		x = 0, y = 1;
		return b;
	}
	else
	{
		T c = ExtGCD(b % a, a, y, x);
		x -= b / a * y;
		return c;
	}
}
#endif

#define rep(i, n) for (int i = 0; i < n; ++ i)
#define forvector(i, v) for (int i = 0; i < (int) (v).size(); ++ i)
#define pb push_back
#define mp make_pair
#define x first
#define y second

double R;

bool Compare(pair <double, double> a, pair <double, double> b)
{
	return (100000.0 / a.y - 100000.0 / (a.y + R) < 100000.0 / b.y - 100000.0 / (b.y + R));
}

double solve()
{
	double X, S, T;
	int N;
	scanf("%lf%lf%lf%lf%d", &X, &S, &R, &T, &N);
	vector < pair <double, double> > Speed;
	Speed.clear();
	rep (i, N)
	{
		int B, E;
		double W;
		scanf("%d%d%lf", &B, &E, &W);
		Speed.pb(mp(E - B, W + S));
		X -= (E - B);
	}
	Speed.pb(mp(X, S));
	double ans = 0.0;
	forvector (i, Speed)
		ans += Speed[i].x / Speed[i].y;
	R -= S;
	sort(Speed.begin(), Speed.end(), Compare);
	while (T > 1e-12 && !Speed.empty())
	{
		double s = Speed.back().x, v = Speed.back().y;
		Speed.pop_back();
		double s0 = (v + R) * T;
		ans -= min(s, s0) / v;
		T -= min(s, s0) / (v + R);
		ans += min(s, s0) / (v + R);
	}
	return ans;
}

int main()
{
	int TestCase;
	scanf("%d", &TestCase);
	rep (i, TestCase)
		printf("Case #%d: %.9lf\n", i + 1, solve());
}
