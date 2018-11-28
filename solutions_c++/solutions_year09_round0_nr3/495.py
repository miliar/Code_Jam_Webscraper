#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	string t, s = "welcome to code jam";
	getline(cin,t);
	for (int z=1;z<=n;++z){
		getline(cin,t);
		int tn = t.length(), sn = s.length();
		int dp[tn+1][sn+1];
		memset(dp,0,sizeof(dp));
		dp[0][0] = 1;
		for (int i=0;i<tn;++i)
			for (int r=0;r<sn;++r)
				if (t[i]==s[r])
					for (int k=0;k<=i;++k)
						dp[i+1][r+1] = (dp[i+1][r+1]+dp[k][r])%10000;
		int ans = 0;
		for (int i=0;i<=tn;++i)
			ans = (ans + dp[i][sn])%10000;
		printf("Case #%d: %04d\n",z,ans);
	}
	return 0;
}
