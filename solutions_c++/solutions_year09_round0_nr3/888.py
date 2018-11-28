#include<stdio.h>
#include<string>
#include<iostream>

using namespace std;

int tc,t;
string s;
string pt="welcome to code jam";
int dp[20][501];
int i,j;
int res;

int main(){
	freopen("wel2.in","r",stdin);
	freopen("wel2.out","w",stdout);

	scanf("%d\n",&tc);
	for(t=1;t<=tc;t++){
		getline(cin,s);
		for(i=0;i<19;i++){
			for(j=0;j<s.length();j++){
				dp[i][j]=0;
			}
		}
		if(s[0]==pt[0]) dp[0][0]=1;
		for(j=1;j<s.length();j++){
			for(i=0;i<19;i++){
				dp[i][j]=dp[i][j-1];
			}
			if(s[j]==pt[0]) dp[0][j]++;
			dp[0][j]%=10000;
			for(i=1;i<19;i++){
				if(s[j]==pt[i]){
					dp[i][j]+=dp[i-1][j-1];
				}
				dp[i][j]%=10000;
			}
		}
		printf("Case #%d: ",t);
		res=dp[18][s.length()-1];
		if(res<1000) printf("0");
		if(res<100) printf("0");
		if(res<10) printf("0");
		printf("%d\n",res);
	}
	return 0;
}
