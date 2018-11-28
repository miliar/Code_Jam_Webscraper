#include <iostream>
#include <string>
#include <map>
#define  MAXN 1024
#define inf 100000000

using namespace std;

map <string,int> mp;

int num[MAXN];
int DP[MAXN][MAXN];
char str[1024];

void init ( int n, int m )
{
	int i, j, k;
	for ( i = 1 ; i <= m; i ++ )
	{
		for ( j = 0; j < n; j ++ )
		{
			if ( j != num[i] )
			{
				if ( DP[i-1][j] < DP[i][j] )
					DP[i][j] = DP[i-1][j];
			}
			else
			{
				for ( k = 0 ; k < n; k ++ )
				{
					if ( k == j ) continue;
					else {
						if ( DP[i-1][j]+1 < DP[i][k] )
							DP[i][k] = DP[i-1][j]+1;
					}
				}
			}
		}
	}
}

int main (void)
{
	int T, n, m;
	int i, j;
	freopen ("A-small-attempt1.in","r",stdin);
	freopen ("AA.out","w",stdout);
	scanf("%d",&T);
	int Case = 0;
	while ( T -- )
	{
		mp.clear();
		Case ++;
		scanf ("%d",&n);
		getchar();
		for ( i = 0 ; i < n ; i ++ )
		{
			gets (str);
			//puts (str);
			mp[str] = i;
		}
		scanf ("%d",&m);
		memset(DP,0,sizeof(DP));
		for ( i = 1 ; i <= m ; i ++ )
		{
			for ( j = 0 ; j < n; j ++ )
				DP[i][j] = inf;
		}
		getchar();
		for ( i = 0 ; i < m ; i ++ )
		{
			gets(str);
			//puts(str);
			num[i+1] = mp[str];
		}
		init (n,m);
		int ans = -1;
		for ( i = 0; i < n; i ++ )
		{
			if ( ans == -1 || DP[m][i] < ans )
				ans = DP[m][i];
		}
		printf ("Case #%d: %d\n",Case,ans);
	}
	return 0;
}