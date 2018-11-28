#include <stdio.h>

int g[12000];
int c[12000];
int M,V;

int m(int a,int b)
{
	if (a<b) return a;
	return b;
}

int x(int i,int d)
{
	int a,b;
//	printf("%d %d\n",i,d);
	if (i<((M-1)/2))
	{
		if (g[i]==1) // and
		{
			if (d==0)
			{
				a=x(2*i+1,0);
				b=x(2*i+2,0);
				return m(a,b);
			} else
			{
				a=x(2*i+1,1);
				b=x(2*i+2,1);
				if (c[i])
				{
					a=m(a+b,m(a+1,b+1));
				} else
				{
					a=a+b;
				}
				if (a<=M)
					return a;
				return M+1;
			}
		} else
		{
			if (d==1)
			{
				a=x(2*i+1,1);
				b=x(2*i+2,1);
				return m(a,b);
			} else
			{
				a=x(2*i+1,0);
				b=x(2*i+2,0);
				if (c[i])
				{
					a=m(a+b,m(a+1,b+1));
				} else
				{
					a=a+b;
				}
				if (a<=M)
					return a;
				return M+1;
			}
		}
	} else
	{
//		printf("R %d %d\n",g[i],d);
		if (g[i]==d) 
		{
			return 0;
		}
		return M+1;
	}
}

int main()
{
	int nn,ii;
	int i;
	scanf("%d\n",&nn);
	for (ii=0;ii<nn;++ii)
	{
		scanf("%d %d",&M,&V);
		for (i=0;i<((M-1)/2);++i)
		{
			scanf("%d %d",g+i,c+i);
		}
		for (;i<M;++i)
		{
			scanf("%d",g+i);
		}
		printf("Case #%d: ",ii+1);
		i=x(0,V);
		if (i<=M)
		{
			printf("%d\n",i);
		} else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
