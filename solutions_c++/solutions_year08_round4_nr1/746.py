#include<iostream>
using namespace std;
#define N 10008
#define INF 1<<20

struct Node{
	int v, g, c;
	bool leaf;
}P[N];

int m, dp[N][2] = {0};

void DP( int pos )
{
	if( P[pos].leaf==true)
	{
		dp[pos][P[pos].v] = 0;
		dp[pos][1-P[pos].v] = INF;
		return;
	}
	DP( 2*pos );
	DP( 2*pos+1 );

	int x0, x1, y0, y1;
	x0 = dp[2*pos][0]+dp[2*pos+1][0];
	x1 = min(dp[2*pos][1]+dp[2*pos+1][0],dp[2*pos][1]+dp[2*pos+1][1]);
	x1 = min(x1, dp[2*pos][0]+dp[2*pos+1][1]);
	
	y0 = min(dp[2*pos][0]+dp[2*pos+1][0],dp[2*pos][0]+dp[2*pos+1][1]);
	y0 = min(y0, dp[2*pos][1]+dp[2*pos+1][0]);
	y1 = dp[2*pos][1]+dp[2*pos+1][1];
	if(P[pos].c==0)
	{
		if(P[pos].g==0)
		{
			dp[pos][0] = x0;
			dp[pos][1] = x1;
		}
		else{
			dp[pos][0] = y0;
			dp[pos][1] = y1;
		}
		return;
	}
	if(P[pos].g==0)
	{
		dp[pos][0] = min( x0, y0+1);
		dp[pos][1] = min( x1, y1+1);
	}
	else{
		dp[pos][0] = min( y0, x0+1);
		dp[pos][1] = min( y1, x1+1);
	}
}
			 
int main()
{
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\in.txt","r",stdin);
	freopen("C:\\Documents and Settings\\v-guozh\\Desktop\\out.txt","w",stdout);
	
	int i, j, k, r, s, t, g, c, root;
	scanf("%d",&t);
	for(i=1; i<=t; i++)
	{
		scanf("%d%d",&m,&root);
		for(j=0; j<N; j++) P[j].leaf = 0;
		for(j=1; j<=(m-1)/2; j++)
		{
			scanf("%d%d",&P[j].g,&P[j].c);
		}
		for( ; j<=m; j++)
		{
			scanf("%d",&P[j].v);
			P[j].leaf = true;
		}

		DP( 1 );
		printf("Case #%d: ",i);
		if( dp[1][root]>=INF ) printf("IMPOSSIBLE\n");
		else printf("%d\n",dp[1][root]);
	}
	return 0;
}