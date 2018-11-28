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

#define FN(a, b, c) for( (a) = (b); (a) < (c); a++)
#define FB(a, b, c) for( (a) = (b); (a) >= (c); a--)
#define REP(i, n) FN(i,0,n)
#define RREP(i, n) FN(i,n,0)
#define RIT(i, n) FN(i, n.begin(), n.end())
#define RRIT(i, n) FN(i, n.rbegin(), n.rend())

using namespace std;

int main()
{
	int T, i, j, k, l, res;
	cin >> T;
	REP(i, T)
	{
		res = 1;
		cout << "Case #" << (i+1) << ": " << endl;
		int r, c;
		cin >> r >> c;
		string tile[r];
		REP(j, r)
		{
			cin >> tile[j];
		}
		int ab = 0;
		REP(j, r)
		{
			REP(k, c)
			{
				if(tile[j][k] == '#' ) ab++;
			}
		}
		if(ab%4 != 0) res = 0;
		if(res)
		{
			REP(j, r)
			{
				REP(k, c)
				{
					if(tile[j][k] == '#' && k != c-1 && tile[j][k+1] == '#' && j != r-1 && tile[j+1][k] == '#' && tile[j+1][k+1] == '#')
					{
						tile[j][k] = '/';
						tile[j+1][k] = '\\';
						tile[j][k+1] = '\\';
						tile[j+1][k+1] = '/';
					}
				}
			}
			REP(j, r)
			{
				REP(k, c)
				{
					if(tile[j][k] == '#' )
					{
						res = 0;
						break;
					}
				}
				if(!res)
					break;
			}
		}
		if(!res)
		{
			cout << "Impossible" << endl;
		}
		else
		{
			REP(j, r)
			cout << tile[j] << endl;
		}
	}
	return 0;
}