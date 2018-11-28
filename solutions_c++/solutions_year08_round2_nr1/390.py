// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <hash_map>
#include <map>
#include <string>
#include <algorithm>

using namespace std;


long long calc_comb(long long a) {
	return a*(a-1)*(a-2)/6;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;

	for(int t=0; t<T; t++)
	{
		int n;
		int A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long x, y;
		x = x0; y = y0;
		int mx[3][3];
		for(int i=0; i<3; i++)
			for(int j=0; j<3; j++)
				mx[i][j] = 0;

		for (int i=1; i<=n; i++)
		{
			cerr << "(" << x <<","<<y<<") ";
			mx[x%3][y%3]++;
			x = (A * x + B) % M;
			y = (C * y + D) % M;
		}

		cerr << endl;

		for(int i=0; i<3; i++)
		{
			for(int j=0; j<3; j++)
				cerr<<mx[i][j]<<" ";
			cerr<<endl;
		}

		long long res = 0;
		for(int i=0; i<3; i++)
		{
			res += (long long)mx[i][0] * mx[i][1] * mx[i][2];
			res += (long long)mx[0][i] * mx[1][i] * mx[2][i];
	
			res += (long long)mx[0][i] * mx[1][(i+1)%3] * mx[2][(i+2)%3];
			res += (long long)mx[0][i] * mx[1][(i+2)%3] * mx[2][(i+1)%3];
			for(int j=0; j<3; j++)
				res += calc_comb(mx[i][j]);
		}

		cout << "Case #" << t+1 <<": " << res << endl;
	}

	return 0;
}

