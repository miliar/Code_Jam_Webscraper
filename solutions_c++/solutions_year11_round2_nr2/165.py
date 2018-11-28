#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

const long double eps = 1e-9;

vector <int> x;
vector <long double> h;
int n;
long double d;

void Load()
{
	cin >> n >> d;
	x.resize(n);
	h.resize(n);
	int i;
	for (i = 0; i < n; i++) {
		cin >> x[i] >> h[i];
	}

}
                                         
bool Can(long double t) 
{
	long double p = -1e60;
	int i;
	for (i = 0; i < n; i++) {
		long double x0, x1;
		x0 = max(x[i] - t, p + d);
		x1 = x0 + ((long double)h[i]-1)*d;
		if(fabs(x1-x[i]) > t || fabs(x0-x[i]) > t) return false;
		p = x1;
	}
	return true;

}


void Solve()
{
	long double l = 0;
	long double r = 1;
	while (!Can(r)) r *= 2;
	int i;
	for (i = 0; i < 300; i++) {
		long double m = (l+r) / 2;
		if (Can(m)) {
			r = m;
		} else {
			l = m;
		}
	}
	cout.precision(12);
	cout.setf(ios::fixed|ios::showpoint);
	cout << r << "\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
