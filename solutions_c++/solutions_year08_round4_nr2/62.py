#include<cstdlib>
#include<cstdio>

using namespace std;


int totCases, n, m, a;
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d:", cases + 1);
		scanf("%d%d%d", &n, &m, &a);
		bool chk = 0;
		for (int i(0); i <= n; ++i)
		    for (int j(0); j <= m; ++j)
		        for (int ii(0); ii <= n; ++ii)
		            for (int jj(0); jj <= m; ++jj)
		                if (abs(i * jj - j * ii) == a && !chk) {
							printf(" 0 0 %d %d %d %d\n", i, j, ii, jj);
							chk = 1;
						}
		if (!chk) printf(" IMPOSSIBLE\n");
	}
}
