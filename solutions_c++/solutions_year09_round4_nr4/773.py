#include <cstdio>
#include <cmath>

int n,x[40],y[40],r[40];

double cx1,cy1,cr1,cx2,cy2,cr2,ans=1e9;

double dist(double xx1,double yy1,double xx2,double yy2)
{
	return sqrt((xx1-xx2)*(xx1-xx2)+(yy1-yy2)*(yy1-yy2));
}

void solve3(double x1,double y1,double r1,double x2,double y2,double r2,double x3,double y3,double r3,double &ax1,double &ay1,double &ar1,double &ax2,double &ay2,double &ar2)
{
	double a1=2*(x2-x1),b1=2*(y2-y1),c1=2*(r2-r1),d1=r1*r1-r2*r2-x1*x1+x2*x2-y1*y1+y2*y2;
	double a2=2*(x3-x1),b2=2*(y3-y1),c2=2*(r3-r1),d2=r1*r1-r3*r3-x1*x1+x3*x3-y1*y1+y3*y3;
	double det=a1*b2-a2*b1;
	double e=(b2*c1-b1*c2)/det,f=(b2*d1-d2*b1)/det-x1;
	double g=(a1*c2-a2*c1)/det,h=(a1*d2-a2*d1)/det-y1;
	double A=e*e+g*g-1,B=2*e*f+2*g*h+2*r1,C=f*f+h*h-r1*r1;
	double T=sqrt(B*B-4*A*C);
	ar1=(-B+T)/(2*A);
	ax1=e*ar1+f+x1;
	ay1=g*ar1+h+y1;
	ar2=(-B-T)/(2*A);
	ax2=e*ar2+f+x1;
	ay2=g*ar2+h+y1;
}

void check()
{
	for(int i=0;i<n;++i)
	{
		if(dist(x[i],y[i],cx1,cy1)<=cr1-r[i]+1e-6) continue;
		if(dist(x[i],y[i],cx2,cy2)<=cr2-r[i]+1e-6) continue;
		return;
	}
	double aaaa=cr1;
	if(cr2>aaaa) aaaa=cr2;
	if(aaaa<ans) ans=aaaa;
}

void work2()
{
	for(int j=0;j<n;++j)
	{
		cx2=x[j];
		cy2=y[j];
		cr2=r[j];
		check();
	}
	for(int j=0;j<n;++j)
		for(int k=j+1;k<n;++k)
		{
			double d=dist(x[j],y[j],x[k],y[k]);
			cr2=(d+r[j]+r[k])/2;
			double l=(cr2-r[j])/d;
			cx2=l*x[k]+(1-l)*x[j];
			cy2=l*y[k]+(1-l)*y[j];
			check();
		}
	for(int j=0;j<n;++j)
		for(int k=j+1;k<n;++k)
			for(int l=k+1;l<n;++l)
			{
				double tx2,ty2,tr2;
				solve3(x[j],y[j],r[j],x[k],y[k],r[k],x[l],y[l],r[l],cx2,cy2,cr2,tx2,ty2,tr2);
				check();
				cx2=tx2;
				cy2=ty2;
				cr2=tr2;
				check();
			}
}

int main()
{
	freopen("D-small-attempt3.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d: ",i+1);
		ans=1e9;
		scanf("%d",&n);
		for(int j=0;j<n;++j)
			scanf("%d%d%d",x+j,y+j,r+j);
		for(int j=0;j<n;++j)
		{
			cx1=x[j];
			cy1=y[j];
			cr1=r[j];
			work2();
		}
		for(int j=0;j<n;++j)
			for(int k=j+1;k<n;++k)
			{
				double d=dist(x[j],y[j],x[k],y[k]);
				cr1=(d+r[j]+r[k])/2;
				double l=(cr1-r[j])/d;
				cx1=l*x[k]+(1-l)*x[j];
				cy1=l*y[k]+(1-l)*y[j];
				work2();
			}
		for(int j=0;j<n;++j)
			for(int k=j+1;k<n;++k)
				for(int l=k+1;l<n;++l)
				{
					double tx2,ty2,tr2;
					solve3(x[j],y[j],r[j],x[k],y[k],r[k],x[l],y[l],r[l],cx1,cy1,cr1,tx2,ty2,tr2);
					work2();
					cx1=tx2;
					cy1=ty2;
					cr1=tr2;
					work2();
				}
		printf("%lf\n",ans);
	}
	return 0;
}

