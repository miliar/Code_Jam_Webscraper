#include<cstdio>
#include<algorithm>
using namespace std;

const int maxn = 10005;
int app[maxn];

int q[maxn],l,r;
int main()
{
	int T=0,TT;
	int n,x,ans;
	scanf("%d",&TT);
	while( TT-- )
	{
		printf("Case #%d: ",++T);
		for( int i = 1;i<maxn;i++ ) app[i] = 0;
		scanf("%d",&n);
		if( n==0 ) ans = 0;else ans = 10000;
		while(n--)
		{
			scanf("%d",&x);
			app[x]++;
		}
		l = 1;
		r = 0;
		for( int i = 1;i<maxn;i++ )
		if( app[i] < r-l+1  )
		{
			while( app[i] < r-l+1 )
			{
				ans = min( ans,i-q[l] );
				l++;
			}
		}else
		{
			while( r-l+1 < app[i] )
				q[++r] = i;
		}

		printf("%d\n",ans);
	}
	return 0;
}
