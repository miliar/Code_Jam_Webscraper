#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
	
int w[600][600];
int dpx[600][600];
int dpy[600][600];
int mass[600][600];

int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
		
	int tests;
	inf >> tests;
	for (int test = 0; test < tests; test++)
	{	
		int r,c,d;
		inf >> r >> c >> d;
		for (int i = 0; i < r; i++)
		{
			string st;
			inf >> st;
			
			for (int j = 0; j < c; j++)			
				w[i][j] = st[j]- '0';
		}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)			
			{
				//dp[i][j] -- make
				if (i == 0 && j == 0)
				{
					dpx[i][j] = dpy[i][j] = 0;
					mass[i][j] = w[i][j];
					continue;
				}
				if (i == 0)
				{

					dpx[i][j] = dpx[i][j-1] + w[i][j]*(j);
					dpy[i][j] = 0;
					mass[i][j] = mass[i][j-1] + w[i][j];
					continue;
				}
				if (j == 0)
				{
					dpx[i][j] = 0;
					dpy[i][j] = dpy[i-1][j] + w[i][j]*(i);
					mass[i][j] = mass[i-1][j] + w[i][j];
					continue;
				}
				dpx[i][j] = dpx[i-1][j] + dpx[i][j-1] - dpx[i-1][j-1] + (j)*w[i][j];

				dpy[i][j] = dpy[i-1][j] + dpy[i][j-1] - dpy[i-1][j-1] + (i)*w[i][j];
				mass[i][j] = mass[i-1][j] + mass[i][j-1] - mass[i-1][j-1] + w[i][j];
			}
		int anw = -1;
		for (int k = min(c,r); k >=3; k--)
		{
			for (int i1 = 0; i1 + k-1 < r; i1++)
				for (int j1 = 0; j1 + k-1 < c; j1++)
				{
					//check square
					int i2 = i1 + k-1;
					int j2 = j1 + k-1;
					int bx = 0;
					int by = 0;
					int fm = mass[i2][j2];
					if (i1 >0 ) fm -= mass[i1-1][j2];
					if (j1 >0 ) fm -= mass[i2][j1-1];
					if (i1 > 0 && j1 > 0) fm += mass[i1-1][j1-1];
					fm -= w[i1][j1];
					fm -= w[i1][j2];
					fm -= w[i2][j1];
					fm -= w[i2][j2];
					bool flag = false;

					bx = dpx[i2][j2];
					if (i1 >0 ) bx -= dpx[i1-1][j2];
					if (j1 >0 ) bx -= dpx[i2][j1-1];
					if (i1 > 0 && j1 > 0) bx += dpx[i1-1][j1-1];
					bx -= (j1)*w[i1][j1];
					bx -= (j2)*w[i1][j2];
					bx -= (j1)*w[i2][j1];
					bx -= (j2)*w[i2][j2];	
					int nbx = (fm*(j1 + j2));
					int div = 2;
					if (bx * div == nbx)
						flag = true;

					//coppyy
					by = dpy[i2][j2];
					if (i1 >0 ) by -= dpy[i1-1][j2];
					if (j1 >0 ) by -= dpy[i2][j1-1];
					if (i1 > 0 && j1 > 0) by += dpy[i1-1][j1-1];
					by -= (i1)*w[i1][j1];
					by -= (i1)*w[i1][j2];
					by -= (i2)*w[i2][j1];
					by -= (i2)*w[i2][j2];	
					int nby = (fm*(i1 + i2));
					div = 2;
					if (by * div == nby)
						if (flag)
						{
							anw = k;
							goto eend;
						}
					
											


				}
		}
eend:
		if (anw == -1)		
			outf << "Case #" << test+1 << ": " << "IMPOSSIBLE" << endl;		
		else
			outf << "Case #" << test+1 << ": " << anw << endl;

	
	}

	outf.close();
	return 0;
}

