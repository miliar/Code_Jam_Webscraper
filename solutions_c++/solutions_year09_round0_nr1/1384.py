#include <cstdio>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

const int MXD = 5000;//za mali 25, broj rijeci u rjecniku
const int MXL = 15;//za mali 10, duljina rijeci
const int MXN = 500;//za mali 10, N pattern-a

int L, D, N;
char sve[MXD+2][MXL+2];

char rijec[1000];
vector <int> polje;

void obradi( void ){
	int K = strlen( rijec );
	polje.clear();

	for( int i = 0; i < K; i++ ){
		int dodaj = 0;
		if( rijec[i] == '(' ){
			for( i++; rijec[i] != ')'; i++ )
				dodaj |= (1<<(rijec[i]-'a'));
			polje.push_back( dodaj );
		} else{
			dodaj |= (1<<(rijec[i]-'a'));
			polje.push_back( dodaj );
//			if( !i ) printf( "%d %c\n", dodaj, rijec[i] );
		}
	}
	int sol = 0;
	for( int i = 0; i < D; i++ ){
		bool valja = 1;
		for( int j = 0; j < L; j++ ){
			if(!( (1<<(sve[i][j]-'a'))&polje[j] )){
//				printf( "%d %c (%d)", j, sve[i][j], polje[j] );
				valja = 0;
				break;
			}
		}
		if( valja ) sol++;
//		break;
	}

	printf( "%d\n", sol );

}

int main( void ){

	scanf( "%d %d %d\n", &L, &D, &N );
	for( int i = 0; i < D; i++ )
		scanf( "%s\n", sve[i] );


	for( int i = 0; i < N; i++ ){
		scanf( "%s\n", rijec );
//		printf( "%s\n", rijec );
		printf( "Case #%d: ", i+1 );
		obradi();

//		break;
	}

	return 0;
}
