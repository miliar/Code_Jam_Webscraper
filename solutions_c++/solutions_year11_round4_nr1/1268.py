#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <ctime>
#include <string>

using namespace std;

typedef vector<int> vint;
typedef vector<vint> vvint;
//typedef double D;
typedef long long LL;

const int inf = 1000 * 1000 * 1000;
const LL INF = 1000000000ll * 1000000000ll;
const double eps = 1e-8;

int T, x, s, r, n;
double t;

struct P
{
	int w, b, e;
	P() {}
	void scan()
	{
		cin >> b >> e >> w;
	}
};

P a[1 << 10];

bool operator<(const P & a, const P & b)
{
	return a.w < b.w;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> T;
	for(int I = 1; I <= T; ++I)
	{
		cin >> x >> s >> r >> t >> n;
		double len = 0;
		for(int j = 0; j < n; ++j)
		{
			a[j].scan();
			len += (a[j].e - a[j].b);
		}
		len = x - len;
		double res = 0;
		if (r * t > len)
		{
			res = (len / (r + 0.0));
			t -= res;
		}
		else
		{
			len -= r * t;
			res = t + (len / (s + 0.0));
			t = 0;
		}
		sort(a, a + n);
		for(int i = 0; i < n; ++i)
		{
			if (t > eps)
			{
				double time = (a[i].e - a[i].b) / (a[i].w + r + 0.0);
				if (time > t)
				{
					double ss = (a[i].w + r + 0.0) * t;
					res += t;
					t = 0;
					res += (a[i].e - a[i].b - ss) / (a[i].w + s + 0.0);
				}
				else
				{
					res += time;
					t -= time;
				}
			}
			else
				res += (a[i].e - a[i].b) / (a[i].w + s + 0.0);
		}
		printf("Case #%d: %.8lf\n", I, res); 
	}
	return 0;
}