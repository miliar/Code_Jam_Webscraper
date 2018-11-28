#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>

using namespace std;

int squ(int x1, int y1, int x2, int y2, int x3, int y3) {
	x2 -= x1;
	x3 -= x1;
	x1 = 0;
	y2 -= y1;
	y3 -= y1;
	y1 = 0;
	return abs(x2 * y3 - x3 * y2);
}

int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);
     int test;
     cin >> test;
     for (int tt = 0; tt < test; ++tt) {
		int n, m, a;
		cin >> n >> m >> a;
		cout << "Case #" << tt+1 <<": ";
		//if (n * m < a)
	//		cout << "IMPOSSIBLE\n";
	//	else {
			bool f = true, h = false;
			int i, j, ii, jj;
			for ( i = 0; f && i <= n; ++i)
				for ( j = 0; f && j <= m; ++j)
					for ( ii = 0; f && ii <= n; ++ii)
						for ( jj = 0; f && jj <= m; ++jj)
							if (squ(0, 0, i ,j,ii,jj) == a) {
								h = true;
								f = false;
							}
			if (!h)
				cout << "IMPOSSIBLE\n";
			else {
				cout << "0 0 " << i - 1 << ' ' << j - 1 << ' ' << ii - 1 << ' ' << jj - 1 << endl;
			}
	//	}
     }
     return 0;
}