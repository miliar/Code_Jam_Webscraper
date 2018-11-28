#include <iostream>
#include <iomanip>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define double long double

typedef double answer_type;



answer_type solve()
{
	int n;
	double D;
	cin >> n >> D;
	map<double, int> M;
	double x;
	int q;
	double a = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> x >> q;
		M[x] = q;
		a = max(a, D * (q - 1) / 2);
	}
	double b = 1e19;
	const double EPS = 1e-7;
	while (b - a > EPS)
	{
		double t = (a + b) / 2;
		double INF = 1e40;
		double l = -INF;
		bool good = 1;
		for (auto it = M.begin(); it != M.end(); it++)
		{
			x = it->first;
			q = it->second;
			double rl = x - t;
			double pos = max(rl, l);
			double right = pos + D * (q - 1);
			if (fabs(right - x) > t + EPS)
			{
				good = false;
				break;
			}
			l = right + D;
		}
		if (good)
			b = t;
		else
			a = t;
	}
	return (a + b) / 2;
}

int main()
{
	int T;
	cin >> T;
	cout << fixed << setprecision(10);
	cerr << fixed << setprecision(10);
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
