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

int tc, n, leng;
map<pair<int, string>, int> dp;

int solve(int pos, string s)
{
	if(pos == leng)
		return atoi(s.c_str());
	if(dp[make_pair(pos, s)])
		return dp[make_pair(pos, s)];
	int ret = 1000000000;
	for(int i = 0; i < leng; ++i)
	{
		string seek = s;
		seek[i] = s[pos];
		seek[pos] = s[i];
		int get = solve(pos + 1, seek);
		if(get != n && get > n)
			ret = min(ret, get);
	}
	return dp[make_pair(pos, s)] = ret;
}

int main()
{
	freopen("B-Small.in", "r", stdin);
	freopen("B-Small.out", "w", stdout);
	
	scanf("%d", &tc);
	
	for(int T = 1; T <= tc; ++T)
	{
		dp.clear();
		scanf("%d", &n);
		string s;
		stringstream ss;
		ss << n;
		s = ss.str();
		leng = s.size();
		int res = solve(0, s);
		if(res < 1000000000)
			printf("Case #%d: %d\n", T, res);
		else
		{
			sort(s.begin(), s.end());
			int z = 0;
			printf("Case #%d: ", T);
			bool found = false;
			for(int i = 0; i < s.size(); ++i)
				if(s[i] != '0' && !found)
				{
					found = true;
					printf("%c0", s[i]);
					for(int j = 0; j < z; ++j)
						printf("0");
				}
				else if(found)
					printf("%c", s[i]);
				else
					++z;
			printf("\n");
		}
	}
	
	return 0;
}
