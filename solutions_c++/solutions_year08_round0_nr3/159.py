#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define pi 3.1415926535897932384626433832795

double f,R,t,r,g,A,a=0.0;

double getcl(double p)
{
	return sqrt((R-t-f)*(R-t-f)-p*p);
}

double getca(double rad)
{
	return rad*rad*3.1415926535897932384626433832795;
}

double dist(double x,double y)
{
	return sqrt(x*x+y*y);
}

double findarea(double posx,double posy,double l,double ra)
{
	double ta=0.0;
	if(dist(posx+f,posy+g-f)<=ra-f && dist(posx+g-f,posy+f)<=ra-f)
	{
		double td1 = getcl(posx+g-f)-posy-f,td2 = getcl(posy+g-f)-posx-f;
		double x=g-f-f;
		ta+=(x)*(x)-(x-td1)*(x-td2)/2.0;
		double hyp=sqrt((x-td1)*(x-td1)+(x-td2)*(x-td2));
		hyp/=2.0;
		double td3=sqrt((ra-f)*(ra-f)-hyp*hyp);
		double ang = asin(hyp/(ra-f));
		ang*=2.0;
		double as=(ra-f)*(ra-f)*ang/2.0;
		ta+=as-td3*hyp;

	}
	else if(dist(posx+f,posy+g-f)<=ra-f)
	{
		double td1 = getcl(posy+g-f)-posx-f,td2=getcl(posy+f)-posx-f-td1,hyp,x=g-f-f;
		ta+=td1*(g-f-f);
		ta+=(td2)*x/2.0;
		hyp=sqrt(x*x+td2*td2);hyp/=2.0;
		double td3=sqrt((ra-f)*(ra-f)-hyp*hyp);
		double ang = asin(hyp/(ra-f));ang*=2.0;
		double as=(ra-f)*(ra-f)*ang/2.0;
		ta+=(as-td3*hyp);
	}
	else if(dist(posx+g-f,posy+f)<=ra-f)
	{
		double td1 = getcl(posx+g-f)-posy-f,td2=getcl(posx+f)-posy-f-td1,hyp,x=g-f-f;
		ta+=td1*(g-f-f);
		ta+=(td2)*x/2.0;
		hyp=sqrt(x*x+td2*td2);hyp/=2.0;
		double td3=sqrt((ra-f)*(ra-f)-hyp*hyp);
		double ang = asin(hyp/(ra-f));ang*=2.0;
		double as=(ra-f)*(ra-f)*ang/2.0;
		ta+=(as-td3*hyp);
	}
	else
	{
		double td1 = getcl(posx+f)-posy-f,td2=getcl(posy+f)-posx-f,hyp;
		ta=td1*td2/2.0;
		hyp=sqrt(td1*td1+td2*td2);hyp/=2.0;
		double td3=sqrt((ra-f)*(ra-f)-hyp*hyp);
		double ang = asin(hyp/(ra-f));ang*=2.0;
		double as=(ra-f)*(ra-f)*ang/2.0;
		ta+=(as-td3*hyp);
	}
	return ta;
}

void main()
{
	int probnum,numtest;
	string ins;
	cin>>numtest;
	for(probnum=0;probnum<numtest;probnum++)
	{
		int i,j,k;
		printf("Case #%d: ",probnum+1);
		double x,y,z=1.0;
		a=0.0;
		cin>>f>>R>>t>>r>>g;
		if(g/2.0<=f){ printf("%.6lf\n",1.0);continue;}
		A = getca(R);
		double s=R-t;
		double rs=s,posx=r,posy=r;
		while(posx<=s)
		{
			posy=r;
			y= sqrt((R-t)*(R-t)-posx*posx);
			while(posy<y)
			{
				if(dist(posx+g,posy+g)<=s)
					a+=((g-f-f)*(g-f-f));
				else
				{
					if(dist(posx+f,posy+f)<=(s-f))
					{
						a+= findarea(posx,posy,g,s);
					}
				}
				posy+=g+r+r;
			}
			posx+=g+r+r;
		}
		a*=4.0;
		printf("%.6lf\n",(A-a)/A);
	}
}