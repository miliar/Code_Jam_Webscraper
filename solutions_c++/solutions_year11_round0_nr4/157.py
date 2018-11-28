#include<iostream>
#include<vector>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
int key[2000],mark[2000],dps[2000];
double pp,dp[2000];
void dfs(double now, int n, int remain, int here){
//	printf("%lf\t%d\t%d\t%d\n",now,n,remain,here);
	if(remain == 0){
		double ans=1;
		for(int i=1;i<here;i++)ans+=dps[i]*dp[i];
	//	printf("%lf\n",ans);
		ans*=now;
		pp+=now;
		//ans*=here;ans/=(here-1);
		dp[here] += ans;//min(dp[here], ans);
		return;
	}
	if(n>=here)return;
	double x=1;
	int tot=1;
	dps[n]=0;
	dfs(now*x,n+1,remain,here);
	while(remain>=n){
		x/=n;
		x/=tot;
		dps[n]=tot;
		tot++;
		remain-=n;
		dfs(now*x,n+1,remain,here);
	}
}
void getdp(int n){
	dfs(1,1,n,n);
	dp[n]*=n;dp[n]+=1;
	dp[n]/=(n-1);
}

int main(){
	freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);
	int T,n,TC=0,i;
	double ans;
	scanf("%d",&T);
	for(i=2;i<20;i++)dp[i]=0;
	for(i=2;i<20;i++){
		pp=0;
	//	getdp(i);
	//	printf("%lf\t%lf\n",pp+(1.0/i),dp[i]);
	}
	
	while(T--){TC++;
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%d",&key[i]),mark[i]=0;
		for(ans=0,i=0;i<n;i++)if(!mark[i]){
			int sum=0,tem=key[i];
			while(tem-1 != i){
				sum++;
				mark[tem-1] = 1;
				tem = key[tem-1];
			}
			//printf("%d\n",sum);
			ans+=sum?(sum+1):0;
		}
		printf("Case #%d: %.6lf\n",TC,ans);
	}
}
