#include <iostream>
#include <cstdio>
#include <complex>

using namespace std;

typedef complex<double> pnt;
#define X real()
#define Y imag()

const int MAXR = 1000;

typedef long long ll;

struct fen
{
	double t[MAXR][MAXR];
	double sum(int x, int y)
	{
		double ss = 0;
		while(x > 0)
		{
			int y1 = y;
			while(y1 > 0)
			{
				ss += t[x][y1];
				y1 -= (y1 & -y1);
			}
			x -= (x & -x);
		}
		return ss;
	}
	double rsum(int x, int y, int k)
	{
		return sum(x+k-1, y+k-1) - sum(x-1, y+k-1) - sum(x+k-1, y-1) + sum(x-1, y-1);
	}
	double fsum(int x, int y, int k)
	{
		return rsum(x, y, k) - rsum(x, y, 1) - rsum(x+k-1, y, 1) - rsum(x, y+k-1, 1) - rsum(x+k-1, y+k-1, 1);
	}
	void update(int x, int y, double v)
	{
		while (x <= MAXR)
		{
			int y1 = y;
			while (y1 <= MAXR)
			{
				t[x][y1] += v;
				y1 += (y1 & -y1); 
			}
			x += (x & -x); 
		}
	}
	void init()
	{
		for(int i=0; i<MAXR; i++)
			for(int j=0; j<MAXR; j++)
				t[i][j] = 0;
	}
} m, x, y;

int main()
{
	int TC;
	cin >> TC;
	for(int T=1; T<=TC; T++)
	{
		m.init();
		x.init();
		y.init();

		int r, c, d;
		cin >> r >> c >> d;
		for(int i=1; i<=r; i++)
			for(int j=1; j<=c; j++)
			{
				char c;
				cin >> c;
				int mm = c - '0' + d;
				m.update(i, j, mm);
				x.update(i, j, mm * (i + .5));
				y.update(i, j, mm * (j + .5));
			}
		
		int fnd = 0;
		for(int k=min(r, c); k>=3; k--)
			for(int i=1; i+k<=r+1; i++)
				for(int j=1; j+k<=c+1; j++)
				{
					pnt dd = pnt(x.fsum(i, j, k), y.fsum(i, j, k)) / m.fsum(i, j, k);
					if(abs(dd - (pnt(i, j) + pnt(i+k, j+k))/2.0) < 1e-12)
					{
						fnd = k;
						goto hell;
					}
				}
hell:
		cout << "Case #" << T << ": ";
		if(fnd)
			cout << fnd;
		else
			cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}

