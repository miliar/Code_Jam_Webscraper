#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>

#include <set>
#include <vector>
#include <utility>
#include <map>

#include <algorithm>
#include <cassert>

using namespace std;


typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;

typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define pb push_back
#define forn(i,N) for(int i=0;i<(N); ++i)

//FILE * f = fopen("a.in","rt",stdin);
//FILE * g = fopen("c-large.out","wt");
ifstream f("c-large.in",ifstream::in);
ofstream g("c-large.out",ofstream::out);

typedef long double ld;
ld pi = 3.14159265358979323846;

ld Integ(ld R, ld x)
{
	ld d = R*R-x*x;
	if (d<=0) return pi*R*R/4;
	ld res = 0.5 * ( atan2(x,sqrt(d))*R*R + x*sqrt(d));
	return res;
}
ld Integrate(ld R, ld a, ld b)
{
	ld res = Integ(R,b)-Integ(R,a);
	assert(res>=(b-a)*sqrt(R*R-b*b));
	assert(res<=(b-a)*sqrt(R*R-a*a));
	return res;
}

ld getsurf(ld R, vector<pair<ld,ld> >& lines)
{
	ld result = 0;
	forn(i,lines.size())
		result += Integrate(R,lines[i].first,lines[i].second);
	return result;
}

vector<pair<ld,ld> > getLines(ld R, ld x, ld w)
{
	ld a = x;
	ld b = x+w;
	vector<pair<ld,ld> > result;
	while (a<R)
	{
		result.pb(pair<ld,ld>(a,min(R,b)));
		a=b+2*x;
		b=a+w;
	}
	return result;

}

ld getInter(ld R, pair<ld,ld> l1, pair<ld,ld> l2)
{
	ld x1 = l1.first;
	ld x2 = l1.second;
	
	ld y1 = l2.first;
	ld y2 = l2.second;

	ld yy2=sqrt(R*R-x1*x1);
	ld yy1=sqrt(R*R-x2*x2);

	if (yy2<=y1) return 0; //sorry, no intersection
	if (yy1>=y2) return (x2-x1)*(y2-y1);//full intersection
	if (yy1>=y1 && yy2<=y2) // lower inside, upper inside
		return Integrate(R,x1,x2)-(x2-x1)*y1;
	
	if (yy1<=y1 && yy2<=y2) //lower is below, upper is inside
	{
		ld x = sqrt(R*R-y1*y1);
		return Integrate(R,x1,x)-(x-x1)*y1;
	}
	
	if (yy1>=y1 && yy2>=y2) //lower is inside, upper is above
	{
		return Integrate(R,yy1,y2)-(y2-yy1)*x1 + (x2-x1)*(yy1-y1);
	}

	if (yy1<=y1 && yy2>=y2) // lower is below, upper is above
	{
		ld xx1 = sqrt(R*R-y2*y2);
		ld xx2 = sqrt(R*R-y1*y1);
		return Integrate(R,xx1,xx2)-(xx2-xx1)*y1+(xx1-x1)*(y2-y1);
	}
}

ld GetIntersectionArrea(ld R, vector<pair<ld,ld> > &lines)
{
	ld result =0;
	forn(i,lines.size())
	{
		ld r = 0;
		forn(j,lines.size())
		{
			assert(getInter(R, lines[i], lines[j])>=0);
			r += getInter(R, lines[i], lines[j]);
			assert(r<(lines[i].second-lines[i].first)*lines[j].second);
			assert(r<Integrate(R,lines[i].first,lines[i].second));

		}
		assert(r<Integrate(R,lines[i].first,lines[i].second));
		result += r;
	}
	return result;
}

int main()
{
	int Tests; f>>Tests;
	string s;

	forn(TestIndex,Tests)
	{
		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": ";
		cout<<"Case #"<<TestIndex+1<<": "<<endl;
		long double fr,R,t,r,gap;
		f>>fr>>R>>t>>r>>gap;
		
		if (gap<=2*fr)
		{
			g<<"1"<<endl;
			continue;
		}
		
		vector<pair<ld,ld> > inters = getLines(R-t-fr,r+fr,gap-2*fr);
		//ld q1 = getsurf(R-t,inters);
		//count the intersections
		ld inter = GetIntersectionArrea(R-t-fr,inters);
		ld res = (4*inter)/(pi*R*R);

		g<<1-res<<endl;

	}
	return 0;
}