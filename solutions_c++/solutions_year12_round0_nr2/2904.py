#include <iostream>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int work1(int n){
	int ans=-1;
	for(int i=0;i<=10;i++){
		for(int j=i;j<=i+2;j++){
			for(int k=j;k<=i+2;k++){
				if(k-i==2 && i+j+k==n) ans=max(ans,k);
			}
		}
	}
	return ans;
}

int work2(int n){
	int ans=-1;
	for(int i=0;i<=10;i++){
		for(int j=i;j<=i+2;j++){
			for(int k=j;k<=i+2;k++){
				if(k-i<2 && i+j+k==n) ans=max(ans,k);
			}
		}
	}
	return ans;
}

int ti[200],dp[200][200];

int main()
{
	int a,b,x;
	string str;
	cin>>x;
	for(int y=1;y<=x;y++){
		int t,s,p;
		cin>>t>>s>>p;
		memset(ti,0,sizeof ti);
		memset(dp,0,sizeof dp);
		for(int i=1;i<=t;i++) cin>>ti[i];
		for(int i=1;i<=t;i++){
			for(int j=0;j<=s;j++){
				dp[i][j]=dp[i-1][j];
				if(work2(ti[i])>=p) dp[i][j]++;
				if(j>0){
					if(work1(ti[i])>=p){
						if(dp[i-1][j-1]+1>dp[i][j]) dp[i][j]=dp[i-1][j-1]+1;
					}
				}
			}
		}
		cout<<"Case #"<<y<<": "<<dp[t][s]<<endl;
	}
}