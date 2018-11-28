#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
using namespace std;

char combTable['Z'-'A'+1]['Z'-'A'+1];
bool oppoTable['Z'-'A'+1]['Z'-'A'+1];
int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);
	FILE* _fopen;

	_fopen = fopen( "output2.txt", "w" );
	int TestCase = 0;
	scanf( "%d", &TestCase );

	for( int tcase=0; tcase<TestCase; ++tcase )
	{
		memset( combTable, 0, sizeof(combTable) );
		memset( oppoTable, 0, sizeof(oppoTable) );

		int C;
		cin >> C;
		for( int c=0; c<C; ++c )
		{
			char comb[4];
			scanf( "%s", comb );
			combTable[ comb[0] - 'A' ][ comb[1] - 'A' ] = comb[2];
			combTable[ comb[1] - 'A' ][ comb[0] - 'A' ] = comb[2];
		}
		
		int D;
		cin >> D;
		for( int d=0; d<D; ++d )
		{
			char oppo[3];
			scanf( "%s", oppo );
			oppoTable[ oppo[0] - 'A' ][ oppo[1] - 'A' ] = true;
			oppoTable[ oppo[1] - 'A' ][ oppo[0] - 'A' ] = true;
		}

		int N;
		cin >> N;
		char _ch;
		string Invoke;
		string Result;
		cin >> Invoke;
		
		for( int i=0; i<Invoke.size(); ++i )
		{
			Result.push_back( Invoke[i] );
			if( Result.size() < 2 )
				continue;
			
			if( (_ch = combTable[ Result[Result.size()-2] - 'A' ][ Result[Result.size()-1] - 'A' ] ) != 0 )
			{
				int size = Result.size();
				Result.erase( size-1 );
				Result.erase( size-2 );
				Result.push_back( _ch );
			}
			else
			{
				for( int j=0; j<Result.size(); ++j )
				{
					if( oppoTable[ Result[j] - 'A' ][ Result[Result.size()-1] - 'A' ] )
					{
						Result.clear();
						//Result.erase( j, Result.size() );
						break;
					}
				}
			}
		}

		if( tcase > 0 )
			fprintf( _fopen, "\n" );
		fprintf( _fopen, "Case #%d: [", tcase+1 );
		if( Result.empty() )
			fprintf( _fopen, "]" );
		else
		{
			for(int re=0; re<Result.size(); ++re )
			{
				if( re == Result.size()-1)
					fprintf( _fopen, "%c]", Result[re]);
				else 
					fprintf( _fopen, "%c, ", Result[re]);
			}
		}
	}

	fclose( _fopen );
	return 0;
}