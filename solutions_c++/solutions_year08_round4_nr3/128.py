#include <cstdio>
#include <algorithm>
#include <cmath>
#define eps 0.00000001
using namespace std;

int n, T, t;

double x[1001], y[1001], z[1001], p[1001];

int w[8];

int ww[128][6];
int N;


inline void afis()
{++N;
	for(int i=1;i<=3;++i) ww[N][i]=w[i];
}

		
	

inline void back(int k)
{
	if(k==4) afis();
	else
	{
		w[k]=0;
		back(k+1);
		w[k]=1;
		back(k+1);
		w[k]=-1;
		back(k+1);
	}
}


int main()
{
	back(1);
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d\n", &T);
	int i, j;
	double d, dm;
	
//	for(i=1;i<=N;++i) printf("%d %d %d\n", ww[i][1], ww[i][2], ww[i][3]);
	
	
	for(t=1;t<=T;++t)
	{
		scanf("%d\n", &n);
		for(i=1;i<=n;++i) scanf("%lf %lf %lf %lf\n", &x[i], &y[i], &z[i], &p[i]);
		
		double dd=0x3f3f3f3f;
		
		double X=0, Y=0,Z=0;
		
		for(i=1;i<=n;++i) X+=x[i], Y+=y[i], Z+=z[i];
		X=X/(double)n;
		Y=Y/(double)n;
		Z=Z/(double)n;
		
		double Q=1000000;
		
		double nx,ny, nz, D;
		nx=X;ny=Y;nz=Z;
		dm=0;
			
			for(j=1;j<=n;++j)
				
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
			
		D=dm;
			
		//printf("%lf\n", D);
		
		
		int ok=1;
		while(Q>eps)
		{
				ok=1;
				
				
			for(i=1;i<=N &&ok;++i)
			{
				
			nx=X+Q*ww[i][1];
			ny=Y+Q*ww[i][2];
			nz=Z+Q*ww[i][3];
			
			
			dm=0;
		
			for(j=1;j<=n;++j)
				
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;//,X=nx, Y=ny, Z=nz;
				}
				
			
			if(dm<D){ D=dm;X=nx; Y=ny; Z=nz; ok=0;}
			}
			
			//printf("%lf\n", D);
			if(ok) Q=Q/2.0;	
				
			//
			/*
			nx=X-Q;
			ny=Y;
			nz=Z;
			
			
			dm=0;
			//ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X+Q;
			ny=Y+Q;
			nz=Z;
			
			
			dm=0;
			//ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X+Q;
			ny=Y;
			nz=Z+Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
			
				//
			nx=X;
			ny=Y+Q;
			nz=Z+Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X+Q;
			ny=Y+Q;
			nz=Z+Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
			
				//
			nx=X-Q;
			ny=Y-Q;
			nz=Z;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X-Q;
			ny=Y;
			nz=Z-Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X;
			ny=Y-Q;
			nz=Z-Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X-Q;
			ny=Y-Q;
			nz=Z-Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
			
				//
			nx=X+Q;
			ny=Y-Q;
			nz=Z;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X+Q;
			ny=Y;
			nz=Z-Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
			
				//
			nx=X+Q;
			ny=Y-Q;
			nz=Z-Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X-Q;
			ny=Y+Q;
			nz=Z;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
			
				//
			nx=X;
			ny=Y+Q;
			nz=Z-Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			
				//
			nx=X+Q;
			ny=Y-Q;
			nz=Z+Q;
			
			
			dm=0;
			ok=1;
			for(j=1;j<=n;++j)
				if(i!=j)
				{
					d=(fabs(nx-x[j])+fabs(ny-y[j])+fabs(nz-z[j]))/(double)p[j];
					if(dm<d) dm=d;
				}
				
			
			if(dm<D){ D=dm; ok=0;}
			*/
		//	printf("%lf\n", dm);
			
			
		}
		
		
		printf("Case #%d: %lf\n", t, D);
	}
	return 0;
}

				