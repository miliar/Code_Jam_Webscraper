#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#define MAXN 1010

using namespace std;

int n;
int adj[MAXN][MAXN], nadj[MAXN];
int mark[MAXN];
int fila[MAXN];

int main() {
	int t, caso = 0;
	scanf("%d", &t);
	while(t--) {
		scanf("%d", &n);
		for(int i = 1; i <= n; ++i) {
			scanf("%d", &nadj[i]);
			for(int j = 0; j < nadj[i]; ++j)
				scanf("%d", &adj[i][j]);
		}

		bool has = false;
		for(int i = 1; i <= n && !has; ++i) {
			memset(mark, 0, sizeof(mark));
			int ini = 0, fim = 0;
			for(int j = 0; j < nadj[i]; ++j) {
				fila[fim++] = adj[i][j];
				mark[adj[i][j]] = j + 1;
			}

			while(ini < fim) {
				int x = fila[ini++];
				for(int j = 0; j < nadj[x]; ++j) {
					int u = adj[x][j];
					if(mark[u] && mark[x] != mark[u]) { has = true; break; }
					if(!mark[u]) fila[fim++] = u, mark[u] = mark[x];
				}
			}
		}

		if(has) printf("Case #%d: Yes\n", ++caso);
		else printf("Case #%d: No\n", ++caso);
		
	}
	
	return 0;
}

