#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
const char S[]="welcome to code jam";
int dp[501][20];
int main(){
	int t;
	cin>>t;
	string s;
	getline(cin,s);
	for(int k=1;k<=t;++k){
		getline(cin,s);
		memset(dp,0,sizeof(dp));
		for(int i=0;i<(int)s.length();++i){
			dp[i][0]=1;
			for(int j=0;j<19;++j){
				dp[i+1][j+1]=dp[i][j+1];
				if(s[i]==S[j])
					dp[i+1][j+1]+=dp[i][j];
				dp[i+1][j+1]%=10000;
			}
		}
/*		int ans=0;
		for(int i=18;i<(int)s.length();++i){
			ans+=dp[i+1][19];
			ans%=10000;
		}*/
		printf("Case #%d: %04d\n",k,dp[s.length()][19]);
	}
	return 0;
}
