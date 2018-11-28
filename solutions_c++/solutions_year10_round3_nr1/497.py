#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("R1A.in","r");
FILE *out=fopen("R1A.out","w");

int x[1100],y[1100];

int ver;

class point{
public:
	long double x;
	long double y;
	point(){}point(long double x1,long double y1){
		x=x1;
		y=y1;
	}
};
class line{
public:
	point f;
	point s;
	long double a;
	long double b;
	long double c;
};
point operator+(point a,point b)
{
	point ret;
	ret.x=a.x+b.x;
	ret.y=a.y+b.y;
	return ret;
}
point operator-(point a,point b)
{
	point ret;
	ret.x=a.x-b.x;
	ret.y=a.y-b.y;
	return ret;
}
long double operator^(point a,point b)
{
	return a.x*b.y-a.y*b.x;
}
long double operator*(point a,point b)
{
	return a.x*b.x+a.y*b.y;
}
line ptl(point a,point b)
{
	line ret;
	ret.f=a;
	ret.s=b;
	ret.a=b.y-a.y;
	ret.b=a.x-b.x;
	ret.c=ret.a*a.x+ret.b*a.y;
	return ret;
}
bool pbtl(point a,line b)
{
	if(fabs(a.x*b.a+a.y*b.b-b.c)<=1e-7)return true;
	return false;
}
bool pbts(point a,line b)
{
	if(pbtl(a,b) && a.x>=min(b.f.x,b.s.x) && a.x<=max(b.f.x,b.s.x)  && a.y>=min(b.f.y,b.s.y) && a.y<=max(b.f.y,b.s.y))return 1;
	return 0;
}
line fixline(line a)
{
	if(a.f.x>a.s.x)
		a=ptl(a.s,a.f);
	return a;
}
point inter(line a,line b,bool vis)
{
	point ret;
	ret.x=0;
	ret.y=0;
	long double d;
	ver=0;
	a=fixline(a);
	b=fixline(b);
	d=a.a*b.b-a.b*b.a;
	if(fabs(d)<EPS){
		if(pbts(a.f,b))return ret;
		if(pbts(a.s,b))return ret;
		if(pbts(b.f,a))return ret;
		if(pbts(b.s,a))return ret;
		ver=1;
		return ret;
	}
	ret.x=(b.b*a.c-a.b*b.c)/d;
	ret.y=(a.a*b.c-b.a*a.c)/d;
	if(ret.x==-0)ret.x=0;
	if(ret.y==-0)ret.y=0;
	if(vis){
		if(!pbts(ret,a) || !pbts(ret,b))ver=1;
	}
	return ret;
}
long double dist(point a,point b,point c,bool vis)
{
	long double d=((b-a)^(c-a))/sqrt((b-a)*(b-a));
	if(!vis)return fabs(d);
	long double x=(c-b)*(b-a);
	if(x+EPS>0)return sqrt((b-c)*(b-c));
	x=(c-a)*(a-b);
	if(x+EPS>0)return sqrt((a-c)*(a-c));
	return fabs(d);
}
line ax[1100];
int main()
{
	int i,j,n,k;
	int tests;
	fscanf(in,"%d",&tests);
	for(int test=0;test<tests;test++){
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)fscanf(in,"%d%d",&x[i],&y[i]);
		int ret=0;
		for(i=0;i<n;i++){
			ax[i]=ptl(point(1,x[i]),point(5,y[i]));
		}
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				ver=0;
				inter(ax[i],ax[j],1);
				if(!ver)ret++;
			}
		}
		fprintf(out,"Case #%d: %d\n",test+1,ret);
	}
	return 0;
}