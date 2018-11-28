#include <stdio.h>
#include <string>
#include <map>

using namespace std;

char path[102];

int createpath( char path[], map<string, bool> &ep )
{
	int i;
	int cnt = 0;
	string str(path);

	if( !ep[str] )
		{
		++cnt;
		ep[str] = true;
		for( i = strlen( path ) - 1; path[i] != '/'; --i );//end for
		if( i > 0 )
			{
			path[i] = '\0';
			cnt += createpath( path, ep );
			path[i] = '/';
			}//end if
		}//end if
	return cnt;
}


int main()
{
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int t;
	int i, j;
	int m, n;
	map<string, bool> ep;
	int cnt;

	scanf( "%d", &t );

	for( i = 1; i <= t; ++i )
		{
		ep.clear();
		scanf( "%d%d", &m, &n );
		for( j = 0; j < m; ++j )
			{
			scanf( "%s", path );
			ep[string(path)] = true;
			}//end for
		cnt = 0;
		for( j = 0; j < n; ++j )
			{
			scanf( "%s", path );
			cnt += createpath( path, ep );
			}//end for
		printf( "Case #%d: %d\n", i, cnt );
		}//end for

	return 0;
}
