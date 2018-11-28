#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <cmath>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#define fr(a,b,c) for (int a=b;a<=c;a++)
#define frr(a,b,c) for (int a=b;a>=c;a--)
#define rep(a,b) for (int a=0;a<b;a++)
#define repp(a,b) for (int a=b-1;a>=0;a--)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define pii pair<int,int>
#define oo 1000111222
#define maxN 1
using namespace std;
const int dx[2][4]={{1,0,-1,0},{0,1,0,-1}};
const int dy[2][4]={{0,1,0,-1},{1,0,-1,0}};
const double eps2=1e-9;

int n,W,L,r[1010],d[1010],type;
double x[1010],y[1010];

double dist(double x,double y,double xx,double yy)
{
	return sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy));
}

int lessThan(double x,double y)
{
	return x-1e-7<y;
}

int find(double x0,double y0,double x1,double y1,double &X,double &Y,double R,int z)
{
	double xm=(x0+x1)/2,ym=(y0+y1)/2;
	fr(i,1,z-1)
	{
		double cx=x[d[i]],cy=y[d[i]];
		int cnt=0;
		cnt+=lessThan(dist(cx,cy,x0,y0),R+r[i]);
		cnt+=lessThan(dist(cx,cy,x0,y1),R+r[i]);
		cnt+=lessThan(dist(cx,cy,x1,y0),R+r[i]);
		cnt+=lessThan(dist(cx,cy,x1,y1),R+r[i]);
		if (cnt==4) return 0;
	}
	
	if (fabs(x0-x1)<eps2 && fabs(y0-y1)<eps2) 
	{
		X=xm; Y=ym;
		return 1;
	}
	else
	{
		if (find(x0,y0,xm,ym,X,Y,R,z)) return 1;
		if (find(x0,ym,xm,y1,X,Y,R,z)) return 1;
		if (find(xm,y0,x1,ym,X,Y,R,z)) return 1;
		if (find(xm,ym,x1,y1,X,Y,R,z)) return 1;
	}
	return 0;
}

int main()
{
	freopen("bsmall.in","r",stdin); freopen("bsmall.out","w",stdout);
	int test;
	cin >> test;
	for (int itest=1;itest<=test;itest++)
	{
		cin >> n >> W >> L;
		fr(i,1,n) cin >> r[i], d[i]=i;
		fr(i,1,n) fr(j,i+1,n)
			if (r[i]<r[j]) swap(r[i],r[j]), swap(d[i],d[j]);
			
		fr(i,1,n) find(0,0,W,L,x[d[i]],y[d[i]],r[i],i);
			
		printf("Case #%d:",itest);
		fr(i,1,n) printf(" %.9lf %.9lf",x[i],y[i]);
		puts("");
	}
}
