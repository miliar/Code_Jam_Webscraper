#pragma comment(linker, "/STACK:60000000")
//#define _MY_OPT_MODE_
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <deque>

#include <ctime>
#include <cassert>

using namespace std;

typedef long double ldb;
typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

#define left L
#define right R
#define up U
#define down D
#define y0 wwwwwww
#define y1 qqqqqqq
#define next NEXT
#define prev PREV
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define ford(i, n) for (int i = (int) n - 1; i >= 0; i--)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define last(a) a[a.size() - 1]
#define mp make_pair

template <class T> T sqr(T x) { return x * x; }

double const pi = 3.1415926535897932384626433832795;
int const inf = (int) 1e9;
int64 const inf64 = (int64) 4e18;
const string name = "b";

const int NMAX = 100010;
const double eps = 1e-9;

double D, A, t[NMAX], x[NMAX];
int n, m;

void calc(double &X, double &T, double &V)
{
	double l = 0, r = 1e18;
	forn(i, 150)
	{
		double m = (l + r) / 2, tmp;
		if (m > t[n - 1] - eps) tmp = D;
		else
			forn(i, n)
				if (m < t[i] - eps)
				{
					tmp = x[i - 1] + (m - t[i - 1]) / (t[i] - t[i - 1]) * (x[i] - x[i - 1]);
					break;
				}
		if (A * m * m / 2 > min(tmp, D)) r = m;
		else l = m;
	}
	T = (l + r) / 2;
	V = A * T;
	X = A * T * T / 2;
}

void recalc(double &X, double &T, double &V,  double D, double U)
{
	if (D - X < eps) return;
	V = min(V, U);
	{
		double delta = (U - V) / A;
		if (V * delta + A * delta * delta / 2 < D - X)
		{
			X += V * delta + A * delta * delta / 2;
			V = U;
			T += delta;
		}
		else
		{
			delta = -V / A + sqrt(fabs(V * V + 2 * A * (D - X))) / A;
			T += delta;
			V += A * delta;
			X = D;
			return;
		}
	}

	{
		T += (D - X) / V;
		X = D;
	}
}

void solve()
{
	cin >> D >> n >> m;
	forn(i, n)
		cin >> t[i] >> x[i];
	forn(i, m)
	{
		cin >> A;
		double X, T, V;
		calc(X, T, V);
		forn(j, n - 1)
			if (X < x[j + 1] - eps)
				recalc(X, T, V, min(x[j + 1], D), (x[j + 1] - x[j]) / (t[j + 1] - t[j]));
		printf("%.6lf\n", T);
	}
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);
#endif

	int tst;
	cin >> tst;
	forn(i, tst)
	{
		cout << "Case #" << i + 1 << ":" << endl;
		solve();
	}

	return 0;
}
