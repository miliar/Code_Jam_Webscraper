#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
typedef long long LL;
char s[10000006];
int d[10000006];
int k;
void work()
{
	memset( d, 0, sizeof( d ));
	int l = strlen( s );
	d[0] = 1;
	d[1] = -1;
	for ( int i = 0; i < l; i++ )
	{
		if ( s[i] == '1' ) 
		{
			d[++d[0]] = i;
		}
	}
	d[++d[0]] = l;

	LL ans = 0;
	int i = 1;
	int st = 0;
	if ( k == 0 )
	{
		for ( int i = 2; i <= d[0]; i++ )
		{
			LL j;
			j = d[i] - d[i-1] - 1;
			ans = ans + (j+1)*j/2;
		}
	}
	else
	{
		i = 2;
		while ( i + k - 1 < d[0] )
		{
			LL j,jj;
			j = d[i] - d[i-1] - 1;
			jj = d[i + k - 1+1] - d[i + k - 1] - 1;

			ans = ans + ( j + 1 ) * ( jj + 1 );
			i++;
		}
	}
	printf( "%I64d\n", ans );
}
void init()
{
	scanf( "%d", &k );
	scanf( "%s", s );
}
int main()
{
	init();
	work();
	return 0;
}