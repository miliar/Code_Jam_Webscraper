#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf (1<<30)
#define clr(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define eps 1e-12

struct abc
{
	double x,y,z,vx,vy,vz;
}aa[550];
struct point
{
	double x,y,z;
};
int n;
int main()
{
	freopen("B-large.in","r",stdin);
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1,i;
	double tmn,dmn,p,q,r,u,v,w,a,b,c;
	cin>>cs;
	while(cs--)
	{
		cin>>n;
		p=q=r=u=w=v=0;
		for(i=0;i<n;i++)
		{
			cin>>aa[i].x>>aa[i].y>>aa[i].z>>aa[i].vx>>aa[i].vy>>aa[i].vz;
			p+=aa[i].x;
			q+=aa[i].y;
			r+=aa[i].z;
			u+=aa[i].vx;
			v+=aa[i].vy;
			w+=aa[i].vz;
		}
		p/=n;
		q/=n;
		r/=n;
		u/=n;
		v/=n;
		w/=n;
		a=u*u+v*v+w*w;
		b=2*(p*u+q*v+r*w);
		c=p*p+q*q+r*r;
		if(a>eps)
			tmn=-b/(2*a);
		else
			tmn=0;
		if(tmn<eps)
			tmn=0;
		dmn=a*tmn*tmn;
		dmn+=b*tmn;
		dmn+=c;
		if(dmn<eps)
			dmn=0;
		dmn=sqrt(dmn);
		printf("Case #%d: %.8lf %.8lf\n",t++,dmn,tmn);
	}
	return 0;
}


