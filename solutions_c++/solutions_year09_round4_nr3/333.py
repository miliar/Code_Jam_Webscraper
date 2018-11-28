#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxn 210
struct Edge {
	int to;
	Edge *next;
}edges[maxn * maxn], *Gp[maxn];
int n, K;
int mat[maxn][maxn];
int nEdge;
bool used[maxn], fb[maxn];
int pos[maxn], Qu[maxn], qN;  

bool path(int x){
    Edge* p;
    int k, v;
    for (p = Gp[x]; p; p = p->next)
        if (!used[v = p->to] && !fb[v]){
            k = pos[v];
            pos[v] = x;
            Qu[qN++] = v;
			used[v] = true;
			if (k == -1 || path(k))
                return true;
            pos[v] = k;
        }
    return false;
}

int get_match(int n1, int n2){
    int i, j, ret = 0;
    memset(pos, -1, n2 * sizeof(int));
    memset(fb, false, n2);
    for (i = 0; i < n1; i++){
        memset(used, false, n2); qN = 0;
        if (path(i)){
            ret++; 
			continue;
        }
        for (j = 0; j < qN; j++)
            fb[Qu[j]] = true;
    }
    return ret;
}

void insertp(int x, int y) {
	Edge *p = &edges[nEdge++];
	p->to = y;
	p->next = Gp[x];
	Gp[x] = p;
}
void solve(){
	int i, j, k;
	for (i = 0; i < n; ++i)
		for (j = 0; j < n; ++j) {
			for (k = 0; k < K; ++k)
				if (mat[i][k] >= mat[j][k]) break;
				if (k >= K) {
					insertp(i, j);
				}
		}
	printf("%d\n", n - get_match(n, n));
}
void init() {
	int i, j;
	scanf("%d%d", &n, &K);
	for (i = 0; i < n; ++i)
		for (j = 0; j < K; ++j)
			scanf("%d", &mat[i][j]);
	
	memset(Gp, 0, sizeof(Gp));
	nEdge = 0;
}

int main() {
	freopen("Cl.in", "r", stdin);
	freopen("Cl.out", "w", stdout);
	
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		init();
		printf("Case #%d: ", ++cas);
		solve();

	}
	//while (1);
	return 0;
}
