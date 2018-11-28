#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const long double EPS = 1e-9;
const long double PI = 3.1415926535897932384626433832795;

typedef long double ld;

ld x, s, r, n;
ld t;
int b[1024];
int e[1024];
int w[1024];
bool u[1024];

ld min_time(ld x, ld s, ld r)
{
	ld tt = x / r;
	if (t * r < x + EPS)
		tt = t;
	t -= tt;
	return tt + (x - tt * r) / s;
}

int main()
{
//	freopen("input.txt", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cout << setiosflags(ios::fixed) << setprecision(10);

	int tcn;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		cin >> x >> s >> r >> t >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> b[i] >> e[i] >> w[i];
		}

		ld res = 0, last = 0;
		for (int i = 0; i < n; i++)
		{
			res += min_time(b[i] - last, s, r);
			last = e[i];
		}
		res += min_time(x - last, s, r);

		memset(u, 0, sizeof(u));
		for (int i = 0; i < n; i++)
		{
			int mn = -1;
			for (int j = 0; j < n; j++)
			{
				if (!u[j] && (mn == -1 || w[mn] > w[j]))
					mn = j;
			}
			u[mn] = true;
			res += min_time(e[mn] - b[mn], w[mn] + s, w[mn] + r);
		}
		
	    cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}
