#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define REP(AA,BB) for(int AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(int AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(__typeof((AA).begin()) BB=(AA).begin(); BB!=(AA).end(); ++BB)
#define SZ(AA) ((int)((AA).size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP make_pair

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;

int n, m; VI ve[20010];
char c[210][210]; int p[210][210];

int get(int x, int y, int dx, int dy) {
	x=(x+dx+n)%n; y=(y+dy+m)%m;
	return p[x][y];
}

int vis[20010]; int cnt, E;

void dfs(int v) {
	vis[v]=1; ++cnt;
	REP(i,SZ(ve[v])) {
		int k=ve[v][i]; ++E;
		if(!vis[k])
			dfs(k);
	}
}

int main(void) {
	int T; scanf("%d", &T);
	FOR(t,1,T+1) {
		int N=0; scanf("%d%d", &n, &m);
		REP(i,n) {
			scanf("%s", c[i]);
			REP(j,m)
				p[i][j]=N++;
		}
		REP(i,N)
			ve[i].clear();
		REP(i,n) {
			REP(j,m) {
				int a=-1, b=-1;
				if(c[i][j]=='|') {
					a=get(i,j,-1,0);
					b=get(i,j,1,0);
				}
				else if(c[i][j]=='-') {
					a=get(i,j,0,-1);
					b=get(i,j,0,1);
				}
				else if(c[i][j]=='/') {
					a=get(i,j,-1,1);
					b=get(i,j,1,-1);
				}
				else if(c[i][j]=='\\') {
					a=get(i,j,-1,-1);
					b=get(i,j,1,1);
				}
				ve[a].PB(b);
				ve[b].PB(a);
			}
		}
		memset(vis, 0, sizeof vis);
		LL res=1, MOD=1000003;
		REP(i,N) {
			if(!vis[i]) {
				cnt=0; E=0;
				dfs(i); E/=2;
				if(E==cnt-1)
					res=(res*cnt)%MOD;
				else if(E==cnt)
					res=(res*2LL)%MOD;
				else
					res=0;
			}
		}
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}
