#define maxn 1100
#include <iostream>
using namespace std;
int p, n;

int m[maxn], pri[maxn/2][maxn/2], dep[maxn][maxn];
int opt[maxn][maxn][10];

void init(){
	scanf("%d", &p); n=(1<<p);
	for (int i=0; i<n; i++){
		scanf("%d", &m[i]);
		m[i] = p - m[i];
	}
	for (int i=0; i<p; i++)
		for (int j=0; j<(1<<(p-i-1)); j++) {
			scanf("%d", &pri[i][j]);
			if (i==0) dep[i][j] = max(m[j*2], m[j*2+1]);
			else dep[i][j] = max(dep[i-1][j*2], dep[i-1][j*2+1]);
		}
}

int dfs(int bas, int d, int pos){
	if (bas >= dep[d][pos]) return 0;
	if (d==0) return pri[d][pos];
	if (opt[d][pos][bas]!=0x7f7f7f7f) return opt[d][pos][bas];
	int ret1 = 0x7f7f7f7f, ret2;
	if (bas+d >= dep[d][pos])
		ret1 = dfs(bas, d-1, pos*2) + dfs(bas, d-1, pos*2+1);
	ret2 = dfs(bas+1, d-1, pos*2) + dfs(bas+1, d-1, pos*2+1) + pri[d][pos];
	opt[d][pos][bas] = min(ret1, ret2);
	return opt[d][pos][bas];
}

void solve(int cas){
	memset(opt, 0x7f, sizeof opt);
	printf("Case #%d: %d\n", cas, dfs(0, p-1, 0));
}

int main(){
	int test; scanf("%d", &test);
	for (int cas=1; cas<=test; cas++){
		init();
		solve(cas);
	}
	return 0;
}
