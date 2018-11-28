#define DBGi
// Grzegorz Guspiel
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,bb,ee) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define ST first
#define ND second
#define PB push_back
#define PP pop_back
#define MP make_pair

struct tpos {
	int a,b,p;
	tpos() {}
	tpos(int aa, int bb, int pp):
		a(aa), b(bb), p(pp) {}
};

tpos combine(tpos x, tpos y) {
	if(x.p && y.p) return tpos(0,0,0);
	return tpos(x.a+y.a, x.b+y.b, x.p+y.p);
}

const int maxn = 110;
typedef pair<string, int> torder;
int n,l;
torder todo[maxn];
char buf[34];
vector<tpos> t[maxn][maxn][maxn];
int d[maxn][maxn][maxn];
bool v[maxn][maxn][maxn];

int main() {
	n = 100;
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		scanf("%d", &l);
		FOR(i,1,l) {
			scanf("%s%d", buf, &todo[i].ND);
			todo[i].ST = buf;
		}
		
		FOR(i,0,n+1) FOR(j,0,n+1) FOR(k,0,l+1)
			v[i][j][k] = 0;
		FOR(i,1,n) FOR(j,1,n) FOR(k,1,l) {
			
			vector<tpos> mvx, mvy;
			{
				mvx.PB(tpos(-1,0,0));
				mvx.PB(tpos(+1,0,0));
				mvx.PB(tpos( 0,0,0));
				if(todo[k].ST == "O" && todo[k].ND == i)
					mvx.PB(tpos( 0,0,1));
			}
			{
				mvy.PB(tpos(0,-1,0));
				mvy.PB(tpos(0,+1,0));
				mvy.PB(tpos(0, 0,0));
				if(todo[k].ST == "B" && todo[k].ND == j)
					mvy.PB(tpos(0, 0,1));
			}	
			REP(x,mvx.size()) REP(y,mvy.size()) if(mvx[x].p * mvy[y].p == 0) {
				tpos v = combine(mvx[x], mvy[y]);
				t[i][j][k].PB(tpos(i+v.a,j+v.b,k+v.p));
			}
		}
		
		d[1][1][1] = 0;
		v[1][1][1] = 1;
		queue<tpos> q;
		q.push(tpos(1,1,1));
		while(!q.empty()) {
			tpos act = q.front(); q.pop();
			debug("visit %d %d %d, d %d\n", act.a, act.b, act.p, d[act.a][act.b][act.p]);
			REP(i, t[act.a][act.b][act.p].size()) {
					tpos bct = t[act.a][act.b][act.p][i];
					if(!v[bct.a][bct.b][bct.p]) {
						d[bct.a][bct.b][bct.p]  = d[act.a][act.b][act.p] + 1;
						v[bct.a][bct.b][bct.p] = 1;
						q.push(bct);
					}
			}
				
		}
		
		int best = 1000000100;
		FOR(i,1,n) FOR(j,1,n) if(v[i][j][l+1])
			best = min(best, d[i][j][l+1]);
		printf("Case #%d: %d\n", zz,best);
		
		FOR(i,1,n) FOR(j,1,n) FOR(k,1,l)
			t[i][j][k].clear();
	}
	return 0;
}

