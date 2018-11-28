
#include <stdio.h>
#include <string.h>

int L, D, N;
char words[30][30];
char cases[256];

int func( char * a, char * b )
{
	int i,j,f;
	for ( i = 0, j = 0; a[i]; i++ )
	{
		if ( !b[j] )
		{
			return 0;
		}
		else if ( b[j] == '(' )
		{
			j++;
			f = 0;
			while ( b[j] != ')' )
			{
				if ( a[i] == b[j] )
				{
					f = 1;
				}
				j++;
			}
			if ( !f )
			{
				return 0;
			}
			j++;
		}
		else
		{
			if ( a[i] != b[j] )
			{
				return 0;
			}
			j++;
		}
	}
	return 1;
}

int main()
{
	int i,j, ans;
	freopen("C:\\A-small-attempt0.in","r",stdin);
	freopen("C:\\A-small-attempt0.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	for ( i = 0; i < D; i++ )
	{
		scanf("%s", words[i]);
	}
	for ( i = 1; i <= N; i++ )
	{
		scanf("%s", cases);
		ans = 0;
		for ( j = 0; j < D; j++ )
		{
			ans += func( words[j], cases );
		}
		printf("Case #%d: %d\n", i, ans );
	}
}