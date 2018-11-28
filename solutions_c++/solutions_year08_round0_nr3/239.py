#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <vector>
using namespace std;

const long double eps = 1e-10;
const long double PI = 3.1415926535897932384626433832795;

inline long double square(long double a)
{
	return a * a;
}

long double R, r, t, g, f;

void Load()
{
	cin >> f >> R >> t >> r >> g;
}

long double GetSquare(vector<pair<long double, long double> > &p)
{
	int i;
	/*cerr << "Getting square of such thing:\n";
	for (i = 0; i < p.size(); i++)
	{
		cerr << p[i].first << " " << p[i].second << "\n";
	}*/
	long double res = 0;
	for (i = 0; i < p.size() - 1; i++)
	{
		long double v = p[i].first * p[i + 1].second - p[i + 1].first * p[i].second;
		res += v;
	}
	//cerr << "resulted in  " << fabs(res) / 2 << "\n";
	return fabs(res) / 2;
}

long double Intersect(long double x1, long double y1, long double x2, long double y2, long double r)
{
	if (fabs(x1 - x2) < eps)
	{
		long double t = r * r - x1 * x1;
		if (t < -eps) return 1e100;
		t = sqrt(fabs(t));
		t = (t - y1) / (y2 - y1); 
		if (! (t < 1 + eps)) return 1e100;
		return t;
	}
	else
	{
		long double t = r * r - y1 * y1;
		if (t < -eps) return 1e100;
		t = sqrt(fabs(t));
		t = (t - x1) / (x2 - x1); 
		if (! (t < 1 + eps)) return 1e100;
		return t;
	}
}

void Solve()
{
	cout.setf(ios::fixed | ios::showpoint);
	cout.precision(10);
	if (g / 2 < f) 
	{
		cout << "1.0000000000";
		return;
	}
	if (R - t - f < -eps)
	{
		cout << "1.0000000000";
		return;
	}
	long double sqr = 0;
	long double cx, cy;
	cx = r + f;
	//cerr << "begcx = " << cx << "\n";
	while (cx < (R - t - f))
	{
		cy = r + f;
		while (cy < (R - t - f))
		{
			long double rx, ry;
			rx = cx + g - 2 * f;
			ry = cy + g - 2 * f;
			if (cx * cx + cy * cy > (R - t - f) * (R - t - f)) break;
			//cerr << "processing rectangle " << cx << " " << cy << " " << rx << " " << ry << "\n";
			vector<pair<long double, long double> > cp1, cp2;
			cp1.push_back(make_pair(cx, cy));
            long double ct = Intersect(cx, cy, rx, cy, R - t - f);
			if (ct > 1e50)
			{
				cp1.push_back(make_pair(rx, cy));
				ct = Intersect(rx, cy, rx, ry, R - t - f);
				if (ct > 1e50) cp1.push_back(make_pair(rx, ry));
				else cp1.push_back(make_pair(rx, cy + (ry - cy) * ct));
			}
			else
			{
				cp1.push_back(make_pair(cx + (rx - cx) * ct, cy));
			}
			cp2.push_back(make_pair(cx, cy));
            ct = Intersect(cx, cy, cx, ry, R - t - f);
			if (ct > 1e50)
			{
				cp2.push_back(make_pair(cx, ry));
				ct = Intersect(cx, ry, rx, ry, R - t - f);
				if (ct > 1e50) cp2.push_back(make_pair(rx, ry));
				else cp2.push_back(make_pair(cx + (rx - cx) * ct, ry));
			}
			else
			{
				cp2.push_back(make_pair(cx, cy + (ry - cy) * ct));
			}
			long double l = sqrt(square(cp1[cp1.size() - 1].first - cp2[cp2.size() - 1].first) + 
								 square(cp1[cp1.size() - 1].second - cp2[cp2.size() - 1].second));
		   	//cerr << "got l = " << l << "\n";
			if (fabs(l) > eps)
			{
				long double v, s;
				v = cp1[cp1.size() - 1].first * cp2[cp2.size() - 1].second - cp2[cp2.size() - 1].first * cp1[cp1.size() - 1].second;
				s = cp1[cp1.size() - 1].first * cp2[cp2.size() - 1].first + cp1[cp1.size() - 1].second * cp2[cp2.size() - 1].second;
				long double cang = atan2(v, s);
				/*cerr << "cang = " << cang << "\n";
				cerr << "v = " << v << "\n";
				cerr << "square adding is: " << fabs(cang) * (R - t - f) * (R - t - f) / 2 - fabs(v) / 2 << "\n";*/
				sqr += fabs(cang) * (R - t - f) * (R - t - f) / 2 - fabs(v) / 2;
			}
			reverse(cp2.begin(), cp2.end());
			int i;
			for (i = 0; i < cp2.size(); i++) cp1.push_back(cp2[i]);
			sqr += GetSquare(cp1);

			cy += g + 2 * r;
		}
		cx += g + 2 * r;
	}
	/*cerr << "Total sqr = " << sqr << "\n";
	cerr << "Square of all is " << PI * R * R / 4.0 << "\n";*/
	long double p = 1 - sqr / (PI * R * R / 4.0);
	cout << p;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
		cerr << "case " << it + 1 << " of " << nt << "\n";
	}
	return 0;
}