#include <cstdio>
#include <algorithm>

using namespace std;

int n,nspl,pt;
int tr[111][3];

int solve()
{
	int c = 0;
	for( int i=0; i<n; i++ )
	{
		if( tr[i][0]>=pt )
		{
			c++;
			continue;
		}
		if( !nspl ) continue;
		nspl--;
		if( tr[i][2] && tr[i][0]==tr[i][0] )
		{
			tr[i][0]++;
			tr[i][2]--;
		}
		else if( tr[i][1] && tr[i][0]==tr[i][1] )
		{
			tr[i][0]++;
			tr[i][1]--;
		}
		if( tr[i][0]>=pt ) c++;
	}
	return c;
}

int main()
{
	int t;
	//freopen("ip.txt","r",stdin);
	scanf("%d",&t);
	for( int j=1; j<=t; j++ )
	{
		scanf("%d%d%d",&n,&nspl,&pt);
		int tmp[111];
		for( int i=0; i<n; i++ ) 
		{
			scanf("%d",&tmp[i]);
		}
		sort(tmp,tmp+n);
		reverse(tmp,tmp+n);
		for( int i=0; i<n; i++ ) 
		{
			tr[i][0] = tr[i][1] = tr[i][2] = tmp[i]/3;
			tmp[i] %= 3;
			for( int k=0; k<tmp[i]; k++ ) tr[i][k]++;
		}
		printf("Case #%d: %d\n",j,solve());
	}
	return 0;
}

