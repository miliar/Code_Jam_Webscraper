#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

struct node
{
	char C;
	int  S;
}Move[ 105 ];

bool Used[ 105 ];
int  Q[ 105 ];
int  S[ 105 ];
int  V[ 105 ];

int main()
{
	int T,N;
	fin >> T;
	for ( int i = 1 ; i <= T ; ++ i ) {
		fin >> N;
		for ( int j = 1 ; j <= N ; ++ j )
			fin >> Move[ j ].C >> Move[ j ].S;
			
		int now_O = 0;
		int now_B = 0;

		for ( int j = 1 ; j <= N ; ++ j ) 
			if ( Move[ j ].C == 'B' ) {
				V[ j ] = abs( now_B-Move[ j ].S )+1;
				now_B = Move[ j ].S;
			}else {
				V[ j ] = abs( now_O-Move[ j ].S )+1;
				now_O = Move[ j ].S;
			}
		
		int sumB = 0;
		int sumO = 0;
		for ( int j = 1 ; j <= N ; ++ j )
			if ( Move[ j ].C == 'B' ) {
				V[ j ] += sumB;
				sumB	= V[ j ];
			}else {
				V[ j ] += sumO;
				sumO	= V[ j ];
			}
		
		for ( int j = 2 ; j <= N ; ++ j ) 
			if ( V[ j ] <= V[ j-1 ] ) {
				int Short = V[ j-1 ]+1 - V[ j ];
				for ( int k = j ; k <= N ; ++ k )
					if ( Move[ k ].C == Move[ j ].C )
						V[ k ] += Short;
			}
	
		fout << "Case #" << i << ": " << V[ N ]-1 << endl;
	}
	return 0;
}
