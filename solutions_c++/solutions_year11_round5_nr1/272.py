#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <map>
#include <utility>
#include <iomanip>

using namespace std;

int T;
int W, L, U, G;
double LL[1001];
double UU[1001];
int tmpx, tmpy;
int oldx, oldy;
int ix;
double iy;
double prevy;
double sz, sz_per_g;
double ans[101];
double eps = 1e-7;
double tmpsz;
double calculate(int i, double pos)
{
	double u = (UU[i+1] - UU[i]) - (LL[i+1] - LL [i]);
	double bot = (UU[i] - LL[i]) + u*pos;
	return ((UU[i] - LL [i]) + bot) /2 * pos;
}
int main()
{
	ifstream fin ("A.in");
	ofstream fout ("A.out");
	fin >> T;
	for (int t = 0 ; t < T; t++)
	{
		fout << "Case #" << t+1 << ": " << endl;
		fin >> W >> L >> U >> G;
		fin >> oldx >> oldy;
		ix = oldx; LL[ix] = oldy; ix++;
		prevy = oldy;
		for (int l = 0 ; l < L-1 ; l++)
		{
			fin >> tmpx >> tmpy;
			iy = (double)tmpy - (double)oldy;
			iy = iy / (tmpx - oldx);
			while (ix <= tmpx)
			{
				LL[ix] = prevy + iy;
				prevy += iy;
				ix++;
			}
			oldx = tmpx;
			oldy = tmpy;
		}
		fin >> oldx >> oldy;
		ix = oldx; UU[ix] = oldy; ix++; prevy = oldy;
		for (int l = 0 ; l < U-1 ; l++)
		{
			fin >> tmpx >> tmpy;
			iy = (double)tmpy - (double)oldy;
			iy = iy / (tmpx - oldx);
			while (ix <= tmpx)
			{
				UU[ix] = prevy + iy;
				prevy += iy;
				ix++;
			}
			oldx = tmpx;
			oldy = tmpy;
		}
		sz = 0;
		for (int i = 0 ; i < W ; i++)
		{
			sz += ((UU[i] - LL[i]) + (UU[i+1] - LL [i+1]))/2;
		}
		sz_per_g = sz / G;
		tmpsz = 0;
		for (int i = 0 ; i < W - 1; i ++)
		{
			tmpsz += ((UU[i] - LL[i]) + (UU[i+1] - LL [i+1]))/2;
			if (tmpsz <= sz_per_g) continue;
			else
			{
				tmpsz -= ((UU[i] - LL[i]) + (UU[i+1] - LL [i+1]))/2;
				double ii = 0.25;
				double pos = 0.5;
				while (abs(tmpsz + calculate(i , pos) - sz_per_g ) > eps)
				{
					if (tmpsz + calculate(i , pos) > sz_per_g)
					{
						pos -= ii;
						ii /=2;
					}
					else
					{
						pos += ii;
						ii /=2;
					}
				}
				fout << setprecision (8) << i + pos << endl;
				tmpsz = calculate(i , 1) - calculate(i , pos);
			}
		}
	}
}