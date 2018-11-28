#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

int cost[3000];
int cnt[3000];
int f[3000][15];


int Go(int pos, int l, int r, int b)
{
	int& res = f[pos][b];
	if (res != -1) return res;
	res = -2;
	if (l == r)
	{
		if (b >= cnt[l]) return res = 0;
		else return res = -2;
	}

	int m = (l+r) / 2;
	int r1 = Go(pos*2+1, l, m, b);
	int r2 = Go(pos*2+2, m+1, r, b);
	if (r1 != -2 && r2 != -2)
	{
		res = r1+r2;
	}

	r1 = Go(pos*2+1, l, m, b+1);
	r2 = Go(pos*2+2, m+1, r, b+1);
	if (r1 != -2 && r2 != -2)
	{
		if (res == -2 || res > r1+r2+cost[pos])
		{
			res = r1+r2+cost[pos];
		}
	}
	return res;
}

int main()
{
	ifstream ifs("b.in");
	ofstream ofs("b.out");		
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		memset(cost, 0, sizeof(cost));
		memset(f, -1, sizeof(f));
		int p;		
		ifs >> p;
		for (int i = 0; i < (1<<p); ++i )
		{
			ifs >> cnt[i];
			cnt[i] = p-cnt[i];
		}
		vector<int> c;
		for (int i = 0; i < p; ++i)
		{
			vector<int> tmp;
			for (int j = 0; j < (1<<(p-i-1)); ++j)
			{
				int k;
				ifs >> k;
				tmp.push_back(k);
			}
			c.insert(c.begin(), tmp.begin(), tmp.end());
		}
		for (int i = 0; i < c.size(); ++i)
		{
			cost[i] = c[i];
		}
		int res = Go(0, 0, (1<<p)-1, 0);
		ofs << "Case #" << test+1 << ": " << res << endl;
	}
  	return 0;
}
