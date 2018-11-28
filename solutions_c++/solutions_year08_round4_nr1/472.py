//////////
//
//	Auther: hazy
//	Pro ID:	
//	Pro Profile:  
//	Attention!!: 	
//	Created @ 2008_8
//
//////////
#include <stdio.h>
#include <string.h>

#include <vector>

#include <iostream>
#include <utility>
#include <algorithm>

typedef 	long long 	i64;
using namespace std;
const int MAXN = 10100;

int 	cas, T = 0;

int 	n, m, V;
int 	g[MAXN], c[MAXN];
int 	val[MAXN];

int 	dp[MAXN][2];
int 	icnt;


void 	AND(int pos, int add)
{
	int		lef = pos*2 - 1;
	int 	rig = pos*2;

	int 	a0, b0, a1, b1;
	
	a0 = dp[lef][0];
	a1 = dp[lef][1];
	b0 = dp[rig][0];
	b1 = dp[rig][1];
	
	dp[pos-1][1] <?= (a1 + b1 + add);
	
	dp[pos-1][0] <?= (a0 + b0 + add);
	dp[pos-1][0] <?= (a0 + b1 + add);
	dp[pos-1][0] <?= (a1 + b0 + add);
}

void 	OR(int pos, int add)
{
	int		lef = pos*2 - 1;
	int 	rig = pos*2;

	int 	a0, b0, a1, b1;
	
	a0 = dp[lef][0];
	a1 = dp[lef][1];
	b0 = dp[rig][0];
	b1 = dp[rig][1];
	
	dp[pos-1][1] <?= (a1 + b1 + add);
	dp[pos-1][1] <?= (a0 + b1 + add);
	dp[pos-1][1] <?= (a1 + b0 + add);
		
	dp[pos-1][0] <?= (a0 + b0 + add);
}

void	DFS(int 	pos)
{
	if (pos * 2 > m)	//	leaf
	{
		dp[pos-1][ val[pos - 1] ] = 0;
	}
	else
	{
		DFS(pos*2);
		DFS(pos*2 + 1);
		
		if (g[pos-1] == 0)
			OR(pos, 0);
		else
			AND(pos, 0);
		
		if (c[pos-1] == 1)
		{
			g[pos - 1] ^= 1;
			if (g[pos-1] == 0)
				OR(pos, 1);
			else
				AND(pos, 1);
		}
	}
}



int main()
{
	int 	i, j,k;
	
	freopen("A-large.in", "r", stdin);
	freopen("a_lagrelagre.out", "w", stdout);
	
	
	
//	printf("%d %d\n", dp[0][0], dp[0][0]*2);
	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d %d", &m, &V);
		
		icnt = (m-1)/2;
		for (i=0; i<(m-1)/2; i++)
			scanf("%d %d", &g[i], &c[i]);
		for (i=0; i<(m+1)/2; i++)
			scanf("%d", &val[icnt + i]);
		
		memset(dp, 0xf, sizeof(dp));
		
		DFS(1);
		
		int 	temp = dp[0][V];
		
		printf("Case #%d: ", ++T);
		
		if (temp > m)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", temp);
	}
	return 0;
}
