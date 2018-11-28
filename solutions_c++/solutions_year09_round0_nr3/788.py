#include <iostream>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

#define REP(i,m,n) for(i = m;i <= n;i++)

const int MOD_NUM = 10000;

int dp[501][20],ans[4];

int main()
{
//	freopen("D:\\VC project\\ForTest\\Debug\\input.in","r",stdin);
//	freopen("D:\\VC project\\ForTest\\Debug\\out.txt","w",stdout);
	int n,i,j,no = 0,len;
	string input,str = "welcome to code jam";
	scanf("%d",&n);getchar();
	while(++no <= n)
	{
		getline(cin,input);
		len = (int)input.size();
		memset(dp,0,sizeof(dp));
		REP(i,0,len) dp[i][0] = 1;
		REP(i,1,len) REP(j,1,19) 
		{
			if(j > i) break;
			if(i > j) dp[i][j] = dp[i - 1][j];
			if(input[i - 1] == str[j - 1]) dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD_NUM;
		}
		REP(i,0,3) ans[i] = dp[len][19] % 10,dp[len][19] /= 10;
		cout << "Case #" << no << ": "<< ans[3] << ans[2] << ans[1] << ans[0] << endl;
	}
	return 0;
}