#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

long long C[ 1005 ];

long long minv( int s, int t )
{
	if ( s == t )
		return C[ s ];
	else 
		return min( minv( s, (s+t)/2 ),minv( (s+t)/2+1, t ) ); 
}

int main()
{
	int T,N;
	fin >> T,N;
	for ( int i = 1 ; i <= T ; ++ i ) {
		fin >> N;
		long long sumv = 0;
		long long sums = 0;
		for ( int j = 0 ; j < N ; ++ j )
			fin >> C[ j ];
		for ( int j = 0 ; j < N ; ++ j ) {
			sumv ^= C[ j ];
			sums += C[ j ];
		}
		fout << "Case #" << i << ": ";
		if ( sumv ) 
			fout << "NO" << endl;
		else
			fout << sums-minv( 0, N-1 ) << endl;
	}
	return 0;
}
