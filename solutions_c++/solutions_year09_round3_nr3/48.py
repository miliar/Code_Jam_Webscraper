#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <queue>
using namespace std;
int tc,p,q,a[105];
int dp[105][105];
int f(int h,int t){
	if (dp[h][t]!=-1) return (dp[h][t]);
	else if (h>t) {dp[h][t]=0; return 0;}
	else {
		int mn=(1<<30)-1;
		for (int i=h;i<=t;i++){
			int tmp=f(h,i-1)+f(i+1,t);
			if (tmp<mn) mn=tmp;
		}
		dp[h][t]=mn+(a[t+1]-a[h-1]-2);
		return (dp[h][t]);
	}
}
int main(){
	scanf("%d",&tc);
	for (int c=1;c<=tc;c++){
		scanf("%d%d",&p,&q);
		memset(dp,-1,sizeof(dp));
		for (int i=1;i<=q;i++) scanf("%d",&a[i]);
		a[0]=0; a[q+1]=p+1;
		printf("Case #%d: %d\n",c,f(1,q));	
	}
}
