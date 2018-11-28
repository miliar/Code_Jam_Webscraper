#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <assert.h>

using namespace std;

long long calc(int n, int A, int B, int C, int D, int x0, int y0, int M)
{
	long long mods[3][3] = {0};
	long long x = x0;
	long long y = y0;
	mods[x%3][y%3]++;
	for (int i=1; i<n; ++i)
	{
		x = (A*x+B) % M;
		y = (C*y+D) % M;
		assert(x>=0 && y>=0);
		mods[x%3][y%3]++;
	}
	long long res = 0;
	/*for (int i=0; i<3; ++i)
	{
		for (int j=0; j<3; ++j)
			cout << mods[i][j] << " ";
		cout << endl;
	}*/
	for (int x1=0; x1<3; ++x1)
	for (int y1=0; y1<3; ++y1)
		for (int x2=0; x2<3; ++x2)
		for (int y2=0; y2<3; ++y2)
			for (int x3=0; x3<3; ++x3)
			for (int y3=0; y3<3; ++y3)
			{
				if (((x1+x2+x3) % 3==0) && ((y1+y2+y3) % 3==0))
				{
					if (x1==x2 && y1==y2 && x1==x3 && y1==y3)
						res += mods[x1][y1]*(mods[x1][y1]-1)*(mods[x1][y1]-2)/6*6;
					else if (x1==x2 && y1==y2)
						res += mods[x1][y1]*(mods[x1][y1]-1)/2 * mods[x3][y3]*2;
					else if (x1==x3 && y1==y3)
						res += mods[x1][y1]*(mods[x1][y1]-1)/2 * mods[x2][y2]*2;
					else if (x3==x2 && y3==y2)
						res += mods[x3][y3]*(mods[x3][y3]-1)/2 * mods[x1][y1]*2;
					else
						res += mods[x1][y1] * mods[x2][y2] * mods[x3][y3];
					/*if (mods[x1][y1] * mods[x2][y2] * mods[x3][y3]>0)
					{
					cout << x1 << " " << y1 << ", ";
					cout << x2 << " " << y2 << ", ";
					cout << x3 << " " << y3 << endl;
					}*/
				}
			}
	return res/6;
}

int main(int argc, char *argv[])
{
	if (argc<2)
	{
		cout << "Filename needed\n";
		return -1;
	}
	fstream fin(argv[1]);
	int numcases;
	fin >> numcases;
	for (int i=0; i<numcases; ++i)
	{
		int n,A,B,C,D,x0,y0,M;
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		cout << "Case #" << i+1 << ": " << calc(n,A,B,C,D,x0,y0,M) << endl;
	}
	fin.close();
	return 0;
}