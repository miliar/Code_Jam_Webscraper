#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAX = 205;
const double eps = 1e-8;

int L[MAX][2], U[MAX][2], d[MAX];
double delta[MAX], s[MAX], r[MAX];

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  cout.setf(ios::fixed, ios::floatfield);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": " << endl;
		int w, l, u, g;
		cin >> w >> l >> u >> g;
		int pts = 0;
		for (int i = 0; i < l; i++)
		{
			cin >> L[i][0] >> L[i][1];
			d[pts++] = L[i][0];
		}
		for (int i = 0; i < u; i++)
		{
			cin >> U[i][0] >> U[i][1];
			d[pts++] = U[i][0];
		}
		sort(d,d+pts);
		double S = 0;
		double ly = L[0][1], uy = U[0][1];
		delta[0] = delta[1] = uy - ly;
		l = 1, u = 1;
		for (int i = 2; i < pts; i++)
		{
			if (d[i] == d[i-1]){
				delta[i] = delta[i-1];
				s[i] = 0;
				continue;
			}
			double cly, cuy;
			if (L[l][0] == d[i])
			{
				cly = L[l][1];
				l++;
			}
			else
			{
				cly = L[l-1][1] + double(L[l][1] - L[l-1][1]) / (L[l][0] - L[l-1][0]) * (d[i] - L[l-1][0]);
			}
			if (U[u][0] == d[i])
			{
				cuy = U[u][1];
				u++;
			}
			else
			{
				cuy = U[u-1][1] + double(U[u][1] - U[u-1][1]) / (U[u][0] - U[u-1][0]) * (d[i] - U[u-1][0]);
			}
			delta[i] = cuy - cly;
			s[i] = ((delta[i] + delta[i-1]) * (d[i] - d[i-1]))/2;
			r[i] = (delta[i] - delta[i-1]) / (d[i] - d[i-1]);
//			cerr << delta[i-1] << ' ' << delta[i] << ' ' << s[i] << " " << r[i] << endl;
			S += s[i];
		}
		double g0 = S / g;
		double cg = g0;
		for (int i = 2; i < pts; i++)
		{
			while (cg < s[i] - eps)
			{
				double cur;
				if (abs(r[i]) < eps)
				{
				   cur = cg / delta[i-1];
				}
				else
				{
					double D = delta[i-1] * delta[i-1] + 2 * cg * r[i];
					if (D < eps) D = 0;
					cur = (sqrt(D) - delta[i-1]) / r[i];
				}
				cout << cur + d[i-1] << endl;
				cg += g0;
			}
			cg -= s[i];
		}
  }
  return 0;
}