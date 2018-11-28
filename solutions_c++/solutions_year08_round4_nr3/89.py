#include <algorithm>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;


double c1[2][2][2];
double c2[2][2][2];
double cur1[2][2][2];
double cur2[2][2][2];

void relax(double x,double y,double z) {
	double mul[2]={-1,1};
	REP(i1,2)REP(i2,2)REP(i3,2) {
		double res=mul[i1]*x+mul[i2]*y+mul[i3]*z;
		cur1[i1][i2][i3]=min(cur1[i1][i2][i3],res);
		cur2[i1][i2][i3]=max(cur2[i1][i2][i3],res);
	}
}
double targ=1e-8;
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int N,test;
	struct {
		double x,y,z;
	}dirs[6]={{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};

	for(cin>>N,test=1;test<=N;++test) {
		int n;
		cin>>n;
		struct {
			double x,y,z,p;
		}ships[n];
		double minx,maxx,miny,maxy,minz,maxz;
		REP(i,n)
			cin>>ships[i].x>>ships[i].y>>ships[i].z>>ships[i].p;
		minx=maxx=ships[0].x;
		miny=maxy=ships[0].y;
		minz=maxz=ships[0].z;
		REP(i,n) {
			minx=min(minx,ships[i].x);
			maxx=max(maxx,ships[i].x);
			miny=min(miny,ships[i].y);
			maxy=max(maxy,ships[i].y);
			minz=min(minz,ships[i].z);
			maxz=max(maxz,ships[i].z);
		}
		double minr=0,maxr=(maxx-minx)+(maxy-miny)+(maxz-minz),r;
		while(maxr-minr>targ) {
			r=(minr+maxr)/2;
			REP(i1,2)REP(i2,2)REP(i3,2) {
				c1[i1][i2][i3]=-1e100;
				c2[i1][i2][i3]=+1e100;
			}
			REP(i,n) {
				REP(i1,2)REP(i2,2)REP(i3,2) {
					cur1[i1][i2][i3]=+1e100;
					cur2[i1][i2][i3]=-1e100;
				}
				REP(d,6)
					relax(ships[i].x+dirs[d].x*r*ships[i].p,
							ships[i].y+dirs[d].y*r*ships[i].p,
							ships[i].z+dirs[d].z*r*ships[i].p);
				REP(i1,2)REP(i2,2)REP(i3,2) {
					c1[i1][i2][i3]=max(c1[i1][i2][i3],cur1[i1][i2][i3]);
					c2[i1][i2][i3]=min(c2[i1][i2][i3],cur2[i1][i2][i3]);
				}
			}
			bool ok=true;
			REP(i1,2)REP(i2,2)REP(i3,2) {
				if(c1[i1][i2][i3]>c2[i1][i2][i3]-1e-9)ok=false;
			}
			if(ok)maxr=r;
			else minr=r;
		}
		printf("Case #%d: %.9lf\n",test,(minr+maxr)/2);
	}

	fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
	return 0;
}
