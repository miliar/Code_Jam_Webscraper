#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))

#include <iostream>

using namespace std;

typedef long long ll;

bool g[101][101];
int n, k;
int par[201];
bool use[201];
int pr[101][30];

bool DFS(int v) {
	use[v] = 1;
	for (int i=1; i<=n; i++) if (g[v][i]) {
		if ( par[i+n] == 0 || (!use[par[i+n]] && DFS(par[i+n])) ) {
			par[v] = i+n, par[i+n] = v;
			return 1;
		}
	}
	return 0;
}

int main() {
	int t;
	scanf("%d",&t);
	for (int curTest = 1; curTest<=t; curTest++) {
		memset(g,0,sizeof(g));
		memset(par,0,sizeof(par));
		
		scanf("%d%d",&n,&k);
		for (int i=1; i<=n; i++)
			for (int j=0; j<k; j++) scanf("%d",&pr[i][j]);
		for (int i=1; i<=n; i++)
			for (int j=1; j<=n; j++) {
				bool flag = 1;
				for (int j1=0; j1<k; j1++)
					if (pr[i][j1]>=pr[j][j1]) {
						flag = 0;break;
					}
				g[i][j] = flag;
			}
		
		int match = 0;
		for (int i=1; i<=n; i++) {
			memset(use,0,sizeof(use));
			if (DFS(i)) match++;
		}

		cerr << match;
		
		printf("Case #%d: %d\n",curTest,n-match);
	}
}
