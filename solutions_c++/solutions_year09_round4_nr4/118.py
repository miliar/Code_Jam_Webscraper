#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define UN(v) sort(all(v)),(v).erase(unique((v).begin(),(v).end()),(v).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,int> pdi;

double sqr(double x) { return x*x; }
double mod(double x, double y) { return sqrt(x*x+y*y); }

const int h=50;
const double eps=1e-9, pi=2*acos(0.0);
int t, n, x[h],y[h],r[h];
double R, d[h][h];

double ang (double a, double b, double c)
{	return acos((a*a+b*b-c*c)/2/a/b); }

double norm (double a)
{	if(a<0) a+=2*pi;
	if(a>2*pi) a-=2*pi;
	return a;
}

bool can (const vi &p, int k)
{
//	printf("%d:\n", k);	REP(i, sz(p)) printf("%d ", p[i]); printf("\n");
	int n=sz(p);
	REP(i, n) if(r[p[i]]>R) return false;
	vector<pdi> e;
	vi l;
	bool u[h];
	REP(i, n)
	{
		e.clear();
		REP(j, n) if(i!=j) if(r[p[i]]+d[p[i]][p[j]]+r[p[j]]<=2*R)
		{
			double a=atan2(double(y[p[j]]-y[p[i]]), double(x[p[j]]-x[p[i]]));
			double t=ang(d[p[i]][p[j]], R-r[p[i]], R-r[p[j]]);
			e.pb(pdi(norm(a-t), p[j]));
			e.pb(pdi(norm(a+t), -p[j]-1));
		}
		sort(all(e));
		CL(u, 0);
		REP(j, n) if(mod(x[p[i]]+R-r[p[i]] - x[p[j]], y[p[i]]-y[p[j]])<=R-r[p[j]])
			u[p[j]]=1;
		l.clear();
		REP(s, n) if(!u[p[s]]) l.pb(p[s]);
		if(l.empty()) return true;
		if(k==2 && can(l, 1)) return true;
/*		printf("%d %d\n", k, i);
		REP(j, sz(e)) printf("%lf %d\n", e[j].X, e[j].Y);
		REP(j, n) printf("%d", u[p[j]]); printf("\n");*/
		REP(j, sz(e))
		{
			if(e[j].Y < 0) u[-e[j].Y-1]=0;
			else u[e[j].Y]=1;
			l.clear();
			REP(s, n) if(!u[p[s]]) l.pb(p[s]);
			if(l.empty()) return true;
			if(k==2 && can(l, 1)) return true;
		}
	}
	return false;
}

int main()
{
freopen("d-small-attempt0.in", "r", stdin);
freopen("d-small.out", "w", stdout);
	scanf("%d", &t);
REP(it, t)
{
	scanf("%d", &n);
	REP(i, n) scanf("%d%d%d", &x[i], &y[i], &r[i]);
	REP(i, n) REP(j, n) d[i][j]=mod(x[i]-x[j], y[i]-y[j]);
	double a=0,b=100000;
	vi p;
	REP(i, n) p.pb(i);
	while(a+1e-6<b)
	{
		R=(a+b)/2;
//		printf("! %lf\n", R);
		if(can(p, 2)) b=R;
		else a=R;
	}
	printf("Case #%d: %.6lf\n", it+1, (a+b)/2);
}	
	return 0;
}
