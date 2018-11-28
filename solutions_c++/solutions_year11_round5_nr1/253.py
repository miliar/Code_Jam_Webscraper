#include <iostream>
#include <cstdio>
#include <iomanip>
#include <complex>
#include <deque>
#include <cmath>

using namespace std;

typedef complex<double> pnt;
#define X real()
#define Y imag()

const double eps = 1e-12;

deque<pnt> pl, pu;
double Gy(deque<pnt>& p, double x)
{
	for(int i=0; i<p.size(); i++)
		if(abs(p[i].X - x) < eps)
			return p[i].Y;
		else if(p[i].X > x)
			return (p[i].Y - p[i-1].Y)/(p[i].X - p[i-1].X)*(x - p[i-1].X) + p[i-1].Y;
}
double Sx(double ox, double nx)
{
	double oly, nly, ouy, nuy;
	oly = Gy(pl, ox);
	nly = Gy(pl, nx);
	ouy = Gy(pu, ox);
	nuy = Gy(pu, nx);
	return ((nuy - nly) + (ouy - oly))/2 * (nx - ox);
}

int main()
{
	cout << fixed << setprecision(8);
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		cout << "Case #" << T << ":" << endl;

		int w, l, u, g;
		cin >> w >> l >> u >> g;


		pl.resize(l);
		pu.resize(u);
		for(int i=0; i<l; i++)
			cin >> pl[i].X >> pl[i].Y;
		for(int i=0; i<u; i++)
			cin >> pu[i].X >> pu[i].Y;

		double ar = 0;

		double ox ;
		int p1, p2;

		ox = 0;
		p1 = p2 = 1;
		while(p1 != l || p2 != u)
		{
			double nx;
			if(p1 == l || pu[p2].X < pl[p1].X)
				nx = pu[p2++].X;
			else
				nx = pl[p1++].X;
			if(nx - ox < eps)
				continue ;
			ar += Sx(ox, nx);
			ox = nx;
		}
		ar /= g;

		ox = 0;
		p1 = p2 = 1;
		double rm = 0;
		while(p1 != l || p2 != u)
		{
			double nx;
			if(p1 == l || pu[p2].X < pl[p1].X)
				nx = pu[p2++].X;
			else
				nx = pl[p1++].X;
			bb:;
			if(abs(nx - ox) < 1e-2)
				continue ;
			if(rm + Sx(ox, nx) >= ar)
			{
				double dd = ar - rm;
				double lb = ox, ub = nx;
				while(ub - lb > eps)
				{
					double md = (lb + ub) / 2;
					if(Sx(ox, md) < dd)
						lb = md;
					else
						ub = md;
				}
				ox = (ub + lb) / 2;
				cout << ox << endl;
				rm = 0;
				g--;
				if(g == 1)
					break;
				goto bb;
			}
			else
				rm += Sx(ox, nx);
			ox = nx;
		}

	}
	return 0;
}

