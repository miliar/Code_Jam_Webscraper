#include <iostream>
#include <cmath>
using namespace std;

class TaskC
{
	const double pi;
	double f, R, t, r, g;
	double area0(double a)  { return 0.5*(a-sin(a)*cos(a)); }
	double area(double x1, double x2, double y1, double y2)
	{
		if (x1>x2 || y1>y2 || x1*x1+y1*y1>1.0)  return 0.0;
		x2 = min(x2, sqrt(1-y1*y1));
		y2 = min(y2, sqrt(1-x1*x1));
		double x = min(x2, sqrt(1-y2*y2));
		return (x-x1)*y2 + area0(acos(x))-area0(acos(x2)) - (x2-x1)*y1;
	}
public:
	TaskC() : pi(2.0*acos(0.0)) {}
	void ReadData()
	{
		cin >> f >> R >> t >> r >> g;
	}
	void Solve(int nCase)
	{
		ReadData();

		double s = 0.0;
		double R0 = R-t-f;
		if (R0>0)
		{
			f /= R0;  R /= R0;  t /= R0;  r /= R0;  g /= R0;
			for (double x=0; x<1.0; x += g+2*r)
			for (double y=0; y<1.0; y += g+2*r)
				s += area(x+r+f, x+r+g-f, y+r+f, y+r+g-f);
		}
		cout << "Case #" << nCase << ": " << 1.0-4*s/(pi*R*R) << endl;
	}
};

int main()
{
	int N;  cin >> N;
	TaskC sol;  for (int i=1; i<=N; ++i)  sol.Solve(i);
	return 0;
}