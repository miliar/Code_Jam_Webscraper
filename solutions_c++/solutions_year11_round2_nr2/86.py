#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <string>

#define fr(x,y) for(int x=0; x<(y); ++x)
#define fe(x,y,z) for(int x=(y); x<(z); ++x)
#define fw(x,y,z) for(int x=(y); x<=(z); ++x)
#define df(x,y,z) for(int x=(y); x>=(z); --x)
#define mn(x,y) ((x)<(y) ? (x) : (y))
#define mx(x,y) ((x)>(y) ? (x) : (y))
#define ab(x) ((x)<0 ? (-(x)) : (x))
#define MP make_pair
#define PB push_back
#define BIG 1000000000
#define X first
#define Y second
#define dbg(x) if(DEBUG) {cout<<#x<<": "<<(x)<<endl;}
#define dout(x) if(DEBUG) {cout<<x;}
#define dline(x) if(DEBUG) {cout<<x<<endl;}
#define dbgr(x,l) if(DEBUG) {cout<<#x<<": ";fr(innercounter,l) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbge(x,y,z) if(DEBUG) {cout<<#x<<": ";fe(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgw(x,y,z) if(DEBUG) {cout<<#x<<": ";fw(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgee(x,l1,l2) if(DEBUG) {cout<<#x<<": "<<endl;fr(icounter,l1){fr(jcounter,l2) cout<<x[icounter][jcounter]<<" ";cout<<endl;}}

bool DEBUG = false;

using namespace std;

int t,d,c,pos[1000000],v,p,n;

bool ok(double tim)
{
double l = pos[0]-tim;
double minim = l+d;
fe(i,1,n)
	{
	if(pos[i]>minim)
		{
		double maxim = pos[i]-tim;
		l = mx(maxim,minim);
		}	
	else 
		{
		if(pos[i]+tim+1e-9<minim) return false;
		l = minim;
		}
	minim = l+d;
	}
return true;
}

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
DEBUG = true;
#endif
scanf("%d\n", &t);
fw(test,1,t)
	{
	scanf("%d %d\n", &c, &d);
	n = 0;
	fr(i,c)
		{
		scanf("%d%d", &p, &v);
		fr(j,v)
			pos[n++] = p;
		}
	double l = 0, r = 1e13;
	double eps = 1e-4;
	while(r-l>eps)
		{
		double m = (l+r)/2;
		if(ok(m)) r = m;
		else l = m;
		if(r<1e3) eps = 1e-7;
		else if(r<1e4) eps = 1e-6;
		else if(r<1e5) eps = 1e-5;
//		else if(r<1e6) eps = 1e-4;		
		}
	double m = (l+r)/2;
	printf("Case #%d: %.9lf\n", test, m);
	}
return 0;
}
