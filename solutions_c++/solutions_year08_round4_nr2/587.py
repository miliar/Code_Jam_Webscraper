#include <stdio.h>
#include <math.h>

int xx[100];
int c[100];
int N,M,A;
int X,Y,Q,W,R,T;

long long sqrr(long long x)
{
	return x*x;
}

int go(long long z,long long v,int h,int n)
{
	long long i,x,y,q,w;
//	printf("%lld %lld %d %d\n",z,v,h,n);
	if (h==n)
	{
		if (N*N+M*M<z) return 0;
		x=y=0;
		while (y*y<z) ++y;
		while (y>=0)
		{
			if (x*x+y*y<=z)
			{
				if (x*x+y*y==z && x>=0 && x<=N && y>=0 && y<=M)
				{
					q=w=0;
					while (w<=M && w*x<A*A) ++w;
					while (w<=M && q<=N)
					{
						if (sqrr(w*x-q*y)==z*v)
						{
							X=x;
							Y=y;
							Q=q;
							W=w;
							return 1;
						}
						if (sqrr(w*x-q*y)<z*v)
						{
							++w;
						} else
						{
							++q;
						}
					}
				}
				++x;
			} else
			{
				--y;
			}
		}
	} else
	{
		for (i=0;i<2*c[h];++i) v=v*xx[h];
		for (i=0;i<=2*c[h];++i)
		{
			if (go(z,v,h+1,n)) return 1;
			z=z*xx[h];
			v=v/xx[h];
		}
	}
	return 0;
}

double e(int x)
{
	return x*x;
}

int main()
{
	int nn,ii,i,j,n;
	int x,y,q,w;
	scanf("%d\n",&nn);
	for (ii=0;ii<nn;++ii)
	{
		scanf("%d %d %d",&N,&M,&A);
/*		n=0;
		for (i=2;i<=A;++i) if ((A%i)==0)
		{
			xx[n]=i;
			c[n]=0;
			while ((A%i)==0)
			{
				c[n]++;
				A/=i;
			}
			++n;
		}*/
		n=0;
		for (i=0;i<1;++i) for (j=0;j<1;++j) if (n==0)
					for (x=0;x<=N;++x) for (y=0;y<=M;++y) if (n==0)
								for (q=0;q<=N;++q) for (w=0;w<=M;++w) if (n==0)
		{
			double a,b,c,s,S;
			a=sqrt(e(i-x)+e(j-y));
			b=sqrt(e(i-q)+e(j-w));
			c=sqrt(e(q-x)+e(w-y));
			s=(a+b+c)/2.0;
			S=sqrt(s*(s-a)*(s-b)*(s-c));
			if (fabs(S-A/2.0)<0.2)
			{
				n=1;
				R=i;
				T=j;
				X=x;
				Y=y;
				W=w;
				Q=q;
			}
		}
		printf("Case #%d: ",ii+1);
		if (n)
		{
			printf("%d %d %d %d %d %d\n",R,T,X,Y,Q,W);
		} else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
