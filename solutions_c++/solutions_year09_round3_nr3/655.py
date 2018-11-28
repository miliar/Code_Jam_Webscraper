#include <algorithm>
#include <functional>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <iostream>

using namespace std;

#define MX 1000000000

int tc, p, q;
int pris[6], dp[1 << 7];

int solve(int n)
{
	int &ret = dp[n];
	if(ret == -1)
	{
		ret = MX;
		bool found = false;
		for(int i = 0; i < q; ++i)
			if((n & (1 << i)) == 0)
			{
				set<int> vis;
				for(int j = 0; j < q; ++j)
					if((n & (1 << j)) > 0)
						vis.insert(pris[j]);
				found = true;
				int get = 0;
				for(int j = pris[i] - 1; j >= 1; --j)
					if(vis.find(j) != vis.end())
						break;
					else
						++get;
				for(int j = pris[i] + 1; j <= p; ++j)
					if(vis.find(j) != vis.end())
						break;
					else
						++get;
				ret = min(ret, solve((n | (1 << i))) + get);
			}
		if(!found)
			ret = 0;
	}
	return ret;
}

int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	
	scanf("%d", &tc);
	
	for(int T = 1; T <= tc; ++T)
	{
		scanf("%d %d", &p, &q);
		for(int i = 0; i < q; ++i)
			scanf("%d", &pris[i]);
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", T, solve(0));
	}
	
	return 0;
}
