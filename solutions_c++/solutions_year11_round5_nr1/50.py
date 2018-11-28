#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

const int maxn = 200 + 10;

const double zero = 1e-8;


struct pline
{
	int x[maxn],y[maxn];
	int tot;

	void init()
	{
		for( int i = 0;i<tot;i++ ) scanf("%d%d",x+i,y+i);
	}
	void get( int p,int xstart,double &a,double &b )
	{
		double la = 1.0*(y[p+1]-y[p])/(x[p+1]-x[p]);
		double lb = y[p] + (xstart-x[p])*la;

		a = 0.5*la;b = lb;
	}
} bd[2];


int W,G;

double length[maxn],sa[maxn],sb[maxn];

int xv[maxn],xt;
int main()
{
	int T=0,TT;
	double a1,b1,a2,b2;
	double tarea;
	for( scanf("%d",&TT);TT;TT-- )
	{
		printf("Case #%d:\n",++T);
		scanf("%d%d%d%d",&W,&bd[0].tot,&bd[1].tot,&G);
		bd[0].init();
		bd[1].init();

		xt = 0;
		for( int i = 0;i<bd[0].tot;i++ )
			xv[xt++] = bd[0].x[i];
		for( int i = 0;i<bd[1].tot;i++ )
			xv[xt++] = bd[1].x[i];
		sort( xv,xv+xt );

		int tmp = xt;
		xt = 0;
		for( int i = 1;i<tmp;i++ ) if( xv[i]!=xv[xt] )
			xv[++xt] = xv[i];

		//xv[0]~xv[xt]
		int p1 = 0,p2 = 0;
		tarea = 0;
		for( int i = 0;i<xt;i++ )
		{
			length[i] = xv[i+1] - xv[i];
			while( bd[0].x[p1+1] <= xv[i] ) p1++;
			while( bd[1].x[p2+1] <= xv[i] ) p2++;
			bd[1].get( p2,xv[i],a1,b1 );
			bd[0].get( p1,xv[i],a2,b2 );
			sa[i] = a1 - a2;
			sb[i] = b1 - b2;

			tarea += length[i]*length[i] * sa[i] + length[i]*sb[i];
		}

		double left = tarea / G,ans;
		p1 = 0;
		for( int i = 1;i<G;i++ )
		{
			while(length[p1] * length[p1] * sa[p1] + length[p1]*sb[p1] +zero < left)
			{
				left -= length[p1] * length[p1] * sa[p1] + length[p1]*sb[p1];
				p1++;
			}
			//solve eq
			if( fabs(sa[p1]) > zero )
			     ans = (-sb[p1] + sqrt(fabs(sb[p1]*sb[p1]+4*sa[p1]*left)))/ (2*sa[p1]);
           else ans = left / sb[p1];
			printf("%.10lf\n",ans + xv[p1]);
			left += tarea / G;
		}
	}
	return 0;
}
