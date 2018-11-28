#include <cstdio>
#define INF ((double)10000000000000LL)
int tt,I,J,n,D,k,i;
double x[200],y[200],T[200],l,r,xx,q,maxT;
bool f(double t)
{
	q=-INF;
	for(i=0;i<n;i++)
	{
//		printf("t=%.6lf,i=%d,x[i]=%.6lf,y[i]=%.6lf,q=%.6lf,D=%d,%d\n",(t-T[i]),i,x[i],y[i],q,D,x[i]+(t-T[i])-D<q);
		if(x[i]+(t-T[i])-D<q)
			return false; else
		if(x[i]-(t-T[i])-D>q)
			q=y[i]-(t-T[i]); else
			q=y[i]+(q+D-x[i]);
	}
	return true;
}
int main()
{
	freopen("2.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&tt);
	for(I=1;I<=tt;I++)
	{
		scanf("%d%d",&n,&D);
		maxT=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&J,&k);
			T[i]=0.5*D*(k-1);
			if(T[i]<0) T[i]=0;
			x[i]=J-T[i];
			y[i]=J+T[i];
			if(maxT<T[i]) maxT=T[i];
		}
		l=maxT; r=INF;
		for(J=0;J<300;J++)
		{
			xx=0.5*(l+r);
			if(f(xx))
				r=xx; else
				l=xx;
		}
		if(l-(long long)l>0.999)
			l=(long long)l+1;
		printf("Case #%d: %.6lf\n",I,l);
	}
	return 0;
}