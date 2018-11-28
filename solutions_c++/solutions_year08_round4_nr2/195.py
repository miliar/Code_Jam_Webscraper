#include<stdio.h>
int h,t,n,m,a,i,j,k,l,z;
int main()
{
	freopen("b.in.txt","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for(h=0;h<t;h++)
	{
		scanf("%d%d%d",&n,&m,&a);
		z=0;
		printf("Case #%d: ",h+1);
		if(a<=n*m)
		{
			z=1;
			i=n;
			for(l=0;i*l<a;l++);
			j=1;
			for(k=0;i*l-j*k>a;k++);
			printf("%d %d %d %d %d %d\n",0,0,i,j,k,l);
		}
		if(!z)puts("IMPOSSIBLE");
	}
	return 0;
}