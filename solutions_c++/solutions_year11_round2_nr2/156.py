#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
using namespace std;

const int N_MAX = 330;
int v[N_MAX], p[N_MAX];
int c;
LD d;

const LD EPS = 1.0E-12;
const LD INF = 1.0E30;

bool f(LD t)
{
	LD x0 = -INF;
	for (int i = 0; i < c; ++i)
	{
		LD len = (v[i] - 1) * d;
		LD cl = p[i] - len * 0.5L;

		if (x0 + d <= cl)
			x0 = max(p[i] - t, x0 + d) + len;
		else if (x0 + d + len - p[i] <= t)
			x0 = x0 + len + d;
	    else return false;
	}

	return true;
}

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tst;
	cin >> tst;

	for (int t = 1; t <= tst; ++t)
	{
		int di;
		cin >> c >> di;

		int mintime = 0;

		for (int i = 0; i < c; ++i)
		{
			cin >> p[i] >> v[i];
			mintime = max(v[i] - 1, mintime);
		}

		d = di;

		LD L = mintime * d * 0.5L;
		LD R = INF;

		const int ITER = 20000;
		for (int it = 0; it < ITER; ++it)
		{
			LD m = (L + R) * 0.5L;
			if (f(m)) R = m; else L = m;
		}
		cout << "Case #" << t << ": " << fixed << setprecision(8) << (L + R) * 0.5L << '\n';
	}


	return 0;
}
