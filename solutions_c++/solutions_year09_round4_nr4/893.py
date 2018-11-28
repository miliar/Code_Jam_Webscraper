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

#define max(a,b) ((a)>(b+eps)?(a):(b))
#define min(a,b) ((a+eps)<(b)?(a):(b))
#define pi acos(-1.0)
#define inf (1<<29)
#define clr(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define eps 1e-11

struct point
{
	double x,y;
};

struct circle
{
	point c;
	double r;
};

int n;
circle a[10];
double rsa,rsb,tmp;

double dis(point a,point b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

double fnd(circle a,circle b)
{
	double d;
	d=dis(a.c,b.c);
	d+=a.r+b.r;
	return d/2;
}

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cs,t=1,i,j,k;
	double rs;
	cin>>cs;
	while(cs--)
	{
		cin>>n;
		a[1].r=0;
		for(i=0;i<n;i++)
		{
			cin>>a[i].c.x>>a[i].c.y>>a[i].r;
		}
		rsa=inf;
		rsb=inf;
		if(n>2)
		{
			tmp=fnd(a[0],a[1]);
			if(tmp+eps<rsa)
			{
				rsa=tmp;
				rsb=a[2].r;
			}
			tmp=fnd(a[2],a[1]);
			if(tmp+eps<rsa)
			{
				rsa=tmp;
				rsb=a[0].r;
			}
			tmp=fnd(a[0],a[2]);
			if(tmp+eps<rsa)
			{
				rsa=tmp;
				rsb=a[1].r;
			}
		}
		else
		{
			rsa=a[0].r;
			rsb=a[1].r;
		}
		rs=max(rsa,rsb);
		printf("Case #%d: %.6lf\n",t++,rs+eps);
	}
	return 0;
}


