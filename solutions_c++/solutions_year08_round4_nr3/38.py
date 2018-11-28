#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int xx = 1; xx <= t; ++xx) {
	double a = 0., b = 1.e12;
	int n;
	cin >> n;
	vector<double> x(n), y(n), z(n), p(n);
	for (int i = 0; i < n; ++i)
	    cin >> x[i] >> y[i] >> z[i] >> p[i];
	while (b - a > 1e-7) {
	    double yy = (a + b)*.5;
	    double s[2][2][2];
	    for (int u = 0; u < 2; ++u)
		for (int v = 0; v < 2; ++v)
		    for (int w = 0; w < 2; ++w)
			s[u][v][w] = 1e15;
	    for (int i = 0; i < n; ++i)
		for (int u = 0; u < 2; ++u)
		    for (int v = 0; v < 2; ++v)
			for (int w = 0; w < 2; ++w)
			    s[u][v][w] = min(s[u][v][w], yy*p[i] +
					     (u ? x[i] : -x[i]) +
					     (v ? y[i] : -y[i]) +
					     (w ? z[i] : -z[i]));
	    double d = 0., e = 0.;
	    for (int u = 0; u < 2; ++u)
		for (int v = 0; v < 2; ++v) {
		    if (s[u][v][u^v] + s[!u][!v][!(u^v)] < 0)
			goto bad;
		    d += s[u][v][u^v]; e += s[!u][!v][!(u^v)];
		}
	    if (d < 0 || e < 0)
		goto bad;
	    b = yy;
	    continue;
	bad:
	    a = yy;
	}
	cout << "Case #" << xx << ": ";
	cout.flags(ios::fixed);
	cout.precision(6);
	cout << (a + b)*.5 << endl;
    }
}

