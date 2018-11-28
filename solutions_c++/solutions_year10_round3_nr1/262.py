#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<cstring>
#include<string>
#include<map>
#include<queue>
#include<cmath>
#include<vector>
#include<bitset>
#include<sstream>
using namespace std;
#define sign(a) ((a)>0?1:(((a)<0?-1:0)))
struct point{int x,y;};
struct line{point a,b;}a[1234];
int xmult(point p1,point p2,point p0){
	return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y);
}


int dot_online_in(point p,line l)
{
	return !xmult(p,l.a,l.b)&&(l.a.x-p.x)*(l.b.x-p.x)<=0&&(l.a.y-p.y)*(l.b.y-p.y)<=0;
}

int dots_inline(point p1,point p2,point p3)
{
	return !xmult(p1,p2,p3);
}
int same_side(point p1,point p2,line l)
{
	return sign(xmult(l.a,p1,l.b))*xmult(l.a,p2,l.b)>0;
}

int intersect_in(line u,line v)
{
	if (!dots_inline(u.a,u.b,v.a)||!dots_inline(u.a,u.b,v.b))
		return !same_side(u.a,u.b,v)&&!same_side(v.a,v.b,u);
	return dot_online_in(u.a,v)||dot_online_in(u.b,v)||dot_online_in(v.a,u)||dot_online_in(v.b,u);
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
			cin>>a[i].a.x>>a[i].b.x,a[i].a.y=1,a[i].b.y=10;
		int da=0;
		for(int i=0;i<n;i++)
			for(int q=i+1;q<n;q++)
				da+=intersect_in(a[i],a[q]);
		printf("Case #%d: %d\n",cas++,da);
	}


}