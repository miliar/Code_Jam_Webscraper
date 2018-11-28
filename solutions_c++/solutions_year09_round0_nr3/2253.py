#include <algorithm>
#include <iostream>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>

using namespace std;

#define MOD 10000

int n, leng, lengS, dp[500][20];
string wel;
char s[] = {"welcome to code jam"};

int solve(int pos, int seek)
{
	if(seek == lengS)
		return 1;
	if(pos == leng)
		return 0;
	int &ret = dp[pos][seek];
	if(ret == -1)
	{
		ret = 0;
		for(int i = pos + 1; i < leng; ++i)
			if(wel[i] == s[seek])
				ret = (ret % MOD + solve(i, seek + 1) % MOD) % MOD;
	}
	return ret;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	getline(cin, wel);
	istringstream iss(wel);
	iss >> n;
	
	for(int T = 1; T <= n; ++T)
	{
		memset(dp, -1, sizeof(dp));
		getline(cin, wel);
		leng = wel.size();
		lengS = strlen(s);
		int res = 0;
		for(int i = 0; i < leng; ++i)
			if(wel[i] == 'w')
				res = (res % MOD + solve(i, 1) % MOD) % MOD;
		printf("Case #%d: ", T);
		if(res < 1000 && res > 99)
			printf("0");
		else if(res < 100 && res > 9)
			printf("00");
		else if(res < 10)
			printf("000");
		printf("%d\n", res);
	}
	
	return 0;
}
