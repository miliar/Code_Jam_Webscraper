#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int a[20000],len[20000],dp[20000];

int main(){
	int i,j,k,m,n,c,r,x,t,D;
	bool f;
	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&r);
	for(c=1;c<=r;++c){
		scanf("%d",&n);
		for(i=0;i<n;++i)	scanf("%d%d",&a[i],&len[i]);
		scanf("%d",&x);

		memset(dp,0,sizeof(dp));
		dp[0]=a[0];
		for(i=0;i<n-1;++i){
			if(dp[i]==0)	continue;
			for(j=i+1;j<n;++j){
				if(dp[i]+a[i]>=a[j]){
					t=a[j]-a[i];
					if(t>len[j])	t=len[j];
					if(t>dp[j])	dp[j]=t;
				}
			}
		}
		printf("Case #%d: ",c);
		f=false;
		for(i=0;i<n;++i){
			if(dp[i]+a[i]>=x)	f=true;
		}
		if(f)	printf("YES\n");
		else	printf("NO\n");
	}
}
