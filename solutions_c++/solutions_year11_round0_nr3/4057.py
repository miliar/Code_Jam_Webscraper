#include <cstdio>
int t,T,k,p,i,x,pa,n;
int main()
{
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for(i=x=pa=0,p=1000000;i<n;i++)
		{
			scanf("%d",&k);
			if(p>k) p=k;
			pa+=k;
			x^=k;
		}
		if(x)
			printf("NO\n"); else
			printf("%d\n",pa-p);
	}
	return 0;
}