#include <cstdio>
#include <algorithm>
using namespace std;

#define MAXN 11000
int d[MAXN];
int l[MAXN];
int memo[MAXN];

int main ()
{
	int T; int N; int D;
	int i, j, k;
	scanf("%d",&T);
	
	for ( int cnt = 1; cnt <= T; cnt++ )
	{
		scanf("%d",&N);
		
		for ( i = 0; i < N; i++ )
		{
			scanf("%d %d",&d[i],&l[i]);
			memo[i] = -1;
		}
		
		scanf("%d",&D);
			
		for ( i = N-1; i >= 0; i-- )
		{
			for ( j = i+1; j < N; j++ )
			{
				if ( d[j] - d[i] > l[i] ) break;
				if ( memo[j] == -1 ) continue;
				
				if ( memo[j] <= min(d[j]-d[i],l[j]) )
				{
					memo[i] = d[j]-d[i];
					break;
				}
			}	
			
			if ( (memo[i] == -1) && (D - d[i] <= l[i]) ) memo[i] = D - d[i];
		}
		
		if ( memo[0] != -1 && memo[0] <= d[0] ) printf("Case #%d: YES\n",cnt);
		else printf("Case #%d: NO\n",cnt);
	}
}