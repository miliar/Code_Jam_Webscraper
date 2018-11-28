#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std; 
int tcnt; 
int go()
{ 
	int n, m, pn[101], sat[101][20][2], i, j, k; 
	scanf("%d%d", &n, &m); 
	for (i = 0; i < m; i++) 
	{ 
		scanf("%d", &pn[i]); 
		for (j = 0; j < pn[i]; j++) 
		{
			scanf("%d%d", &sat[i][j][0], &sat[i][j][1]); 
			sat[i][j][0]--; 
		}
	}
	int max = 1000, ans = 10000; 
	for (i = 0; i < (1 << n); i++) 
	{ 
		for (j = 0; j < m; j++) 
		{
			for (k = 0; k < pn[j]; k++) 
				if (((i >> sat[j][k][0]) & 1) == sat[j][k][1])
					break; 
			if (k >= pn[j])
				break; 
		}
		if (j >= m)
		{ 
			int cnt = 0; 
			for (j = 0; j < n; j++) 
				cnt += (i >> j) & 1; 
			if (cnt < max) 
				ans = i, max = cnt; 
		}
	}
	printf("Case #%d:", ++tcnt);
	i = ans; 
	if (i < (1 << n))
	{
		for (j = 0; j < n; j++) 
			printf(" %d", (i >> j) & 1); 
		printf("\n"); 
	}
	else
		printf(" IMPOSSIBLE\n"); 
}
int main()
{ 
	freopen("B-small-attempt2.in", "r", stdin); 
	freopen("ans.txt", "w", stdout); 
	int T; 
	tcnt = 0; 
	scanf("%d", &T); 
	while (T--) 
		go();
	return 0; 
}
