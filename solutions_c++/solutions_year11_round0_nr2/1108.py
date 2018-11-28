#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

struct clist
{
	char A,B,C;
}Clist[ 40 ];

struct olist
{
	char A,B;
}Olist[ 30 ];

char Data[ 105 ];
char Answer[ 105 ];

int main()
{
	int T,C,D,N;
	fin >> T;
	for ( int t = 1 ; t <= T ; ++ t ) {
		fin >> C;
		for ( int i = 0 ; i < C ; ++ i )
			fin >> Clist[ i ].A >> Clist[ i ].B >> Clist[ i ].C;
		fin >> D;
		for ( int i = 0 ; i < D ; ++ i )
			fin >> Olist[ i ].A >> Olist[ i ].B;
		fin >> N >> Data;
		
		for ( int i = 1 ; i < N ; ++ i ) {
			for ( int c = 0 ; c < C ; ++ c ) {
				if ( Clist[ c ].A == Data[ i ] && Clist[ c ].B == Data[ i-1 ] ) {
					Data[  i  ] = Clist[ c ].C;
					Data[ i-1 ] = '#'; 
					break;
				}
				if ( Clist[ c ].B == Data[ i ] && Clist[ c ].A == Data[ i-1 ] ) {
					Data[  i  ] = Clist[ c ].C;
					Data[ i-1 ] = '#'; 
					break;
				}
			}
			for ( int d = 0 ; d < D ; ++ d ) {
				if ( Olist[ d ].A == Data[ i ] ) {
					for ( int j = 0 ; j < i ; ++ j )
						if ( Data[ j ] == Olist[ d ].B ) {
							for ( int k = 0 ; k <= i ; ++ k )
								Data[ k ] = '#';
							break;
						}
				}
				if ( Olist[ d ].B == Data[ i ] ) {
					for ( int j = 0 ; j < i ; ++ j )
						if ( Data[ j ] == Olist[ d ].A ) {
							for ( int k = 0 ; k <= i ; ++ k )
								Data[ k ] = '#';
							break;
						}
				}
			}
		}
		
		int number = 0;
		for ( int i = 0 ; i < N ; ++ i )
			if ( Data[ i ] != '#' ) 
				Answer[ number ++ ] = Data[ i ];
		fout << "Case #" << t << ": [";
		for ( int i = 0 ; i < number-1 ; ++ i )
			fout << Answer[ i ] << ", ";
		if ( number > 0 )
			fout << Answer[ number-1 ];
		fout << "]" << endl;
	}
	return 0;
}
