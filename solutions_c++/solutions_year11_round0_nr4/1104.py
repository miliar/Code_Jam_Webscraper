#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream fin("D-large.in");
ofstream fout("D-large.out");

int  Data[ 1005 ];
bool Used[ 1005 ];

int main()
{
	int T,N;
	fin >> T;
	for ( int t = 1 ; t <= T ; ++ t ) {
		fin >> N;
		memset( Used, false, sizeof( Used ) );
		for ( int i = 1 ; i <= N ; ++ i ) 
			fin >> Data[ i ];

		//int count = 0;
		int sum = 0;
		for ( int i = 1 ; i <= N ; ++ i )
			if ( !Used[ i ] ) {
				int count = 0;
				int node = i;
				while ( !Used[ node ] ) {
					Used[ node ] = true;
					node = Data[ node ];
					++ count;
				}
				if ( count > 1 )
					sum += count;
			}
		fout << "Case #" << t << ": " << sum << ".000000" << endl;
	}
	return 0;
}
