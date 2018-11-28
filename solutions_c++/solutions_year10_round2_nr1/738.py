#include <iostream>
using namespace std;

struct NODE
{
	int next[ 36 ];
	bool isDir;
};

NODE trie[ 1000010 ];
int top, n, m;
char path[ 1000 ];
int origin, add, now;


int change( char x )
{
	if ( x >= 'a' && x <= 'z' )
		return x - 'a';
	else
		return x - '0' + 26;
}

int main()
{
	int i, j, t, len, temp, test = 0;
	
	freopen( "A-small-attempt0.in", "r", stdin );
	freopen( "A-out.txt", "w", stdout );
	
	scanf( "%d", &t );
	
	
	while ( t-- )
	{
		
		scanf( "%d %d", &n, &m );
		
		top = 0;
		memset( trie, 0, sizeof( trie ) );
		origin = 0;
		
		for ( i = 0; i < n; ++i )
		{
			scanf( " %s", path );
			len = strlen( path );
			
			now = 0;
			
			for ( j = 1; j < len; ++j )
			{
				
				if ( path[ j ] == '/' )
				{
					if ( !trie[ now ].isDir )
					{
						trie[ now ].isDir = 1;
						++origin;
					}
					continue;
				}
				
				temp = change( path[ j ] );
				
				if ( !trie[ now ].next[ temp ] )
					trie[ now ].next[ temp ] = ++top;
				
				now = trie[ now ].next[ temp ];
			}
			
			
			if ( !trie[ now ].isDir )
			{
				trie[ now ].isDir = 1;
				++origin;
			}
		}
		
		add = 0;
		
		for ( i = 0; i < m; ++i )
		{
			scanf( " %s", path );
			len = strlen( path );
			
			now = 0;
			
			for ( j = 1; j < len; ++j )
			{
				
				if ( path[ j ] == '/' )
				{
					if ( !trie[ now ].isDir )
					{
						trie[ now ].isDir = 1;
						++add;
					}
					continue;
				}
				
				temp = change( path[ j ] );
				
				if ( !trie[ now ].next[ temp ] )
					trie[ now ].next[ temp ] = ++top;
				
				now = trie[ now ].next[ temp ];
			}
			
			
			if ( !trie[ now ].isDir )
			{
				trie[ now ].isDir = 1;
				++add;
			}
		}
		
		printf( "Case #%d: %d\n", ++test, add );
	}
	return 0;
}
			
	
