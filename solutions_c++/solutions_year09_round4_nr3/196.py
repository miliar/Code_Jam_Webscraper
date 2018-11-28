#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

typedef long long int64;
typedef double real;

#define inf 0x3f3f3f3f

#define maxn (1 << 8)
#define maxk (1 << 6)

int g[maxn][maxn], par[maxn], was[maxn], n, is_par[maxn];

int pr[maxn][maxk];

bool find_par(int v) {
	if(was[v]) return false;
	was[v] = 1;
	for(int i = 0; i < n; i++) if(g[v][i])
		if(par[i] == -1 || find_par(par[i])) {
			par[i] = v;
			return true;
		}
	return false;
}

int main() {
	int t = 1, tc;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:", t);
		int k, i, j, l;
		scanf("%d%d", &n, &k);
		for(i = 0; i < n; i++)
			for(j = 0; j < k; j++)
				scanf("%d", pr[i]+j);
		memset(g, 0, sizeof(g));
		for(i = 0; i < n; i++)
			for(j = 0; j < n; j++) {
				for(l = 0; l < k; l++)
					if(pr[i][l] >= pr[j][l]) break;
				g[i][j] |= (l >= k);
			}
		//for(i = 0; i < n; i++, fprintf(stderr, "\n"))
		//	for(j = 0; j < n; j++)
		//		fprintf(stderr, "%d ", g[i][j]);

		memset(par, -1, sizeof(par));
		for(i = 0; i < n; i++) {
			memset(was, 0, sizeof(was));
			find_par(i);
		}
		memset(is_par, -1, sizeof(is_par));
		for(i = 0; i < n; i++)
			if(par[i] != -1)
				is_par[par[i]] = i;
		int ans = 0;
		for(i = 0; i < n; i++) {
			if(par[i] == -1) ans++;
			if(is_par[i] == -1) ans++;
		}
		assert(ans % 2 == 0);
		ans /= 2;
		printf(" %d\n", ans);
	}
	return 0;
}
