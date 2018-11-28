#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>

#define maxN (1000 * 1000 + 1000)

using namespace std;

int x, s, r, t, n;
int b[maxN], e[maxN], w[maxN];

pair <int, pair <int, int> > a[maxN];

#define eps 1E-8

bool equal (double a, double b)
{
	return abs (a - b) < eps;
}

double solve()
{
	double res = 0;
	int sum = 0;

	cin >> x >> s >> r >> t >> n;
	for (int i = 0; i < n; i++)
		cin >> b[i] >> e[i] >> w[i],
		sum += e[i] - b[i],
		a[i] = make_pair (w[i], make_pair (b[i], e[i]));

	sort (a, a + n);

	if ((x - sum) / r >= t)
	{
		res = t + (x - sum - t * r) * (1.00 / (double) s);
		//cerr << res << endl;
		for (int i = 0; i < n; i++)
			res += (e[i] - b[i]) * (1.00 / (s + w[i]));
		return res;
	}

	res = (x - sum) * (1.00 / (double (r)));
	//cerr << res << endl;
	int finished = 0;
	for (int i = 0; i < n; i++)
	{
		int begin = a[i].second.first;
		int end = a[i].second.second;
		int vel = a[i].first;

		if (equal (res, t) || res > t)
			finished = 1;

		if (finished)
			res += double(end - begin) / (double) (s + vel);
		else
		{
			double next = res + double(end - begin) / (double) (r + vel);
			//cerr << i << ' ' << next << endl;
			if (equal (next, t) || next > t)
			{
				finished = 1;
				double dis = end - begin - (r + vel) * (t - res);
				//cerr << "dis " << dis << endl;
				res += (t - res) + dis / double (s + vel);
			}
			else
				res = next;
		}
	}

	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		double res = solve();
		cout << fixed << setprecision (6) << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
