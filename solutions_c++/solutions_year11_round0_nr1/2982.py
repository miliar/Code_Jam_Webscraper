#include <stdio.h>
#define fabs(x) (x>0?x:-x)
#define f(x) (x<0?0:x)
int main()
{
	int i,t,n,k,k2,l=1;
	int b,o,bn,on,sum;
	char c;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		bn=on=1;
		b=o=sum=0;
		scanf("%d ",&n);
		for(i=0;i<n;i++)
		{
			scanf("%1s%d",&c,&k);
			if(c=='O')
			{
				k2=fabs((k-on));
				sum+=f((k2-o))+1;
				b+=f(k2-o)+1;
				o=0;
				on=k;
			}
			else 
			{
				k2=fabs((k-bn));
				sum+=f((k2-b))+1;
				o+=f(k2-b)+1;
				b=0;
				bn=k;
			}
		}
		printf("Case #%d: %d\n",l++,sum);

	}
	return 0;
}