#include <iostream>
#include <cmath>

#define taskId "B"

using namespace std;

int x[1000], y[1000], z[1000], xv[1000], yv[1000], zv[1000]; 

double sqr(double a)
{
	return a * a;
}

int main (int argc, char * const argv[])
{
	freopen(taskId"-large.in","r",stdin);
	freopen(taskId"-large.out","w",stdout);
	
	int _T;
	cin >> _T;
	
	cout.setf(ios::fixed);
	cout.precision(8);
	
	
	for (int T = 0; T<_T; T++)
	{
		int n;
		cin >> n;
		
		for (int i = 0; i < n; i++)
		{
			cin >> x[i] >> y[i] >> z[i] >> xv[i] >> yv[i] >> zv[i];
		}
		
		long long X = 0,
				  Y = 0,
				  Z = 0,
				  XV = 0,
				  YV = 0,
				  ZV = 0;
		
		for (int i = 0; i < n; i++)
		{
			X += x[i];
			Y += y[i];
			Z += z[i];
			XV += xv[i];
			YV += yv[i];
			ZV += zv[i];
		}
		
		long double t = -1;
		
		if ((XV * XV + YV * YV + ZV * ZV) == 0)
		{
			t = 0;
		}
		else
		{
			t *= (X * XV + Y * YV + Z * ZV);
			t /= (XV * XV + YV * YV + ZV *ZV);
		}
		
		t = max(t, (long double)0.0);
		
		double d1 = sqrt(sqr((X + XV * t) / n) + sqr((Y + YV * t) / n) + sqr((Z + ZV * t) / n));
		double d2 = sqrt(sqr((X + XV * 0.0) / n) + sqr((Y + YV * 0.0) / n) + sqr((Z + ZV * 0.0) / n));
		
		if (d2 < d1)
		{
			cout << "Case " << "#" << T + 1 << ": " << d2 << ' ' << 0.0 << '\n';
		}
		else
		{
			cout << "Case " << "#" << T + 1 << ": " << d1 << ' ' << t << '\n';
		}
	}

	
    return 0;
}
