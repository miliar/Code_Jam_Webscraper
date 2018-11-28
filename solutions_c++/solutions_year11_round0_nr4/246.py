#include<cstdio>
int a[1000];
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int i,j,m,n,t,tt=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		m=0;
		for(i=0;i<n;i++)
			if(a[i]!=i+1)m++;
		printf("Case #%d: %lf\n",tt++,(double)m);
	}
	return 0;
}