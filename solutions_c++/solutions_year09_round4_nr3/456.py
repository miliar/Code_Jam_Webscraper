#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cassert>

using namespace std;

#define Eo(x) { cerr << #x << " = " << (x) << endl; }

typedef long long int64;
typedef double real;

static const int inf = 0x3f3f3f3f;
static const real eps = 1e-6;

const int maxn = 16;

vector<int> a[maxn];
char g[maxn][maxn]; // purely less than

char was[maxn];
int dist[maxn];
int back[maxn];

const int maxs = (1 << 17);
int sol[maxs];

inline int bit(int k){
	return (1 << k);
}

int n;

void dfs(int v, int mask, int d){
	sol[mask] = min(sol[mask],d);
	for (int p = 0; p < n; p++) if (g[v][p] && !(bit(p) & mask)){
		int next = mask|bit(p);
		dfs(p,next,d);
	}
}

int main(){
	fill(a,a+maxn,vector<int>(maxn));
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		Eo(_);
		int k; cin >> n >> k;
		for (int i = 0; i < n; i++){
			a[i].resize(k);
			for (int j = 0; j < k; j++){
				int t; scanf("%d",&t);
				a[i][j] = t;
			}
		}
		memset(g,0,sizeof(g));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++) if (i != j){
				g[i][j] = 1;
				for (int l = 0; l < k; l++) if (a[i][l] >= a[j][l]){
					g[i][j] = 0;
					break;
				}
			}
		}
		memset(was,0,sizeof(was));
		memset(sol,0x3f,sizeof(sol));
		sol[0] = 0;
		for (int v = 0; v < bit(n); v++) if (sol[v] != 0x3f3f3f3f){
			int mask = v;
			for (int i = 0; i < n; i++) if (!(bit(i)&v)){
				dfs(i,mask|bit(i),sol[mask]+1);
			}
		}
		printf("Case #%d: %d\n",_+1,sol[bit(n)-1]);
	}
	return 0;
}
