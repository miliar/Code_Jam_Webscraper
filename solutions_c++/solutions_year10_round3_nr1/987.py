#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
using namespace std;

int x[5], y[5];
bool ok;

pair<int,int> norm(int v1, int v2, int v3, int v4)
{
	int
	ax = x[v2] - x[v1], ay = y[v2] - y[v1],
	bx = x[v3] - x[v1], by = y[v3] - y[v1],
	cx = x[v4] - x[v1], cy = y[v4] - y[v1];
	return make_pair(ax*by-ay*bx, ax*cy-ay*cx);
}

void calc(int &x)
{
	if (x > 0) x = 1; else
	if (x < 0) x = -1;
}

bool between(int a, int b, int c)
{
	return (min(x[b], x[c]) <= x[a] && x[a] <= max(x[b], x[c])) &&
	       (min(y[b], y[c]) <= y[a] && y[a] <= max(y[b], y[c]));
}

int intersects(int y1, int y2, int y3, int y4)
{
    y[1] = y1; y[2] = y2; y[3] = y3; y[4] = y4;
	x[1] = x[3] = 0; x[2] = x[4] = 1;
	pair<int,int> p1 = norm(1, 2, 3, 4), p2 = norm(3, 4, 1, 2);

	if (!p1.first && !p1.second && !p2.first && !p2.second)
		ok = between(1, 3, 4) ||
		     between(2, 3, 4) ||
		     between(3, 1, 2) ||
		     between(4, 1, 2); else
	{
		calc(p1.first);
		calc(p1.second);
		calc(p2.first);
		calc(p2.second);
		ok = p1.first != p1.second && p2.first != p2.second;
	}
	return ok;
}

int k, t, i, j, n, a[1001], b[1001], ans;

int main()
{
	freopen("a.in", "r", stdin);
   	freopen("a.out", "w", stdout);
   	cin >> t;
   	for (k = 1; k <= t; k++)
   	{
   		ans = 0;
   		cin >> n;
   		for (i = 0; i < n; i++)
   			cin >> a[i] >> b[i];
		for (i = 0; i < n - 1; i++)
			for (j = i + 1; j < n; j++)
				ans += (intersects(a[i], b[i], a[j], b[j]));
		cout << "Case #" << k << ": " << ans << endl;
   	}
}
