#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <deque>
#include <set>
#include <map>
using namespace std;

const int PINF = 1<<30;
const int NINF = -PINF;
const double EPSILON = 1e-10;
const double PI = M_PI;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

#define ALL(a) (a).begin(), (a).end()
#define FOR(i,a,b) for (LL i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for (int i=(a)-1,_b(b); i>=_b; --i)
#define FORV(i,v) for (int i=0; i<(v).size(); ++i)
#define ABS(a) ((a)>0?(a):-(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define mp make_pair
#define pb push_back
#define sz size()
#define sqr(a) (a)*(a)
#define pow2(n) (1<<(n))
#define has(a,k) ((a).find(k)!=(a).end())


double Rin;

double dist(pair<double,double> p)
{
	return sqrt(sqr(p.first)+sqr(p.second));
}

double dist(pair<double,double> p1,pair<double,double> p2)
{
	return sqrt(sqr(p1.first-p2.first)+sqr(p1.second-p2.second));
}

double segm(PDD p1,PDD p2)
{
	double d = dist(p1,p2);
	double alp = asin((d/2.0l)/Rin)*2.0l;
	
	double h = sqrt(sqr(Rin)-sqr(d/2.0l));
	return (((alp/(2*PI))* PI*Rin*Rin)- d*h/2.0l);
}

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int TTT;
	cin >> TTT;
	FOR(ttt, 1, TTT+1)
	{
		printf("Case #%d: ",ttt);
		double f,R,t,r,g;
		cin >> f >> R >> t >> r >> g;
		Rin = R-t-f;
		
		
		vector<PDD> aY1,aY2,aX1,aX2;


		if (f*2.0>=g) { cout << "1.000000" << endl; continue; }


		// ADD Y's
		double y1=0;
		double y2=r+f;
		double x1=Rin;
		double x2;
		if (y2>Rin)
				x2=0, y2=Rin;
			else
				x2 = sqrt(sqr(Rin)-sqr(y2));
		aY1.pb(mp(x1,y1));
		aY2.pb(mp(x2,y2));
		
		double ys = r+g;
		while (ys-f<Rin)
		{
			y1=ys-f;
			y2=ys+r+r+f;

			x1 = sqrt(sqr(Rin)-sqr(y1));
			if (y2>Rin)
				x2=0, y2=Rin;
			else
				x2 = sqrt(sqr(Rin)-sqr(y2));
			aY1.pb(mp(x1,y1));
			aY2.pb(mp(x2,y2));

			ys+=r+r+g;
		}

		// ADD X's
		x1=0;
		x2=r+f;
		y1=Rin;
		if (x2>Rin)
			y2=0, x2=Rin;
		else
			y2 = sqrt(sqr(Rin)-sqr(x2));
		aX1.pb(mp(x1,y1));
		aX2.pb(mp(x2,y2));
		
		double xs = r+g;
		while (xs-f<Rin)
		{
			x1=xs-f;
			x2=xs+r+r+f;

			y1 = sqrt(sqr(Rin)-sqr(x1));
			if (x2>Rin)
				y2=0, x2=Rin;
			else
				y2 = sqrt(sqr(Rin)-sqr(x2));
			aX1.pb(mp(x1,y1));
			aX2.pb(mp(x2,y2));

			xs+=r+r+g;
		}
		
		double SS=0.0l;
		FOR(i,0,aY1.sz)
		{
			SS+= aY2[i].first*(aY2[i].second-aY1[i].second);
			SS+= (aY1[i].first-aY2[i].first)*(aY2[i].second-aY1[i].second)/2.0l;
			SS+=segm(aY1[i],aY2[i]);
		}

		FOR(i,0,aX1.sz)
		{
			SS+= aX2[i].second*(aX2[i].first-aX1[i].first);
			SS+= (aX1[i].second-aX2[i].second)*(aX2[i].first-aX1[i].first)/2.0l;
			SS+=segm(aX1[i],aX2[i]);
		}


		int MX=sqrt(sqr(R)/2.0l);

		FOR(i,0,aX1.sz)
		{
			FOR(j,0,aY1.sz)
			{
				//if (aX1[i].first<MX)
				{
					// work on X
					
					if (aX1[i].first>=aY1[j].first)
					{
						// both beyond
						break;
					}
					else
					if (aX2[i].first<=aY2[j].first)
					{
						// both above
						SS-=(aY2[j].second-aY1[j].second)*(aX2[i].first-aX1[i].first);
					}
					else
					{
						if (aX1[i].first<aY2[j].first)
						{
							// x1 in the left
							
							if (aX2[i].first<aY1[j].first)
							{
								//x2  is between CH
								
								SS -= (aY2[j].first-aX1[i].first)*(aY2[j].second-aY1[j].second);
								SS -= (aX2[i].first-aY2[j].first)*(aX2[i].second-aY1[j].second);
								SS -= (aX2[i].first-aY2[j].first)*(aY2[j].second-aX2[i].second)/2.0l;
								SS -= segm(aY2[j],aX2[i]);
							}
							else
							{
								// x2 beyond CH
								SS -= (aY2[j].first-aX1[i].first)*(aY2[j].second-aY1[j].second);
								SS -= (aY1[j].first-aY2[j].first)*(aY2[j].second-aY1[j].second)/2.0l;
								SS -= segm(aY1[j],aY2[j]);
							}
						}
						else
						{
							// x1 between
							if (aX2[i].first<aY1[j].first)
							{
								// x2 too CH
								SS -= (aX2[i].second-aY1[j].second)*(aX2[i].first-aX1[i].first);
								SS -= (aX1[i].second-aX2[i].second)*(aX2[i].first-aX1[i].first)/2.0l;
								SS -= segm(aX1[i],aX2[i]);
							}
							else
							{
								// x2 outside CH
								SS -= (aY1[j].first-aX1[i].first)*(aX1[i].second-aY1[j].second)/2.0l;
								SS -= segm(aX1[i],aY1[j]);
							}
						}
					}
				}

				
			}
		}

		SS*=4.0;
		double SSQ = PI*(R*R);
		SS += PI*(R*R - Rin*Rin);

		
		printf("%.6f\n",(SS/SSQ));

	}
	
	
	return 0;
}