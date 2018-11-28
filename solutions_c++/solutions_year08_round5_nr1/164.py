#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define MAX_N 105
#define M (4*MAX_N+4)

int t, ile, tab[4*MAX_N+4][4*MAX_N+4];
bool g[4*MAX_N+4][4*MAX_N+4];
bool d[4*MAX_N+4][4*MAX_N+4];
bool l[4*MAX_N+4][4*MAX_N+4];
bool p[4*MAX_N+4][4*MAX_N+4];
int x, y, dir;
int dx[4]={0,1,0,-1};
int dy[4]={1,0,-1,0};

void fill(int px, int py, int val) {
	tab[px][py]=val;
	REP(i,4) {
		int nx=px+dx[i], ny=py+dy[i];
		if (nx>=0&&nx<M&&ny>=0&&ny<M&&tab[nx][ny]==0)
			fill(nx,ny,val);
	}
}

int main()
{
	scanf("%d", &t);
	FOR(tCase,1,t) {
		scanf("%d", &ile);
		string droga;
		REP(i,ile) {
			string s; int t;
			cin >> s >> t;
			while (t--) droga+=s;
		}
		CLR(tab,0);
		x=0, y=0, dir=0; int lx=0, ly=0;
		REP(i,droga.size()) {
			tab[2*(x+MAX_N)][2*(y+MAX_N)]=2;
			if (droga[i]=='F') {
				tab[lx+x+2*MAX_N][ly+y+2*MAX_N]=2;
				lx=x, ly=y;
				x+=dx[dir], y+=dy[dir];
			}
			else if (droga[i]=='L') dir=(dir-1+4)%4;
			else if (droga[i]=='R') dir=(dir+1)%4;
		}
		tab[lx+x+2*MAX_N][ly+y+2*MAX_N]=2;
		fill(0,0,1);
		//FOR(i,200,230) { FOR(j,200,230) printf("%d", tab[i][j]); printf("\n"); }

		CLR(g,0); CLR(d,0); CLR(l,0); CLR(p,0);
		REP(i,M) { bool ok=false; REP(j,M) { if (tab[i][j]==2) ok=true; l[i][j]=ok; } }
		REP(i,M) { bool ok=false; FORD(j,M-1,0) { if (tab[i][j]==2) ok=true; p[i][j]=ok; } }
		REP(i,M) { bool ok=false; REP(j,M) { if (tab[j][i]==2) ok=true; g[j][i]=ok; } }
		REP(i,M) { bool ok=false; FORD(j,M-1,0) { if (tab[j][i]==2) ok=true; d[j][i]=ok; } }

		//FOR(i,200,230) { FOR(j,200,230) printf("%d", p[i][j]); printf("\n"); }

		int res=0;
		FOR(i,0,M-1) FOR(j,0,M-1) if (tab[i][j]==1 && i%2==1&&j%2==1) {
			if ((g[i][j]&&d[i][j]) || (l[i][j]&&p[i][j])) res++;
		}
		printf("Case #%d: %d\n", tCase, res);
	}
	return 0;
}
