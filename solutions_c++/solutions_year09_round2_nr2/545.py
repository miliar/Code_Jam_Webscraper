#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

char s1[100], s2[100];

int main( void )
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int nt, t, i, l;
	scanf( "%d", &nt );
	for ( t = 1; t <= nt; t++ )
	{
		scanf( "%s", s1 );		
		strcpy( s2, s1 );
		l = strlen(s1);
		if (next_permutation( s1, s1 + l ) )
		{
			printf( "Case #%d: %s\n", t, s1 );									
		}
		else
		{			
			for ( i = 0; s2[i] && s2[i] != '0'; i++ );
			sort( s2, s2 + l );
			for ( i = 0; s2[i] == '0'; i++ );
			if ( i != 0 )
			{
				s2[0] ^= s2[i];
				s2[i] ^= s2[0];
				s2[0] ^= s2[i];				
			}
			printf( "Case #%d: %c0%s\n", t, s2[0], s2 + 1 );						
		}
		
	}	
	return 0;
}