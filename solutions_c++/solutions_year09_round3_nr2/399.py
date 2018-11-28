#include <iostream>
#include <cmath>

#define MAXN 1010

using namespace std;


int N;
double dmin,tmin,x[MAXN],y[MAXN],z[MAXN],vx[MAXN],vy[MAXN],vz[MAXN];

inline double sqr(double x)
{
	return x*x;
}

void run()
{
	int i;
	double p1,p2,p3,q1,q2,q3,A,B,C;
	p1=p2=p3=q1=q2=q3=0.000000;
	for (i=1;i<=N;i++)
	{
		p1+=x[i];
		p2+=y[i];
		p3+=z[i];
		q1+=vx[i];
		q2+=vy[i];
		q3+=vz[i];
	}
	A=sqr(q1)+sqr(q2)+sqr(q3);
	B=2*(p1*q1+p2*q2+p3*q3);
	C=sqr(p1)+sqr(p2)+sqr(p3);
	if (abs(A-0.00000)<1e-9)
	{
		if (abs(B-0.00000)<1e-9)
			tmin=0;
		else
			tmin=-C/B;
	}
	else
		tmin=-(B/(2*A));
	if (tmin<0.0000)
		tmin=0;
	dmin=A*sqr(tmin)+B*tmin+C;
	if (abs(dmin-0.00000)<1e-7)
		dmin=0.00;
	dmin=sqrt(dmin)/((double)N);
}

void ini()
{
	int i,k,T;
	cin>>T;
	for (i=1;i<=T;i++)
	{
		cin>>N;
		for (k=1;k<=N;k++)
		{
			//x y z vx vy vz
			cin>>x[k]>>y[k]>>z[k]>>vx[k]>>vy[k]>>vz[k];
		}
		run();
		//Case #X: dmin tmin
		printf("Case #%d: %lf %lf\n",i,dmin,tmin);
	}
}



int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	ini();
	return 0;
}
	
	
