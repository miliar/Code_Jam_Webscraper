#include "stdio.h"
#include <vector>
using namespace std;

char w[5100];
int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "hayexp.out", "w", stdout );
	int l,n, m;

	scanf( "%d%d%d", &l, &n, &m );
	vector<vector<int>> vecs;

	vector<int> t( l, 0 );
	for( int i=0; i<n; ++i )
	{
		scanf( "%s", w );
		for( int i=0; i<l; ++i )
		{
			t[i] = (1<<(w[i]-'a'));
		}
		vecs.push_back( t );
	}

	for( int i=0; i<m; ++i )
	{
		vector<int>s;
		scanf( "%s", w );

		for( int k=0; w[k]; ++k )
		{
			int h = 0;
			if( w[k] == '(' )
			{
				while( w[++k] != ')' )
				{
					h |= 1<<(w[k]-'a');
				}
			}
			else
				h = 1<<(w[k]-'a');
			s.push_back( h );
		}

		int ans = n;
		for( int j=0; j<n; ++j )
		{
			for( int k=0; k<l; ++k )
			{
				if( (s[k] & vecs[j][k]) == 0 )
				{
					--ans;
					break;
				}
			}
		}
		printf( "Case #%d: %d\n", i+1, ans );
	}

	return 0;

}