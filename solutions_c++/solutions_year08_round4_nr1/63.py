#include<cstdlib>
#include<cstdio>
#include<iostream>
using namespace std;

int const maxM = 20000;
int const oo = 2000000000;
int gate[maxM], change[maxM], m, v;
int opt[maxM][2], totCases;
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &totCases);
	for (int cases(0); cases != totCases; ++cases) {
		printf("Case #%d: ", cases + 1);
		scanf("%d%d", &m, &v);
		for (int i(1); i <= (m - 1) / 2; ++i) scanf("%d%d", &gate[i], &change[i]);
		for (int i(1); i < maxM; ++i) opt[i][0] = opt[i][1] = oo;
		for (int i(1); i <= (m + 1) / 2; ++i) {
			int tem;
			scanf("%d", &tem);
			opt[i + (m - 1) / 2][tem] = 0;
		}
		for (int i = (m - 1) / 2; i >= 1; --i)
		    for (int j(0); j <= 1; ++j)
		        for (int k(0); k <= 1; ++k)
					if (opt[i * 2][j] != oo && opt[i * 2 + 1][k] != oo) {
						if (gate[i]) opt[i][j & k] <?= opt[i * 2][j] + opt[i * 2 + 1][k];
						else opt[i][j | k] <?= opt[i * 2][j] + opt[i * 2 + 1][k];
						if (change[i]) {
							if (gate[i]) opt[i][j | k] <?= opt[i * 2][j] + opt[i * 2 + 1][k] + 1;
							else opt[i][j & k] <?= opt[i * 2][j] + opt[i * 2 + 1][k] + 1;
						}
					}
	//	cout << opt[4][1] << endl;
		if (opt[1][v] == oo) printf("IMPOSSIBLE\n");
		else printf("%d\n", opt[1][v]);
	}
}
