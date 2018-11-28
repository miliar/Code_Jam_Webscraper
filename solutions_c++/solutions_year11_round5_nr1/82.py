#include<cstdio>
#include<algorithm>
using namespace std;
#define N 111
int W,L,U,G,x1[N],y1[N],x2[N],y2[N];
double cu(int a,double u)	//2
{
	return (u-x2[a])/(x2[a+1]-x2[a])*(y2[a+1]-y2[a])+y2[a];
}
double cd(int a,double u)	//1
{
	return (u-x1[a])/(x1[a+1]-x1[a])*(y1[a+1]-y1[a])+y1[a];
}
double calcS(int D,int U,double u,double w)
{
	return (w-u)*(cu(U,u)-cd(D,u)+cu(U,w)-cd(D,w))/2;
}
double cs(double w)
{
	double S=0,la=0;int LU=0,LD=0;
	for(;;)
	{
		int ned=x1[LD+1],neu=x2[LU+1];
		if(w<=min(ned,neu))
		{
			S+=calcS(LD,LU,la,w);
			break;
		}
		if(ned<neu)
		{
			S+=calcS(LD,LU,la,ned);
			la=ned;
			LD++;
		}else
		{
			S+=calcS(LD,LU,la,neu);
			la=neu;
			LU++;
		}
	}
	return S;
}
double cl(double S)
{
	double L=0,R=W;
	for(int _=1;_<=300;_++)
	{
		double M=(L+R)/2;
		if(cs(M)<S)L=M;else R=M;
	}
	return L;
}
int main()
{
	int _;scanf("%d",&_);
	for(int __=1;__<=_;__++)
	{
		scanf("%d%d%d%d",&W,&L,&U,&G);
		for(int i=0;i<L;i++)scanf("%d%d",x1+i,y1+i);
		x1[L]=x1[L-1]+1e-12;y1[L]=y1[L-1]+1e-12;
		for(int i=0;i<U;i++)scanf("%d%d",x2+i,y2+i);
		x2[U]=x2[U-1]+1e-12;y2[U]=y2[U-1]+1e-12;
		double S=cs(W);
		printf("Case #%d:\n",__);
		for(int i=1;i<=G-1;i++)
			printf("%.9lf\n",cl(S/G*i));
	}
	return 0;
}

