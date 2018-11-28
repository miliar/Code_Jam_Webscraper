#include<iostream>
#include<stdio.h>
using namespace std;
int d[10001];
int l[10001];
int dp[10001];
int main(){
	int t,n,D,x,y;
	bool f;
	freopen("A-large.in","r",stdin);
 	freopen("out.out","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
		f=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			dp[i]=0;
			scanf("%d %d",&d[i],&l[i]);
		}
		scanf("%d",&D);
		dp[0]=d[0];
		for(int i=0;i<n;i++){
			if(d[i]+dp[i]>=D){
				f=1;
				break;
			}
			for(int j=i+1;j<n;j++){
				if(d[j]-d[i]<=dp[i]&&dp[j]==0)
					dp[j]=min(l[j],d[j]-d[i]);
			}
		}
		if(f==0)
			printf("Case #%d: NO\n",cas);
		else
			printf("Case #%d: YES\n",cas);
	}
	return 0;
}
