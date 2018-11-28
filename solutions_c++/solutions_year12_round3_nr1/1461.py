#include <iostream>
#include <string.h>
#include <fstream>

using namespace std;

bool mat[110][110];
bool mark[110];
bool possible;
int n;

void DFS( int x )
{
	if( !mark[x] )
		possible = true;
	mark[x] = false;
	for( int i = 1 ; i <= n ; i ++ )
		if( mat[x][i] )
			DFS( i );
}

//#define cout fout

int main()
{
	freopen( "in.txt" , "r" , stdin );
	freopen( "out.txt" , "w" , stdout );
	int t;
	cin >> t;
	for( int tc = 1 ; tc <=  t ; tc++ )
	{
		memset( mat , false , sizeof mat );
		cin >> n;
		for( int k = 1 ; k <= n ; k ++ )
		{
			int l, s;
			cin >> l;
			while( l -- )
			{
				cin >> s;
				mat[k][s] = true;
			}
		}
		possible = false;
		for( int i = 1 ; i <= n ; i ++ )
		{
			memset( mark , true , sizeof mark );
			DFS( i );
		}
		if( possible )
			cout << "Case #" << tc << ": Yes" << endl;
		else
			cout << "Case #" << tc << ": No" << endl;
	}
	return 0;
}
