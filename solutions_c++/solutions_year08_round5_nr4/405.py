#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;

int const maxN = 1000;
int totCases, n, m, r;
bool v[maxN][maxN];
int opt[maxN][maxN];
void UpDate(int i, int j, int sum);
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d: ", cases + 1);
		memset(v, 0, sizeof(v));
		scanf("%d%d%d", &n, &m, &r);
		for (int i(0); i < r; ++i) {
			int a, b;
			scanf("%d%d", &a, &b);
			v[a - 1][b - 1] = 1;
		}
		memset(opt, 0, sizeof(opt));
		opt[0][0] = 1;
		for (int i(0); i < n; ++i)
		    for (int j(0); j < m; ++j)
		        if (!v[i][j]) {
					UpDate(i + 1, j + 2, opt[i][j]);
					UpDate(i + 2, j + 1, opt[i][j]);
				}
		printf("%d\n", opt[n - 1][m - 1]);

	}
}
void UpDate(int i, int j, int sum)
{
	if (i >= 0 && i < n && j >= 0 && j < m && !v[i][j])
		(opt[i][j] += sum) %= 10007;
}
