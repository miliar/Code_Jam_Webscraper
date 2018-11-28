#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

const int nn = 128;
const double eps = 1e-8;

int test;

double x[nn], y[nn], r[nn];
int n;

ll ALL;

ll MS[nn][nn][2];

double sqr(double x) { return x*x; }

ll calc(double X, double Y, double R)
{
	ll msk = 0;
	for (int i = 0; i < n; i++)
	{
		double d = hypot(X - x[i], Y - y[i]) + r[i];
		if (d <= R + eps)
		{
			msk += 1LL << i;
		}
	}
	return msk;
}

bool check(double R)
{
	ALL = 1LL << n; ALL--;
	
	memset(MS, 0, sizeof MS);

	for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) 
		if (i != j)
		{
			double D = hypot(x[i] - x[j], y[i] - y[j]) + r[i] + r[j];
			if (D >= 2*R - eps) 
			{
				MS[i][j][0] = calc(x[i], y[i], R);
				MS[i][j][1] = calc(x[j], y[j], R);
				continue;
			}
			double a = D - r[i] - r[j];
			double b = R - r[i];
			double c = R - r[j];
			double ca = (sqr(a) + sqr(b) - sqr(c)) / 2 / a / b;
			if (ca > 1) ca = 1; if (ca < -1) ca = -1;
			double al = acos(ca);
			double xx = x[j] - x[i];
			double yy = y[j] - y[i];
			
			double dd = hypot(xx, yy) / (R - r[i]);
			xx /= dd;
			yy /= dd;

			double X = xx*cos(al) - yy*sin(al);
			double Y = xx*sin(al) + yy*cos(al);

			MS[i][j][0] = calc(X + x[i], Y + y[i], R);

			al = -al;
			X = xx*cos(al) - yy*sin(al);
			Y = xx*sin(al) + yy*cos(al);
			MS[i][j][1] = calc(X + x[i], Y + y[i], R);
		}
		else
		{
			MS[i][j][0] = calc(x[i], y[i], R);
			MS[i][j][1] = calc(x[j], y[j], R);
		}

	for (int i = 0; i < n; i++) for (int j = i; j < n; j++) for (int k = 0; k < 2; k++)
	for (int i1 = 0; i1 < n; i1++) for (int j1 = i1; j1 < n; j1++) for (int k1 = 0; k1 < 2; k1++)
	{
		ll M1 = MS[i][j][k];
		ll M2 = MS[i1][j1][k1];
		if ((M1 | M2) == ALL) return true;
	}
	return false;
}

void solve()
{
	double ans = 0;
	
	double l = 0;
	double r = 5000;
	
	cin >> n;
	for (int i = 0; i < n; i++) cin >> x[i] >> y[i] >> ::r[i];

	for (int i = 0; i < 35; i++)
	{
		double m = (l + r) / 2;
		if (check(m)) r = m; else l = m;
	}
	
	ans = (r + l) / 2;

	cout.precision(6);
	cerr.precision(6);
	cout << fixed;
	cerr << fixed;
	cout << "Case #" << ++test << ": " << ans << endl;
	cerr << "Case #" << test << ": " << ans << endl;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int t;
	cin >> t;
	while (t--)
	solve();
	fclose(stdout);
	return 0;
}