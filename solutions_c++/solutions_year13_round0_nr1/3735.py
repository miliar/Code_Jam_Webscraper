#include <iostream>
#include <sstream>
#include <bitset>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <numeric>
#include <list>
#define FOR(i,A) for(typeof (A).begin() i = (A).begin() ; i != (A).end() ; i++)
#define mp make_pair
#define debug( x ) cout << #x << " = " << x << endl
#define clr(v,x) memset( v, x , sizeof v )
#define all(x) (x).begin() , (x).end()
#define rall(x) (x).rbegin() , (x).rend()
#define f(i,a,b) for(int i = a ; i < b ; i++)
#define fd(i,a,b) for(int i = a ; i >= b ; i--)
#define TAM 110

using namespace std;

typedef pair<int,int> ii ;
typedef long long ll ;
typedef long double ld ;
typedef pair<int,ii> pii ;

int win( string s ){
	int x = 0 , o = 0 , t = 0 ;
	for(int i = 0 ; i < s.size() ; i++) x += ( s[ i ] == 'X' ) , o += ( s[ i ] == 'O' ) , t += ( s[ i ] == 'T' ) ;
	if( x == 4 || ( x == 3 && t == 1 ) ) return 1 ;
	if( o == 4 || ( o == 3 && t == 1 ) ) return -1 ;
	return 0 ;
}

int main(){

	int test ;
	scanf("%d" , &test ) ;
	cin.ignore() ;
	vector<string> tab( 5 ) ;
	string resp , s = "TTTT" ;

	f( k , 1 , test + 1 ){
		f( i , 0 , 5 ) getline( cin , tab[ i ] ) ;

		int r , x , o , t ;
		resp = "" ;
		//FILAS
		f( i , 0 , 4 ){
			r = win( tab[ i ] ) ;
			if( r != 0 ){
				if( r > 0 ) resp = "X won" ;
				else resp = "O won" ;
				break ;
			}
		}
		if( resp != "" ){
			printf("Case #%d: %s\n" , k , resp.c_str() ) ;
			continue ;
		}
		//COLUMNAS
		f( i , 0 , 4 ){
			f( j , 0 , 4 ) s[ j ] = tab[ j ][ i ] ;
			r = win( s ) ;
			if( r != 0 ){
				if( r > 0 ) resp = "X won" ;
				else resp = "O won" ;
				break ;
			}
		}
		if( resp != "" ){
			printf("Case #%d: %s\n" , k , resp.c_str() ) ;
			continue ;
		}
		//DIAGONAL 1
		f( i , 0 , 4 ) s[ i ] = tab[ i ][ i ] ;
		r = win( s ) ;
		if( r != 0 ){
			if( r > 0 ) resp = "X won" ;
			else resp = "O won" ;
		}
		if( resp != "" ){
			printf("Case #%d: %s\n" , k , resp.c_str() ) ;
			continue ;
		}
		//DIAGONAL 2
		f( i , 0 , 4 ) s[ i ] = tab[ i ][ 3 - i ] ;
		r = win( s ) ;
		if( r != 0 ){
			if( r > 0 ) resp = "X won" ;
			else resp = "O won" ;
		}
		if( resp != "" ){
			printf("Case #%d: %s\n" , k , resp.c_str() ) ;
			continue ;
		}

		//DRAW OR NOT COMPLETED
		int vacio = 0 ;
		f( i , 0 , 4 ) f( j , 0 , 4 ) vacio += ( tab[ i ][ j ] == '.' ) ;
		if( vacio ) resp = "Game has not completed" ;
		else resp = "Draw" ;
		printf("Case #%d: %s\n" , k , resp.c_str() ) ;
	}

    return 0 ;
}

