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
#include <queue>
#include <complex>
using namespace std;

#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))


int main()
{
	freopen("in.in", "r", stdin);
	int t, n;
	int robs[2][101];
	char seq[101];
	cin >> t;
	for(int c = 1; c <= t; c++)
	{
		cin >> n;
		int but;
		int bIdx = 0, oIdx = 0;
		for(int i = 0; i < n; i++)
		{
			cin >> seq[i] >> but;
			if(seq[i] == 'O')
				robs[1][oIdx++] = but;
			else
				robs[0][bIdx++] = but;
		}

		long long res = 0, needed, otherNeeded;
		int bPlc = 1, oPlc = 1;
		bIdx = 0; oIdx = 0;
		for(int i = 0; i < n; i++)
		{
			if(seq[i] == 'O')
			{
				needed = abs(oPlc - robs[1][oIdx]) + 1;
				oPlc = robs[1][oIdx];
				res += needed;
				otherNeeded = abs(bPlc - robs[0][bIdx]);
				if(needed == 0) needed = 1;
				if(otherNeeded <= needed)
					bPlc = robs[0][bIdx];
				else
				{
					if(bPlc < robs[0][bIdx])
						bPlc += needed;
					else
						bPlc -= needed;
				}
				oIdx++;
			}
			else
			{
				needed = abs(bPlc - robs[0][bIdx]) + 1;
				bPlc = robs[0][bIdx];
				res += needed;
				otherNeeded = abs(oPlc - robs[1][oIdx]);
				if(otherNeeded <= needed)
					oPlc = robs[1][oIdx];
				else
				{
					if(oPlc < robs[1][oIdx])
						oPlc += needed;
					else
						oPlc -= needed;
				}
				bIdx++;
			}
		}
		printf("Case #%d: %lld\n", c, res);
	}
	return 0;
}
