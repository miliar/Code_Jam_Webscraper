#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
using namespace std;
int main( void )
{
	string str;
	getline( cin, str );
	int inf = 1000000;
	int N = atoi( str.c_str() );
	for( int C = 0; C < N; C ++ ){
		getline( cin, str );
		int S = atoi( str.c_str() );
		vector<string> s;
		for( int i = 0; i < S; i ++ ){
			getline( cin, str );
			s.push_back( str );
		}

		vector<int> D(S, 0);
		vector<int> D2(S,0);
		getline( cin, str );
		int Q = atoi( str.c_str() );
		for( int i = 0; i < Q; i ++ ){
			getline( cin, str );
			int a = -1;
			int m = inf;
			for( int j = 0; j < S; j ++ ){
				if( str == s[j] )
					a = j;
				m = min( m, D[j] );
			}
			for( int j = 0; j < S; j ++ ){
				if( j == a )
					D[j] = inf;
				else
					D[j] = min( m + 1, D[j] );
			}
		}
		int ret = inf;
		for( int j = 0; j < S; j ++ ){
			ret = min( ret, D[j] );
		}
		printf( "Case #%d: %d\n", C + 1, ret );
	}
}
