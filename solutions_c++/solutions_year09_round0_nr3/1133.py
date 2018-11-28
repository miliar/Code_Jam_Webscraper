#include<algorithm>
#include<iostream>
#include<math.h>
#include<map>
#include<string>
using namespace std;
#define memo(a,b) memset(a,b,sizeof(a))
#define MOD 10000
int dp[505][20],la,lb;
char a[505],b[20];
int solve(int x,int y){
	if(y==lb) return 1;
	if(x==la) return 0;
	if(dp[x][y]!=-1) return dp[x][y];
	int ret=0;
	if(a[x]==b[y]){
		ret+=solve(x+1,y+1);
		ret%=MOD;
	}
	ret+=solve(x+1,y);
	return dp[x][y]=ret%MOD;
}
int main(){
	int cs,t;
//	freopen("C.in","r",stdin);
//	freopen("C.ans","w",stdout);
	strcpy(b,"welcome to code jam");
	lb = strlen(b);
	scanf("%d",&t);
	getchar();
	for(cs=1;cs<=t;cs++){
		gets(a);
		la =strlen(a);
		memo(dp,-1);
		printf("Case #%d: %04d\n",cs,solve(0,0));
	}
	return 0;
}