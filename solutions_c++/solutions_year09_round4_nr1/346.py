#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define maxn 55
int Lmt;
char mat[maxn][maxn];
int opt[maxn];
int n;

void init(){
	int i, j;
	scanf("%d", &n);
	memset(opt, -1, sizeof(opt));
	for (i = 0; i < n; ++i) {
		scanf("%s", mat[i]);
		for (j = 0; j < n; ++j) {
			if (mat[i][j] == '1')
				opt[i] = j;
		}
	}
}
void solve(){

	int ans = 100000, cnt, j, i;
	int seq[maxn];
	for (i = 0; i < n; ++i) seq[i] = i;
	do {
		for (i = 0; i < n; ++i)
			if (opt[seq[i]] > i) break;
		if (i < n) continue;
		cnt = 0;
		for (i = 0; i < n; ++i)
			for (j = 0; j < i; ++j)
				if (seq[j] > seq[i]) ++cnt;
		if (cnt < ans) ans = cnt;
	} while (next_permutation(seq, seq + n));
	printf("%d\n", ans);
}
int main() {
	freopen("As.in", "r", stdin);
	freopen("As.out", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while (T--) {
		init();
		
		printf("Case #%d: ", ++cas);
		solve();
	}
//	while (1);
	return 0;
}
