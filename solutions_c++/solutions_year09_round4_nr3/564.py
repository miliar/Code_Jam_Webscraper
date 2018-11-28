#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <queue>
#include <complex>
#include <ctime>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

#define Type long double

typedef complex<Type> point;

#define X           	real()
#define Y           	imag()
#define Len(x)     		(hypot((x).X,(x).Y))
#define vect(x,y)  		((y)-(x))
#define dot(a,b)   		((conj(a)*(b)).X)
#define cross(a,b)      ((conj(a)*(b)).Y)
#define normalize(a)    ((a)/(point(Len(a),0)))
#define angle(a)        (atan2((a).Y,(a).X)) 
#define EPS         	1e-9
#define PI         		(2*acos(0))
#define rotate(x,a)     ((x)*exp(point(0,(a))))

/*
	Checks if line p1,p2 intersects line a,b 
	if true 
		point p is point of intersection
*/
bool LineIntersect(const point & p1,const point & p2, const point & a,const point & b,point & p)
{
	if(p1 == a )
	{	
		p=a;
		return true;
	}
	if(p2 == b)
	{
		p=b;
		return true;
	}
	if(p2 == a)
	{
		p=a;
		return true;
	}
	if(p2 == b)
	{
		p=b;
		return true;
	}
	Type c1 = cross(vect(p1,a),vect(p1,p2));
	Type c2 = cross(vect(p1,b),vect(p1,p2));
	
	if(fabs(c1-c2)<EPS)	//Parallel 
		return false;
	
	p = (c1 * b - c2 * a)/(c1-c2);
	return true;
}

/*
	Checks if point p lies on the ray from p1 passing through p2
*/
bool isPointOnRay(const point& p1,const point& p2,const point & p)
{
	if(fabs(Len(p-p1))<EPS)	//p is p1
		return true;
	return fabs(Len( normalize(vect(p1,p)) - normalize(vect(p1,p2)) ) )<EPS;
}

/*
	Checks if p lies on the line segment p1,p2
*/

bool pointOnSegment(const point &p1,const point & p2,const point & p)
{
	return isPointOnRay(p1,p2,p) && isPointOnRay(p2,p1,p);
}

bool intersect(int ay,int by,int py,int qy,int bx,int qx)
{
	point a(bx-1,ay),b(bx,by),p(qx-1,py),q(qx,qy),pp;
	return LineIntersect(a,b,p,q,pp)&&pointOnSegment(a,b,pp)&&pointOnSegment(p,q,pp);
}

int pts[103][30];
int n,k;
int mat[100][100];
int mem[(1<<17)];
int vv[(1<<17)];

int f(int mask)
{
	if(mask == 0)
		return 0;
	int&r=mem[mask];
	if(r!=-1)
		return r;
	r=10000000;
	for(int i = mask;i;i=(i-1)&mask)
	{
		if(!vv[i])
			r<?=f(mask&(~i))+1;
	}
	return r;
}

int main()
{
	#ifndef ONLINE_JUDGE
	freopen("c.in","rt",stdin);
	freopen("out.out","wt",stdout);
	#endif
	int t;
	scanf("%d",&t);
	rep(tt,0,t)
	{
		scanf("%d %d",&n,&k);
		memset(mat,0,sizeof(mat));
		memset(vv,0,sizeof(vv));
		rep(i,0,n)
			rep(j,0,k)
				scanf("%d",&pts[i][j]);
		rep(i,0,n)
			rep(j,i+1,n)
			{
				rep(l,1,k)
					rep(m,1,k)
					{
						if(intersect(pts[i][l-1],pts[i][l],pts[j][m-1],pts[j][m],l,m))
						{
							mat[i][j]=mat[j][i]=1;
							goto bara;
						}
					}
				bara:;
			}
		vector<int>v;
		rep(i,0,1<<n)
		{
			v.clear();
			rep(j,0,n)
				if((i>>j)&1)
					v.PB(j);
			rep(j,0,v.size())
				rep(kk,j+1,v.size())
					if(mat[v[j]][v[kk]])
					{
						vv[i]=1;
						goto bara1;
					}
			bara1:;
		}
		memset(mem,-1,sizeof(mem));
		printf("Case #%d: %d\n",tt+1,f((1<<n)-1));
	}
	
	return 0;
}
