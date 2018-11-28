#include<cstdio>
int t,n,mn,c,x,sum;
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		scanf("%d",&n);
		mn=1<<30; x=0; sum=0;
		for (int i=1; i<=n; i++){
			scanf("%d",&c);
			mn=c<mn?c:mn;
			x^=c;
			sum+=c;
		}
		if (x) printf("Case #%d: NO\n",z);
		else printf("Case #%d: %d\n",z,sum-mn);
	}
	return 0;	
}
