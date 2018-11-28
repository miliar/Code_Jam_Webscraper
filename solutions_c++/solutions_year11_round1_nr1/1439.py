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
	int T, Pd, Pg, res;
	unsigned long long N, i, j, k, l;
	cin >> T;
	REP(i, T)
	{
		cin >> N >> Pd >> Pg;
		res = 0;
		REP(j, N+1)
		{
			REP(k, j+1)
			{
				double percent = (double(k*100)/j);
				if(percent == Pd)
				{
					if(Pg == 100)
					{
						if(Pd == 100)
							res = 1;
						else
							res = 0;
					}
					else if(Pg == 0)
					{
						if(Pd == 0)
							res = 1;
						else
							res = 0;
					}
					else
						res = 1;
				}
			}
		}
		if(res)
			cout << "Case #" << (i+1) << ": " << "Possible" << endl;
		else
			cout << "Case #" << (i+1) << ": " << "Broken" << endl;
	}
	return 0;
}