#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <math.h>
#include <map>
#include <utility>

#define mp make_pair
#define fi first
#define se second
using namespace std;

int main()
{
	int i, j, k, T, n, len, match[105], win[105];
	double owp[105], oowp[105], temp, rpi[105];
	char dummy, st[105][105];
//	freopen("1-2.in", "r", stdin);
//	freopen("1-2.out", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; ++i)
	{
		scanf("%d%c", &n, &dummy);
		for (j = 0; j < n; ++j)
		{
			gets(st[j]);
			len = strlen(st[j]);
			match[j] = 0;
			win[j] = 0;
			for (k = 0; k < len; ++k)
			{
				if (st[j][k] != '.')
				{
					++match[j];
					win[j] += st[j][k]-'0';
				}
			}
		}
		for (j = 0; j < n; ++j)
		{
			temp = 0;
			for (k = 0; k < len; ++k)
			{
				if (st[j][k] != '.')
					temp += (win[k]-(st[k][j]-'0'))/(double)(match[k]-1);
			}
			owp[j] = temp/match[j];
		}
		for (j = 0; j < n; ++j)
		{
			temp = 0;
			for (k = 0; k < len; ++k)
			{
				if (st[j][k] != '.')
					temp += owp[k];
			}
			oowp[j] = temp/match[j];
		}
		printf("Case #%d:\n", i);
		for (j = 0; j < n; ++j)
		{
			rpi[j] = (0.25*win[j]/match[j])+(0.5*owp[j])+(0.25*oowp[j]);
			printf("%lf\n", rpi[j]);
		}
	}
//	fclose(stdin); fclose(stdout);
	return 0;
}
