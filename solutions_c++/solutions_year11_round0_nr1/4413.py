#include <cstdio>
int t,T,a,b,x,y,pa,n,k,i;
char cc;
int abs(int a){if(a<0)return -a; return a;}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d",&n);
		a=1; b=1; x=y=0; pa=0;
		for(i=0;i<n;i++)
		{
			scanf(" %c %d",&cc,&k);
			if(cc=='O')
				if(y<=abs(a-k))
				{
					pa+=abs(a-k)-y+1;
					x+=abs(a-k)-y+1;
					y=0;
					a=k;
				}else
				{
					a=k;
					y=0;
					x=1;
					pa++;
				}
			if(cc=='B')
				if(x<=abs(b-k))
				{
					pa+=abs(b-k)-x+1;
					y+=abs(b-k)-x+1;
					x=0;
					b=k;
				}else
				{
					pa++;
					b=k;
					x=0;
					y=1;
				}
		}
		printf("%d\n",pa);
	}
	return 0;
}