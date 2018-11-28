#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>

#define SZ 105
#define INF 1e9

using namespace std;

int memo[SZ][SZ];
int rel[SZ];

int go(int a, int b)
{
	if(memo[a][b] < INF)
		return memo[a][b];
	if(b - a < 2)
	{
		return 0;
	}
	int i;
	for(i = a + 1; i < b; i++)
	{
		int x = rel[b] - rel[a] - 2 + go(a, i) + go(i, b);
		if(x < memo[a][b])
			memo[a][b] = x;
	}
	return(memo[a][b]);
}

int main()
{
//	freopen("C-small-attempt0.in", "rt", stdin);
//	freopen("C-small_1.out", "wt", stdout);
	
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int i, j, kase, inp, p, q;
	scanf("%d", &inp);

	
	for(kase = 1; kase <= inp; kase++)
	{
		for(i = 0; i < SZ; i++)
		{
			for(j = 0; j < SZ; j++)
			{
				memo[i][j] = INF;
			}
		}
		scanf("%d %d", &p, &q);
		rel[0] = 0;
		for(i = 1; i <= q; i++)
		{
			scanf("%d", &rel[i]);
		}
		rel[q + 1] = p + 1;
		int mn = go(0, q + 1);
		printf("Case #%d: %d\n", kase, mn);
	}
	return 0;
}
