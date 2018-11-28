#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "A-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		vector<string> gf(4);
		for(int i = 0; i < 4; ++i)
			cin >> gf[i];
		
		int res = 0;
		for(int i = 0; i < 4 && res <= 0; ++i)
		{
			bool xh = true;
			bool xv = true;
			bool yh = true;
			bool yv = true;
			for(int j = 0; j < 4 && res <= 0; ++j)
			{
				if(gf[i][j] == '.')
				{
					xh = yh = false;
					res = -1;
				}
				else if(gf[i][j] == 'O')
					xh = false;
				else if(gf[i][j] == 'X')
					yh = false;

				if(gf[j][i] == '.')
				{
					xv = yv = false;
					res = -1;
				}
				else if(gf[j][i] == 'O')
					xv = false;
				else if(gf[j][i] == 'X')
					yv = false;
			}
			if(xh || xv)
				res = 1;
			else if(yh || yv)
				res = 2;
		}
		bool xd = true, yd = true, xd2 = true, yd2 = true;;
		for(int i = 0; i < 4 && res <= 0; ++i)
		{
			if(gf[i][i] == '.')
			{
				xd = yd = false;
				res = -1;
			}
			else if(gf[i][i] == 'X')
				yd = false;
			else if(gf[i][i] == 'O')
				xd = false;
		
			if(gf[i][3-i] == '.')
			{
				xd2 = yd2 = false;
				res = -1;
			}
			else if(gf[i][3-i] == 'X')
				yd2 = false;
			else if(gf[i][3-i] == 'O')
				xd2 = false;
		}
		if(res <= 0)
			if(xd || xd2)
				res = 1;
			else if(yd || yd2)
				res = 2;
		cout << "Case #" << Case << ": ";
		if(res == 0)
			cout << "Draw" << endl;
		else if(res == 1)
			cout << "X won" << endl;
		else if(res == 2)
			cout << "O won" << endl;
		else
			cout << "Game has not completed" << endl;
	}

	return 0;
}
