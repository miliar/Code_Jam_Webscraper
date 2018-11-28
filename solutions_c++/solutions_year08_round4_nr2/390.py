#include <iostream>
#include <vector>
#include <complex>
#include <cmath>

using namespace std;

typedef complex<double> tComp;

double area(const tComp& p1, const tComp& p2, const tComp& p3)
{
	double a = abs(p1 - p2);
	double b = abs(p2 - p3);
	double c = abs(p3 - p1);
	if (a == 0 || b == 0 || c == 0)
		return 0;
	return sqrt((a+b+c)*(a+b-c)*(b+c-a)*(a+c-b)) / 2;
}

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int mx, my, a;
		cin >> mx >> my >> a;
		bool done = false;
		for (int x=0; x<=mx; x++)
			for (int y=0; y<=my; y++)
			{
				tComp p1(x, 0);
				tComp p2(0, y);
				for (int x3=-(mx-x); x3<=mx && !done; x3++)
					for (int y3=-(my-y); y3<=my && !done; y3++)
					{
						tComp p3(x3, y3);
						if (fabs(area(p1, p2, p3) - a) < 1.0e-9)
						{
							double sx = min(real(p1), min(real(p2), real(p3)));
							if (sx > 0)
								sx = 0;
							double sy = min(imag(p1), min(imag(p2), imag(p3)));
							if (sy > 0)
								sy = 0;
							p1 += tComp(-sx, -sy);
							p2 += tComp(-sx, -sy);
							p3 += tComp(-sx, -sy);
							cout << "Case #" << kase << ":";
							cout << " " << (int)(real(p1)+0.5);
							cout << " " << (int)(imag(p1)+0.5);
							cout << " " << (int)(real(p2)+0.5);
							cout << " " << (int)(imag(p2)+0.5);
							cout << " " << (int)(real(p3)+0.5);
							cout << " " << (int)(imag(p3)+0.5);
							cout << endl;
							done = true;
						}
					}
			}
		if (!done)
			cout << "Case #" << kase << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
