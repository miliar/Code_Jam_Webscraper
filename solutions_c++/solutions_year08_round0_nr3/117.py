#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define eps 1.0e-9
#define M_PI       3.14159265358979323846

#define NAME "C-large"

PDD operator + (const PDD &a, const PDD &b) { return make_pair(a.X+b.X,a.Y+b.Y); }
PDD operator - (const PDD &a, const PDD &b) { return make_pair(a.X-b.X,a.Y-b.Y); }
PDD operator * (const PDD &a, const double &b) { return make_pair(a.X*b,a.Y*b); }
double operator * (const PDD &a, const PDD &b) { return a.X*b.X+a.Y*b.Y; }
double operator ^ (const PDD &a, const PDD &b) { return a.X*b.Y-a.Y*b.X; }

bool in_circle(PDD p, double R)
{
	return p*p<=(R+eps)*(R+eps);
}

double angle_about(PDD p, PDD base)
{
	p=p-base;
	return atan2(p.Y,p.X);
}

int sign(double x)
{
	if (x<0) return -1;
	else return +1;
}

vector<PDD> intersect(PDD a, PDD b, double R)
{
	PDD base = a;
	PDD v = b-a;
	double aa = v.X*v.X + v.Y*v.Y;
	double bb = 2*(base.X*v.X + base.Y*v.Y);
	double cc = base.X*base.X + base.Y*base.Y - R*R;
	double dd = bb*bb-4*aa*cc;
	if (dd<0) return vector<PDD>();
	dd = sqrt(dd);
	double t1 = (-bb-dd)/2/aa;
	double t2 = (-bb+dd)/2/aa;
	vector<PDD> res;
	res.clear();
	if (-eps <= t1 && t1 <= 1.0+eps)
		res.push_back(base + v*t1);
	if (-eps <= t2 && t2 <= 1.0+eps)
		res.push_back(base + v*t2);
	return res;
}

double normalize_angle(double x)
{
	x = fabs(x);
	while (x >= 2*M_PI)
		x-=2*M_PI;
	if (x>=M_PI)
		x = 2*M_PI-x;
	return x;
}

double sq_inside(PDD sq[], double g, double RR)
{
	bool inside[5];
	bool allin=true,allout=true;
	PDD center = (sq[0]+sq[2])*0.5;
	REP(i,5)
	{
		inside[i]=in_circle(sq[i],RR);
		if (inside[i])
			allout=false;
		else
			allin=false;
	}
	if (allin)
		return g*g;
	if (allout)
		return 0;
	// учитываем, что квадрат не может быть в центре или на диаметре!!!
	vector< pair<double,PDD> > pnts;
	pnts.clear();
	REP(i,4)
		if (inside[i])
			pnts.push_back(make_pair(angle_about(sq[i],center), sq[i]));
	REP(i,4)
	{
		vector<PDD> inters = intersect(sq[i],sq[i+1],RR);
		REP(j,SZ(inters))
			pnts.push_back(make_pair(angle_about(inters[j],center), inters[j]));
	}
	SORT(pnts);
	pnts.push_back(pnts.front());
	double res=0;
	REP(i,SZ(pnts)-1)
	{
		PDD a = pnts[i].second;
		PDD b = pnts[i+1].second;
		double vct = (a^b) / 2.0;
		if (fabs(a.X-b.X) < eps || fabs(a.Y-b.Y) < eps)
			res+=vct;
		else
		{
			double qq = RR*RR/2.0*normalize_angle(angle_about(a,PDD(0,0))-angle_about(b,PDD(0,0)));
			res+=qq*sign(vct);
		}
	}
	return fabs(res);
}

double solve(double f, double R, double t, double r, double g)
{
	t+=f;
	g-=2*f;
	r+=f;
	double d=2*r;
	double RR = R-t;
	if (RR<=0) return 1.0;
	if (g<=0) return 1.0;
	if (d>=2*RR) return 1.0;
	double res=0;
	int cnt = (int)(RR/(g+d)+2);
	for (int ix = -cnt; ix<=cnt; ix++)
		for (int iy = -cnt; iy<=cnt; iy++)
		{
			PDD sq[5];
			const int ddx[5]={0,0,1,1,0};
			const int ddy[5]={0,1,1,0,0};
			REP(i,5)
			{
				sq[i]=make_pair(d/2 + ix*(g+d) + ddx[i]*g, d/2 + iy*(g+d) + ddy[i]*g);
			}
			res += sq_inside(sq,g,RR);
		}
	res = 1.0-(res/(M_PI*R*R));
	return res;
}

double monte_carlo(double f, double R, double t, double r, double g)
{

	return 0;
}

int main()
{
	/*PDD sq[5] = {PDD(1,1), PDD(1,2), PDD(2,2), PDD(2,1), PDD(1,1)};
	printf("%.9lf\n",sq_inside(sq,1,2.8));
	return 0;*/

	freopen(NAME ".in","r",stdin);
	freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d",&tests);
	REP(tst,tests)
	{
		double f,R,t,r,g;
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);

		printf("Case #%d: %.9lf\n",tst+1,solve(f,R,t,r,g),monte_carlo(f,R,t,r,g));
		//fprintf(stderr,"*");
	}
	return 0;
}
