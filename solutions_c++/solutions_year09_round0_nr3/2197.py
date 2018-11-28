#include<iostream>
#include<string>

using namespace std;
string s;
string s2="welcome to code jam";
int dp[501][20];
int doit(int k , int m){
	if(k==s.size())return 0;
	if(m==18){
		int flag=0;
		for(int i=k;i<s.size();i++){
			if(s2[m]==s[i]){
				flag++;
			}
		}
		return flag;
	}
	int &ans=dp[k][m];
	if(ans!=-1)return dp[k][m];
	ans=0;
	for(int i=k;i<s.size();i++)
		if(s2[m]==s[i]){
			ans+=doit(i+1,m+1)%10000;
		}
	return ans;
}
int main(){
	int N;
	cin>>N;
	getline(cin,s);
	for(int i=0;i<N;i++){
		memset(dp,-1,sizeof(dp));
		getline(cin,s);
		int ans=0;
		//for(int j=0;j<s.size();j++){
			ans+=doit(0,0)%10000;
		//}
		printf("Case #%d: %04d\n",i+1,ans);
	}
	return 0;
}