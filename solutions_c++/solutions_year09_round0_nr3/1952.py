#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
#define SS 35
#define LS 505
#define mod 10000
int dp[SS][30],n,len,res,txt,slen=18;
char in[SS];
char ch[]="welcome to code jam";
int doit(int i,int j){
	if(i<0||j<0)return 0;
	if(dp[i][j]>=0)return dp[i][j];
	int r=0;
	//if(in[i]==ch[slen]&&i!=slen)r=(r+doit(i-1,slen-1)%mod)%mod;
	if(in[i]==ch[j]){
		if(j==0)r=(r+1+doit(i-1,slen)%mod)%mod;
		else r=(r+doit(i-1,j-1)%mod)%mod;
	}
	r=(r+doit(i-1,j)%mod)%mod;
	return dp[i][j]=r%mod;
}
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int i,j,k;
	while(scanf("%d",&n)==1){
		gets(in);
		for(i=1;i<=n;i++){
			gets(in);
			memset(dp,-1,sizeof(dp));
			len=strlen(in);
			res=doit(len-1,slen);
			printf("Case #%d: %04d\n",++txt,res);
		}
	}
	return 0;
}