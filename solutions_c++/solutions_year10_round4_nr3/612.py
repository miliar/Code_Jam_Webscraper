#include <iostream>
using namespace std;
int i,j,n,m,curcase = 1 ,testcase,x,xx,y,yy,k,ans,pan;
int G[200][200];
int main()
{
	freopen("in.in","r",stdin);
	freopen("C.out","w",stdout);
	for ( scanf("%d\n",&testcase) ; curcase <= testcase ; curcase++ )
	{
		scanf("%d\n",&n);
		memset(G,0,sizeof(G));
		for ( i = 0 ; i < n ; i++ )
		{
			scanf("%d%d%d%d",&x,&y,&xx,&yy);
			for ( j = x ; j <= xx ; j++ )
				for ( k = y ; k <= yy ; k++ )
					G[j][k] = 1;
		}
		ans = 0;
		pan = 1;
		while (pan)
		{
			pan = 0;
			for ( i = 100 ; i ; i-- )
				for ( j = 100 ; j ; j-- )
				{
					if (G[i-1][j]&G[i][j-1]) G[i][j] = 1;
					if ((G[i-1][j]==0)&&(G[i][j-1]==0)) G[i][j] = 0;
					if (G[i][j]) pan = 1;
				}
			ans++;
		}
		printf("Case #%d: %d\n",curcase,ans);
	}
}
