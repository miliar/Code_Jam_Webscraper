#include <iostream>
#include <cmath>
using namespace std;

const double eps = 1e-11;
const double pi = acos(-1.0);
int dblcmp(double a)
{
	if(fabs(a)<eps) return 0;
	if(a<0.0) return -1;
	return 1;
}

struct pt
{
	double x;
	double y;
};

pt operator+(pt &a,pt &b)
{
	pt res;
	res.x=a.x+b.x;
	res.y=a.y+b.y;
	return res;
}

pt operator-(pt &a,pt &b)
{
	pt res;
	res.x=a.x-b.x;
	res.y=a.y-b.y;
	return res;
}

pt operator*(double a,pt &b)
{
	pt res;
	res.x=a*b.x;
	res.y=a*b.y;
	return res;
}

double f,R,t,r,g;

bool circle_cross_line(pt p3,double rr,pt p1,pt p2,pt &res)
{
	double a,b,c;
	double deta,u=-1.0,u1,u2;
	pt ptt;
	a=(p2.x-p1.x)*(p2.x-p1.x)+(p2.y-p1.y)*(p2.y-p1.y);
	b=2.0*((p2.x-p1.x)*(p1.x-p3.x)+(p2.y-p1.y)*(p1.y-p3.y));
	c=p3.x*p3.x+p3.y*p3.y+p1.x*p1.x+p1.y*p1.y-2.0*(p3.x*p1.x+p3.y*p1.y)-rr*rr;
	deta=b*b-4.0*a*c;
	if(dblcmp(deta)<0) return false;
	deta=sqrt(deta);
	u1=(-b+deta)/(2.0*a);
	u2=(-b-deta)/(2.0*a);
	if(dblcmp(u1)>=0&&dblcmp(u1-1.0)<=0)
		u=u1;
	if(dblcmp(u2)>=0&&dblcmp(u2-1.0)<=0)
		u=u2;
	if(dblcmp(u)<0) return false;
	ptt=p2-p1;
	ptt=u*ptt;
	res=p1+ptt;
	return true;
}

double little(pt a,pt b,double rr)
{
	double ang1,ang2,ang;
	double res;
	ang1=asin(a.y/rr);
	ang2=asin(b.y/rr);
	ang=fabs(ang1-ang2);
	res=ang*rr*rr*0.5;
	res-=0.5*rr*rr*sin(ang);
	return res;
}

double square(pt a,pt p3,double Gg,double rr)
{
	pt b,c,d;
	pt r1,r2;
	double res=0.0;
	b.x=a.x+Gg;
	b.y=a.y;
	c.x=a.x+Gg;
	c.y=a.y+Gg;
	d.x=a.x;
	d.y=a.y+Gg;
	if(circle_cross_line(p3,rr,a,b,r1)&&circle_cross_line(p3,rr,a,d,r2))
	{
		res=little(r1,r2,rr);
		res+=0.5*(r1.x-a.x)*(r2.y-a.y);
	}
	else if(circle_cross_line(p3,rr,a,b,r1)&&circle_cross_line(p3,rr,c,d,r2))
	{
		res=little(r1,r2,rr);
		res+=0.5*(r1.x-a.x+r2.x-a.x)*Gg;
	}
	else if(circle_cross_line(p3,rr,b,c,r1)&&circle_cross_line(p3,rr,a,d,r2))
	{
		res=little(r1,r2,rr);
		res+=0.5*(r1.y-a.y+r2.y-a.y)*Gg;
	}
	else if(circle_cross_line(p3,rr,b,c,r1)&&circle_cross_line(p3,rr,c,d,r2))
	{
		res=little(r1,r2,rr);
		res+=Gg*Gg-0.5*(c.x-r2.x)*(c.y-r1.y);
	}
	else
	{
		printf("error\n");
	}
	return res;
}

double work()
{
	double Rr=R-t-f;
	double Gg=g-2.0*f;
	double rr=r+f;
	double total=0.0;
	double all;
	bool ok;
	pt last,now,org;
	if(dblcmp(Rr-rr)<=0) return 1.0;
	if(dblcmp(Gg)<=0) return 1.0;
	last.x=-Gg-rr;
	last.y=-Gg-rr;
	org.x=0.0;
	org.y=0.0;
	for(int i=0;;++i)
	{
		ok=true;
		last.y+=Gg+2.0*rr;
		now=last;
		for(int j=0;;++j)
		{
			now.x+=Gg+2.0*rr;
			if(dblcmp(now.x*now.x+now.y*now.y-Rr*Rr)>=0)
			{
				if(j==0) ok=false;
				break;
			}
			if(dblcmp((now.x+Gg)*(now.x+Gg)+(now.y+Gg)*(now.y+Gg)-Rr*Rr)>0)
				total+=square(now,org,Gg,Rr);
			else total+=Gg*Gg;
		}
		if(!ok) break;
	}
	total*=4.0;
	all=pi*R*R;
	return 1.0-total/all;
}

int main()
{
	int n;
	double res;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		res=work();
		printf("Case #%d: %.6lf\n",i+1,res);
	}
	return 0;
}
