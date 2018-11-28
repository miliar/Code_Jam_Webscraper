#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

const double Pi = 3.14159265359;
double R;

double corner(double x, double y)
{
	if(x * x + y * y > R * R) return 0;
	double x1 = sqrt(R * R - y * y), y1 = sqrt(R * R - x * x), a = x1 - x, b = y1 - y;
	return R * R * asin(sqrt(a * a + b * b) / 2 / R) - (a * y + b * x) / 2;
}

int main()
{
	ifstream f("C.in");
	ofstream ff("C.out");
	int N, Ni, i;
	double fcon, Rcon, tcon, rcon, gcon, r, g;

	f >> N;

	for(Ni = 1; Ni <= N; ++Ni)
	{
		double S = 0, x, y, a, b;

		f >> fcon >> Rcon >> tcon >> rcon >> gcon;
		R = Rcon - tcon - fcon;
		r = rcon + fcon;
		g = gcon - 2 * fcon;
		if((R <= 0) || (g <= 0))
		{
			ff << "Case #" << Ni << ": " << "1.000000" << endl;
			continue;
		}
		x = r;

		while(x < R)
		{
			y = r;
			while(y < R)
			{
				if((a = x + g) * a + (b = y + g) * b <= R * R) S += g * g;
				else
					if(((a = x + g) * a + (b = y) * b <= R * R) && ((a = x) * a + (b = y + g) * b <= R * R))
					{
						a = sqrt(R * R - (a = y + g) * a);
						b = sqrt(R * R - (b = x + g) * b);
						S += g * (b - y) + (y + g - b) * (a - x) + corner(a, b);
					}
					else
						if((a = x + g) * a + (b = y) * b <= R * R) 
						{
							a = sqrt(R * R - (a = x + g) * a);
							S += g * (a - y) + corner(x, a);
						}
						else
							if((a = x) * a + (b = y + g) * b <= R * R) 
							{
								a = sqrt(R * R - (a = y + g) * a);
								S += g * (a - x) + corner(a, y);
							}
							else S += corner(x, y);
							y += g + 2 * r;
			}
			x += g + 2 * r;
		}

		S *= 4;

		double o = 1 - S / Pi / Rcon / Rcon;
		
		ff << "Case #" << Ni << ": " << (int)o << ".";
		for(i = 0; i < 6; ++i)
		{
			o -= (int)o;
			o *= 10;
			ff << (int)o;
		}
		ff << endl;
	}

	return 0;
}