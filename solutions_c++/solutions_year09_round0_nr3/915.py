#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main() {
	string s="welcome to code jam";
	int n = s.length();
	int t;
	scanf("%d\n",&t);
	for(int si = 1; si <=t;++si){
		cout<<"Case #"<<si<<": ";
		char str[10000];
		gets(str);
		int l = strlen(str);
		int dp[1000][30];
		memset(dp,0,sizeof(dp));
		dp[0][0] = 1;
		for(int i = 1 ; i <= l; ++i){
			dp[i][0] = 1;
			for(int j = 1 ; j <= n; ++j){
				if(s[j-1] == str[i-1]){
					dp[i][j] += dp[i-1][j-1];
				}
				dp[i][j] += dp[i-1][j];
				dp[i][j] %= 10000;
			}
		}
		char ans[5];
		sprintf(ans,"%d",dp[l][n]);
		for(int p = 0 ; p < 4 - strlen(ans); p++) cout<<"0";
		cout << ans << endl;
	}
	return 0;
}
