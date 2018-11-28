#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
#include <iostream>
using namespace std;
#define mp make_pair
typedef long long ll;

int marc[ 200 ][ 200 ];
int casos, n;

double wp( int t, int pular  ){
	int cont = 0, w = 0;
	
	for( int i = 0; i < n; ++i ){
		if( i == pular ) continue;
		
		if( marc[ t ][ i ] != -1 ){
			++cont;
			if( marc[ t ][ i ] == 1 )
				++w;
		}		
	}
	
	return double(w)/double(cont);
}

double owp( int t ){
	double soma = 0;
	int cont = 0;
	
	for( int i = 0; i < n; ++i ){
		if( i == t || marc[ t ][ i ] == -1 ) continue;
		++cont;
		soma += wp( i, t );
	}
	
	return soma / double( cont );
}

double oowp( int t ){
	double soma = 0;
	int cont = 0;
	
	for( int i = 0; i < n; ++i ){
		if( i == t || marc[ t ][ i ] == -1 ) continue;
		++cont;
		soma += owp( i );
	}
	
	return soma / double( cont );
}

int main(){
	char temp;
	scanf( "%d", &casos );
	for( int c = 1; c <= casos; ++c ){
		memset( marc, -1, sizeof( marc ) );
		
		scanf( "%d", &n );
		for( int i = 0; i < n; ++i ){
			for( int j = 0; j < n; ++j ){
				cin >> temp;
				if( temp != '.' )
					marc[ i ][ j ] = temp - '0';
			}		
		}
				
		printf( "Case #%d:\n", c );
		for( int i = 0; i < n; ++i ){
		//	cout << "TIme " << i << " " << owp( i ) << endl;
			printf( "%.12llf\n", 0.25 * wp( i, i ) + 0.50 * owp( i ) + 0.25 * oowp( i ) );
		}
	}
}
