#define DBG
// Grzegorz Guspiel
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
using namespace std;

#ifdef DBG
#define R(x) cout<<x<<endl
#else
#define R(x)
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)
#define FOR(i,b,e) for(int (i)=(b); (i)<=(e); (i)++)

const int maxn=110;
int g[maxn][maxn];
int segs[maxn][maxn];
int s1[maxn];
int s2[maxn];
bool v1[maxn];
int n,m;

void get_data() {
	scanf("%d%d", &n, &m);
	REP(i,n) REP(j,m) scanf("%d", &segs[i][j]);
}
void gen_graph() {
	REP(i,n) REP(j,n) g[i][j]=0;
	REP(i,n) REP(j,n) if(i!=j) {
		g[i][j]=1; // i moze byc pod j
		REP(k,m) if(segs[i][k]>=segs[j][k]) g[i][j]=0; // nie moze
	}
}

bool dfs(int a) {
	v1[a]=1;
	REP(i,n) if(g[a][i]) {
		if(s2[i]==-1 || !v1[s2[i]] && dfs(s2[i])) {
			s2[i]=a;
			s1[a]=i;
			return 1;
		}
	}
	return 0;
}

bool lookup() {
	REP(i,n) v1[i]=0;
	REP(i,n) if(s1[i]==-1) if(dfs(i)) return 1;
	return 0;
}

int main() {
	int z; scanf("%d", &z);
	REP(zz,z) {
		get_data();
		gen_graph();
		REP(i,n) s1[i]=s2[i]=-1;
		int cnt=0;
		while(lookup()) cnt++;
		printf("Case #%d: %d\n", zz+1, n-cnt);
	}
}
