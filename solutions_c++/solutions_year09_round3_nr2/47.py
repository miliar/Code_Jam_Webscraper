// Marek Rogala; Code Jam 2009
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int const MAXN=550;
int n;

double x,y,z,vx,vy,vz,t;
int nx,ny,nz,nvx,nvy,nvz;


void zrob(int testcase){
	
	scanf("%d", &n);
	x=0;y=0;z=0;vx=0;vy=0;vz=0;
	REP(i,n) {
		scanf("%d%d%d%d%d%d",&nx,&ny,&nz,&nvx,&nvy,&nvz);
		x+=nx;
		y+=ny;
		z+=nz;
		vx+=nvx;
		vy+=nvy;
		vz+=nvz;
	}
	x/=n; y/=n; z/=n;
	vx/=n; vy/=n; vz/=n;

	if((vx*vx+vy*vy+vz*vz)<=0.00000001) t = 0; else {t = -(vx*x+vy*y+vz*z)/(vx*vx+vy*vy+vz*vz);
	if(t<0) t=0;}
	
	x+=t*vx;
	y+=t*vy;
	z+=t*vz;
	double dist=sqrt(x*x+y*y+z*z);

	printf("Case #%d: %lf %lf\n",testcase,dist,t);
}

int main() {
	int T; scanf("%d", &T);
	for(int i=1;i<=T;i++) zrob(i);
	return 0;
}


