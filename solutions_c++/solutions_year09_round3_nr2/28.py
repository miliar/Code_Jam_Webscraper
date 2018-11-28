#include <iostream>
#include <cmath>

using namespace std;

int test;

const int nn = 512;
long long x[nn][3], vx[nn][3];
long long X[3], VX[3];
int n;

void solve()
{
	double d = 1e100;
	double t = 0;
	cin >> n;
	for (int i = 0; i < 3; i++) X[i] = VX[i] = 0;
	
	for (int i = 0; i < n; i++) 
	{
		for (int j = 0; j < 3; j++) { cin >> x[i][j]; X[j] += x[i][j]; }
		for (int j = 0; j < 3; j++) { cin >> vx[i][j]; VX[j] += vx[i][j]; }
	}
	
	cerr << X[0] << ' ' << X[1] << ' ' << X[2] << ' ' << VX[0] << ' ' << VX[1] << ' ' << VX[2] << endl;
	
	long long A = 0, B = 0, C = 0;
	C = X[0]*X[0] + X[1]*X[1] + X[2]*X[2];
	B = X[0]*VX[0] + X[1]*VX[1] + X[2]*VX[2];
	A = VX[0]*VX[0] + VX[1]*VX[1] + VX[2]*VX[2];
	
	cerr << A << ' ' << B << ' ' << C << endl;
	
	if (A != 0)
	{
		if (B < 0)
		{
			t = -(double)B / A;
			d = ((double)C*A - (double)B*B) / A;
		}
		else
		{
			d = C;
			t = 0;
		}
	}
	else
	{
		d = C;
		t = 0;
	}
		
	cerr << d << endl;
	d = sqrt(d);
	d /= n;
	
	printf("Case #%d: %.8lf %.8lf\n", ++test, d, t);
}

int main()
{
	int t;
	cin >> t;
	while (t--)
	solve();
	return 0;
}