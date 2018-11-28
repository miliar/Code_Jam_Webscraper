#include<iostream>
#include<cmath>
using namespace std;
struct node 
{
	double x,y,z;
	double vx,vy,vz;

}stu[510];

const double eps=1e-10;
int main()
{
	int t;
	int n;
	freopen("G:\\B-large.in","r",stdin);
	freopen("G:\\B-large.out","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;++cas)
	{
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			cin>>stu[i].x>>stu[i].y>>stu[i].z>>stu[i].vx>>stu[i].vy>>stu[i].vz;
		double a,b,c,d,e,f;
		double res=0.0;
		for(int i=0;i<n;++i)
			res+=stu[i].x;
		a=res/n;
		res=0.0;
		for(int i=0;i<n;++i)
			res+=stu[i].y;
		c=res/n;
		res=0.0;
		for(int i=0;i<n;++i)
			res+=stu[i].z;
		e=res/n;
		res=0.0;
		for(int i=0;i<n;++i)
			res+=stu[i].vx;
		b=res/n;
		res=0.0;
		for(int i=0;i<n;++i)
			res+=stu[i].vy;
		d=res/n;
		res=0.0;
		for(int i=0;i<n;++i)
			res+=stu[i].vz;
		f=res/n;
		double aa,bb,cc;
		aa=b*b+d*d+f*f;
		bb=a*b+c*d+e*f;
		bb*=2.0;
		cc=a*a+c*c+e*e;	
		double resdis,rest;
		if(fabs(aa)<eps)
		{
			if(fabs(bb)<eps)
			{
				rest=0.0;
				resdis=cc;
			}
			else
			{
				rest=(-1)*cc/bb;
				if(rest<0)
				{
					rest=0.0;
					resdis=cc;
				}
				else
				{
					resdis=bb*rest+cc;
				}
			}
		}
		else
		{
			rest=(-1.0)*bb/2.0;
			rest/=aa;
			if(rest<0)
			{
				rest=0.0;
				resdis=cc;
			}
			else
			{
				resdis=aa*rest*rest+bb*rest+cc;
			}
		}
		if(fabs(resdis)<eps)
			resdis=0.0;
		else
			resdis=sqrt(fabs(resdis));
		printf("Case #%d: %.8lf %.8lf\n",cas,resdis,fabs(rest));
	}
	return 0;
}