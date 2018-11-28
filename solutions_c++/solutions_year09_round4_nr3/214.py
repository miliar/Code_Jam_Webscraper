#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)

using namespace std;

vector<int> P[110], ve[210];
int N, M, sx[110], sy[110], vis[110];

int kra(int a, int b) {
	int i;
	REP(i,M) {
		if(P[a][i]>=P[b][i])
			return 0;
	}
	return 1;
}

int dfs(int v) {
	vis[v]=1; int i, k;
	REP(i,ve[v].size()) {
		k=ve[v][i];
		if(sy[k]==-1 || (!vis[sy[k]] && dfs(sy[k]))) {
			sx[v]=k;
			sy[k]=v;
			return 1;
		}
	}
	return 0;
}

int match() {
	int res=0, ok=1, i;
	while(ok) {
		memset(vis, 0, sizeof(int)*N); ok=0;
		REP(i,N) {
			if(!vis[i] && sx[i]==-1 && dfs(i)) {
				++res;
				ok=1;
			}
		}
	}
	return res;
}
		
int main(void) {
	int t, T, n, m, i, j, k, a;
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d%d", &N, &M);
		REP(i,N) {
			P[i].clear();
			ve[i].clear();
		}
		REP(i,N) {
			REP(j,M) {
				scanf("%d", &a);
				P[i].push_back(a);
			}
		}
		REP(i,N) {
			REP(j,N) {
				if(kra(i,j))
					ve[i].push_back(j);
			}
		}
		memset(sx, -1, sizeof sx); memset(sy, -1, sizeof sy); 
		printf("Case #%d: %d\n", t+1, N-match());
	}
	return 0;
}
