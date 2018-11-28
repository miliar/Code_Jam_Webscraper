#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

const int MAX_N = 4;

long x[MAX_N], y[MAX_N], r[MAX_N];
int n;

void enter()
{
	cin >> n;
	for (int i = 1; i <= n; ++i)
		cin >> x[i] >> y[i] >> r[i];
}

long dis(int i, int j)
{
	return (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]);
}

void solve()
{
	if (n == 1)
		cout << setprecision(6) << fixed << r[1]*1.0 << endl;
	else
		if (n == 2)
			cout << setprecision(6) << fixed << max(r[1], r[2])*1.0 << endl;
		else
		{
			long dd;
			double r0;
			double res;
			
			// 1, 2;
			dd = dis(1, 2);
			r0 = (sqrt(dd*1.0) + r[1] + r[2]) / 2;
			r0 = max(r0, r[3]*1.0);
			res = r0;
			
			// 2, 3;
			dd = dis(2, 3);
			r0 = (sqrt(dd*1.0) + r[2] + r[3]) / 2;
			r0 = max(r0, r[1]*1.0);
			if (res > r0) res = r0;
			
			// 1, 3;
			dd = dis(1, 3);
			r0 = (sqrt(dd*1.0) + r[1] + r[3]) / 2;
			r0 = max(r0, r[2]*1.0);
			if (res > r0) res = r0;
			
			cout << setprecision(6) << fixed << res << endl;
		}
}

int main()
{
	int T;
	cin >> T;
	for (int run = 1; run <= T; ++run)
	{
		enter();
		
		cout << "Case #" << run << ": ";
		solve();

		
	}
	
	
	return 0;
}
