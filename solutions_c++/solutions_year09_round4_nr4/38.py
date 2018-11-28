#include<cstdio>
#include<cmath>
#include<cstdlib>

const int maxn = 40 + 5;
const int maxv = 2000;
const double eps = 1e-7;
const double zero = 1e-9;

double vx[maxv],vy[maxv];
long long S[maxv];
int tot;
int x[maxn],y[maxn],R[maxn];
double r[maxn];
int n;

inline double sqr( double x )
{
	return x*x;
}
bool good( double sr )
{
	for(int i=0;i<n;i++)
	{
		r[i] = sr-R[i];
		if(r[i]<zero) return false;
	}
	
	double a,b,c;
	int tot = 0;
	double x0,y0,dx,dy;
	double A,B,C,del;
	double xx;
	for(int i=0;i<n;i++)
	{
		vx[tot] = x[i];
		vy[tot] = y[i]+r[i];
		tot++;

		for(int j=i+1;j<n;j++)if(x[i]!=x[j] || y[i]!=y[j])
		{
			a = 2*(x[j]-x[i]);
			b = 2*(y[j]-y[i]);
			c = sqr(r[j])-sqr(r[i])+sqr(x[i])-sqr(x[j])+sqr(y[i])-sqr(y[j]);

			if( fabs(a*x[i]+b*y[i]+c) -zero < sqrt( a*a+b*b ) * r[i] )
			{
				dx = -b;
				dy = a;
				if( x[i]!=x[j] )
				{
					x0 = -c/a;y0 = 0;
				}else
				{
					x0 = 0;y0 = -c/b;
				}

				A = dx*dx+dy*dy;
				B = 2*( dx*(x0-x[i]) + dy*(y0-y[i]) );
				C = sqr(x0-x[i])+sqr(y0-y[i])-sqr(r[i]);

				del = B*B-4*A*C;
				if( del > -zero )
				{
					del = sqrt(fabs(del));
					xx = 0.5*(-B-del)/A;

					vx[tot] = x0 + xx*dx;
					vy[tot] = y0 + xx*dy;
/*
					if( fabs( sqr(vx[tot]-x[i])+sqr(vy[tot]-y[i])-sqr(r[i]) )>zero )
					{
						puts("ERR");
					}
					if( fabs( sqr(vx[tot]-x[j])+sqr(vy[tot]-y[j])-sqr(r[j]) )>zero )
					{
						puts("ERR");
					}*/
					tot++;

					if( del > zero )
					{
						xx = 0.5*(-B+del)/A;
						vx[tot] = x0 + xx*dx;
						vy[tot] = y0 + xx*dy;
/*
					if( fabs( sqr(vx[tot]-x[i])+sqr(vy[tot]-y[i])-sqr(r[i]) )>zero )
					{
						puts("ERR");
					}
					if( fabs( sqr(vx[tot]-x[j])+sqr(vy[tot]-y[j])-sqr(r[j]) )>zero )
					{
						puts("ERR");
					}
					*/
						tot++;
					}
				}
			}
		}
	}

	long long ss,all = (1LL<<n)-1;
	for(int i=0;i<tot;i++)
	{
		S[i] = 0;
		ss = 1;
		for(int j=0;j<n;j++,ss*=2) if( sqr(vx[i]-x[j])+sqr(vy[i]-y[j]) -zero < sqr(r[j]) )
			S[i]+=ss;
		if( S[i]==all ) return true;
	}

	for(int i=0;i<tot;i++)
	for(int j=i+1;j<tot;j++) if( (S[i]|S[j])==all ) return true;

	return false;
}
int main()
{
	freopen("D-large.in","r",stdin);
	int T;
	scanf("%d",&T);
	for(int num=1;num<=T;num++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d%d%d",x+i,y+i,R+i);

		double l=0,r=1000,mid;
		while( r-l > eps )
		{
			mid = 0.5*(l+r);
			if(good(mid)) r=mid;else l=mid;
		}
		printf("Case #%d: %.10lf\n",num,r);

	}
	return 0;
}
