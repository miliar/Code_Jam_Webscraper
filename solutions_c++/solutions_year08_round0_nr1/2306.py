#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

#define MAXN 1000
#define MAXM 1000
#define MAXLEN 1000

int n, m;
char eng[MAXN+1][MAXLEN+1];
char str[MAXM+1][MAXLEN+1];

map<string, int> gid;

int occ_n[MAXM+1];
int occ[MAXM+1];

void Solve()
{
	int i, j;
	if (m == 0)
	{
		printf("0\n");
		return;
	}
	for (i = 1; i <= m; i ++)
	{
		occ_n[i] = occ[i] = 0;
	}
	j = 1;
	for (i = 1; i <= m; i ++)
	{
		int k = gid[str[i]];
		if (occ[k] < j)
		{
			if (occ_n[j] == n - 1)
			{
				j ++;
				occ[k] = j;
				occ_n[j] = 1;
			}
			else
			{
				occ[k] = j;
				occ_n[j] ++;
			}
		}
	}
	if (occ_n[j] == 0) j --;
	printf("%d\n", j - 1);
}

int main()
{
	int i;
	int ca, cc = 0;
	scanf("%d", &ca);
	while (ca-- > 0)
	{
		scanf("%d", &n);
		for (i = 1; i <= n; i ++)
		{
			scanf("\n");
			fgets(eng[i], MAXLEN, stdin);
			gid[eng[i]] = i;
		}
		scanf("%d", &m);
		for (i = 1; i <= m; i ++)
		{
			scanf("\n");
			fgets(str[i], MAXLEN, stdin);
		}
		printf("Case #%d: ", ++cc);
		Solve();
	}
	return 0;
}
