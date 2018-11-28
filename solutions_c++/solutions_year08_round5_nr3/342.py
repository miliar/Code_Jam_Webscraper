#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;

int opt[15][2000];
int n, m;
bool can[2000][2000];
int get1[100], get2[100], get[100];
int sum[2000];
bool v[100][100];
int totCases;
int zt;
int ans;
void Dfs(int i, int j, int sum);
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d: ", cases + 1);
		scanf("%d%d", &n, &m);
		ans = 0;
		memset(v, 0, sizeof(v));
		memset(opt, 0, sizeof(opt));
		memset(sum, 0, sizeof(sum));
		for (int i(0); i < n; ++i) {
			char ch[100];
			scanf("%s", ch);
			for (int j(0); j < m; ++j)
			    if (ch[j] == 'x') v[i][j] = 1;
			    else v[i][j] = 0;
		}
		for (int i(0); i < (1 << n); ++i)
		    for (int j(0); j < (1 << n); ++j) {
				zt = i;
				for (int k(0); k < n; ++k) {
					get1[k] = zt & 1;
					zt >>= 1;
				}
				zt = j;
				for (int k(0); k < n; ++k) {
					get2[k] = zt & 1;
					zt >>= 1;
				}
				bool chk = 1;
				for (int k(0); k < n; ++k) {
				    if (get2[k] && get1[k]) chk = 0;
				    if (k < n - 1 && get2[k] && get1[k + 1]) chk = 0;
				    if (k > 0 && get2[k] && get1[k - 1]) chk = 0;
				}
				if (chk) can[i][j] = 1;
				else can[i][j] = 0;
			}
		for (int i(0); i < (1 << n); ++i) {
			zt = i;
			for (int k(0); k < n; ++k) {
				if (zt & 1) ++sum[i];
			    zt >>= 1;
			}
			opt[0][i] = sum[i];
		}
		for (int i(0); i < m - 1; ++i) {
			for (int j(0); j < (1 << n); ++j) {
				bool chk = 1;
                zt = j;
                for (int k(0); k < n; ++k) {
					if (zt & 1)
						if (v[k][i]) chk = 0;
			    	zt >>= 1;
				}
				if (!chk) {
					opt[i][j] = 0;
					continue;
				}
			    for (int k(0); k < (1 << n); ++k)
					if (can[j][k]) opt[i + 1][k] >?= opt[i][j] + sum[k];
			}
		}
		for (int i(0); i < (1 << n); ++i) {
			bool chk = 1;
			zt = i;
			for (int k(0); k < n; ++k) {
				if (zt & 1)
					if (v[k][m - 1]) chk = 0;
			    zt >>= 1;
			}
			if (!chk) opt[m - 1][i] = 0;
			ans >?= opt[m - 1][i];
		}
		printf("%d\n", ans);
	}
}
