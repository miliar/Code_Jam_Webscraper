#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CONTAIN(container, it) (container.find(it)!=container.end())
#define CLR(c,n) memset(c,n,sizeof(c))
typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
const int INF=1000000000;
const double EPS=1e-10;
const double PI=acos(-1);
int n, x[40], y[40], r[40];
LL all;
double minr[40][40], dis[40][40], ang[40][40];
bool check(double r0) {
	vector<LL> masks;
	REP(i,n) REP(j,n) if (i!=j&&minr[i][j]<r0) {
		double ri=r0-r[i], rj=r0-r[j], rij=dis[i][j];
		double angi=ang[i][j]-acos((ri*ri+rij*rij-rj*rj)/2/ri/rij);
		double x0=x[i]+ri*cos(angi), y0=y[i]+ri*sin(angi);
		LL mask=(1LL<<i)|(1LL<<j);
		REP(k,n) if (hypot(x[k]-x0,y[k]-y0)+r[k]<r0) mask|=(1LL<<k);
		masks.push_back(mask);
	}
	REP(i,n) if (r[i]<r0) masks.push_back(1LL<<i);
	REP(i,SZ(masks)) FOR(j,0,i) if ((masks[i]|masks[j])==all) return true;
	return false;
}
int main()
{
	//freopen("D.in","r",stdin);
	//freopen("D-small-attempt0.in", "r", stdin); freopen("D-small-attempt0.out", "w", stdout);
	//freopen("D-small-attempt1.in", "r", stdin); freopen("D-small-attempt1.out", "w", stdout);
	freopen("D-large.in", "r", stdin); freopen("D-large.out", "w", stdout);
	//freopen("D-small-practice.in", "r", stdin); freopen("practice.out","w",stdout);
	int testCase; scanf("%d", &testCase);
	for (int caseID=1; caseID<=testCase; ++caseID) {
		cerr << caseID << " of " << testCase << endl;
		scanf("%d", &n); REP(i,n) scanf("%d%d%d", x+i, y+i, r+i);
		REP(i,n) REP(j,n) dis[i][j]=hypot(x[i]-x[j],y[i]-y[j]);
		REP(i,n) REP(j,n) minr[i][j]=(dis[i][j]+r[i]+r[j])/2;
		REP(i,n) REP(j,n) ang[i][j]=atan2(y[j]-y[i],x[j]-x[i]);
		double l=0, u=2000; all=(1LL<<n)-1;
		while (u-l>1e-6) {
			double m=(l+u)/2;
			if (check(m)) u=m;
			else l=m;
		}
		printf("Case #%d: %.6lf\n", caseID, (u+l)/2);
	}
}
