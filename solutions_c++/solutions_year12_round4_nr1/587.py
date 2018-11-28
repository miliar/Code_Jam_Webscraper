#include<cstdio>
#include<cstring>
using namespace std;
const int maxn = 10005;
int d[maxn];
int l[maxn];
int f;
int a[maxn];
int Min( int x, int y )
{
	return x < y? x : y;
}
int main()
{
	int cas, ca = 0,n;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		scanf( "%d", &n ); 
		memset( a, -1, sizeof( a ));
		for ( int i = 0; i < n; i++ )
		{
			scanf( "%d", &d[i] );
			scanf( "%d", &l[i] );
		}
		scanf( "%d", &f );
		a[0] = d[0];
		int j = 1;
		bool u = false;
		for ( int i = 0; i < n; i++ )
		if (  a[i] != -1 )
		{	
				if ( a[i] + d[i] >= f ) 
				{
					u = true;
					break;
				}
//				printf( "%d %d\n", i, a[i] + d[i] );
			while ( j < n && a[i]+d[i] >= d[j] )
			{
				a[j] = Min( l[j], d[j] - d[i] );
				j++;
			}
		}
		else break;
		if ( u )
		{
			printf( "Case #%d: YES\n",++ca);
		}
		else
		{
			printf( "Case #%d: NO\n",++ca);
		
		}
	}
	return 0;
}