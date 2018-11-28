#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

double sector(double r, double alpha)
{
	double res = alpha * r * r * 0.5;
	res -= r * r * sin(alpha) * 0.5;
	return res;
}

double calc(double x1, double y1, double x2, double y2, double x, double y)
{
	x2 -= x1, x -= x1;
	y2 -= y1, y -= y1;
	double s = x2 * x + y2 * y;
	s /= sqrt(x2 * x2 + y2 * y2);
	s /= sqrt(x * x + y * y);
	double alpha = acos(s);
	return sector(sqrt(x * x + y * y), 2.0 * alpha);
}

double X[10000], Y[10000];

void Solve()
{
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> X[i] >> Y[i];
	for (int i = 0; i < m; i++)
	{
		double x, y;
		cin >> x >> y;
		double res = calc(X[0], Y[0], X[1], Y[1], x, y) + calc(X[1], Y[1], X[0], Y[0], x, y);
		printf("%.7lf ", res);
	}
	cout << "\n";
}

int main()
{
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		Solve();
	}
	return 0;
}
