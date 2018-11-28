#include <cstdio>
#include <memory.h>
int a[1010];
int n;
int chk[1010];
int Sum,ans=-1;
int check() {
	int rho1=0,rho2=0;
	int i;
	for(i=0;i<n;i++) {
		if(chk[i]==0) rho1^=a[i];
		else rho2^=a[i];
	}
	if(rho1==rho2) return 1;
	return 0;
}
int dfs(int v,int sum) {
	if(v==n) {
		if(sum==0 || Sum-sum==0) return 0;
		if(check()) {
			int cand=sum>(Sum-sum)?sum:(Sum-sum);
			if(cand>ans) ans=cand;
		}
		return 0;
	}
	dfs(v+1,sum);
	chk[v]=1;
	dfs(v+1,sum+a[v]);
	chk[v]=0;
	return 0;
}
int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int T,Ti;
	scanf("%d",&T);
	for(Ti=0;Ti<T;Ti++) {
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++) {
			scanf("%d",&a[i]);
			Sum+=a[i];
		}
		dfs(0,0);
		if(ans==-1) printf("Case #%d: NO\n",Ti+1);
		else printf("Case #%d: %d\n",Ti+1,ans);
		ans=-1;
		memset(chk,0,sizeof(chk));
		Sum=0;
	}
	return 0;
}