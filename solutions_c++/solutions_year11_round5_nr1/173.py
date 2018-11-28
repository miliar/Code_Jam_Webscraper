#include <cstdio>
using namespace std;
double Uy[1005],Ly[1005],Data[1005];
void scanPoint(int n,double* data)
{
	int lx = 0, ly = 0;
	for (int q=0;q<n;++q)
	{
		int x,y;
		scanf("%d %d",&x,&y);
		for (int ax=lx + 1;ax<x;++ax)
		{
			double ay = ly + (y-ly) * double(ax-lx)/(x-lx);
			data[ax] = ay;
		}
		data[x] = y;
		lx = x, ly= y;
	}
}
double calcArea(double a,double b)
{
	int p = a+1.;
	int q = b;
	double ret = 0.;
	for (int i=p;i<q;++i) ret += (Data[i]+Data[i+1])*.5;
	//a to p
	double ay = Data[p-1] + (Data[p] - Data[p-1]) * (a-p+1);
	double by = Data[q] + (Data[q+1] - Data[q]) * (b-q);
	ret += (ay+Data[p]) * (p-a) * .5 + (by+Data[q]) * (b-q) * .5;
	return ret;
}
int main()
{
	int T;
	scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int W,L,U,G;
		scanf("%d %d %d %d",&W,&L,&U,&G);
		scanPoint(L,Ly);
		scanPoint(U,Uy);



		for (int q=0;q<=W;++q) Data[q] = Uy[q] - Ly[q];
		Data[W+1]= Data[W];
		double tar = 0;
		for (int q=0;q<W;++q) tar += (Data[q] + Data[q+1]) * .5;
		tar/=G;
		printf("Case #%d:\n",kase);
		double cur = 0;
		for (int q=0;q+1<G;++q)
		{
			double lo = cur, hi = W;
			for (int w=0;w<=100;++w)
			{
				double mi = (lo+hi)/2.;
				if ( calcArea(cur,mi) < tar ) lo = mi;
				else hi = mi;
			}
			cur = (lo+hi)/2.;
			printf("%.8lf\n",cur);
		}
	}
	return 0;
}
