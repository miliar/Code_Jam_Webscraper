#include<cstdio>
#define EPS 1e-7
#define MN 1000004
long double a,mi,ma,p[MN],mp,d,wyn;
int test,ntest,n,i,j,c;
inline long double max(long double aa, long double bb) { return aa>bb?aa:bb; }

int main()
{
	scanf("%d",&ntest);
	for(test=1; test<=ntest; ++test) 
	{
		scanf("%d%Lf",&c,&d);
		for(i=n=0; i<c; ++i)
		{
			scanf("%Lf%d",&a,&j);
			while(j--) p[n++]=a;
		}
		mi=0.0;
		ma=n*d;
		while(ma-mi>EPS) {
			a=(ma+mi)/2.0;
			mp=p[0]-a;
			for(i=1; i<n; ++i) {
				mp=max(mp+d,p[i]-a);
				if(mp>p[i]+a) { i=-100; break; }
			}
			if(i<0) mi=a;
			else {
				ma=wyn=a;
			}
		}
		printf("Case #%d: %.8Lf\n",test,wyn);
		fprintf(stderr,"Case #%d: %.8Lf\n",test,wyn);
	}
}

