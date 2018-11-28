#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;


int tc, ntc;
int n, v;

int stat[20000];
int chang[20000];
int isleaf[20000];

int val[20000];

#define INF 1000000

int dp[20000][2];

int doit(int x, int v)
{
	if (isleaf[x])
	{
		if (val[x] != v) return INF;
		return 0;
	}
	
	int &res = dp[x][v];
	if (res != -1) return res;
	
	res = INF;
	
	// do OR
	int add;
	if (stat[x] == 0) add = 0;
	else if (chang[x]) add = 1;
	else add = INF;

	int i, j;
	for (i=0; i<2; i++) for (j=0; j<2; j++)
	{
		if ((i || j) == v)
			res <?= add + doit(x+x+1, i) + doit(x+x+2, j);
	}
		
	if (stat[x] == 1) add = 0;
	else if (chang[x]) add = 1;
	else add = INF;

	for (i=0; i<2; i++) for (j=0; j<2; j++)
	{
		if ((i && j) == v)
			res <?= add + doit(x+x+1, i) + doit(x+x+2, j);
	}
	
	return res;
}

int main()
{
	scanf("%d",&ntc);
	int i;
	int res;
	for (tc = 1; tc <= ntc; tc++)
	{
		scanf("%d %d",&n,&v);
		
		for (i=0; i<(n-1)/2; i++) 
		{
			isleaf[i] = false;
			scanf("%d %d",&stat[i],&chang[i]);
		}
		
		for (; i<n; i++)
		{
			isleaf[i] = true;
			scanf("%d",&val[i]);
		}
		
		memset(dp,-1,sizeof(dp));
		
		res = doit(0, v);
		printf("Case #%d: ",tc);
		if (res >= INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",res);
	}
}