#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <inttypes.h>

using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")
#define _inline(f...) f() __attribute__((always_inline)); f
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); it++)
#define FOREACH(x...) _foreach(x)
#define REP(i,n) for(int i = 0;i < n;++i)
#define FUP(i,a,b) for(int i = (a); i <= (b);++i)
#define FDOWN(i,a,b) for(int i = (a); i >= (b);--i)
#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define PB push_back
#define MP make_pair
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(), (v).rend()

const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;

_inline(int cmp)(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

#define ladoA 0
#define ladoB 1

typedef struct{
	int ini ; int fim ;
	int lado ; bool exec ;
} trip ;

int sorting( const void *a , const void *b ){
	trip *i = (trip *) a ; trip *j = (trip *) b ;

	if( i -> ini < j -> ini ) return -1 ;
	if( i -> ini > j -> ini ) return 1 ;

	return i -> fim - j -> fim ;
}

int main(){

	int caso = 1 ;
	int n ;
	scanf("%d", &n ) ;

	while( n -- ){
		int t ; scanf("%d", &t ) ;

		int na , nb ;
		scanf("%d %d", &na , &nb ) ;

		trip T[ na + nb ] ;

		REP( i , na ){
			int hi , mi , hf , mf ;
			scanf("%d:%d %d:%d", &hi , &mi , &hf , &mf ) ;
			T[ i ].ini = hi * 60 + mi ; T[ i ].fim = hf * 60 + mf + t ;
			T[ i ].lado = ladoA ; T[ i ].exec = false ;
		}

		int j = na ;
		REP( i , nb ){
			int hi , mi , hf , mf ;
			scanf("%d:%d %d:%d", &hi , &mi , &hf , &mf ) ;
			T[ j ].ini = hi * 60 + mi ; T[ j ].fim = hf * 60 + mf + t ;
			T[ j ].lado = ladoB ; T[ j ].exec = false ;
			j++ ;
		}

		qsort( T , na + nb , sizeof( trip ) , sorting ) ;

		int train[ 2 ] = { 0 , 0 } ;

		REP( i , na + nb ){

			if( !T[ i ].exec ){ 
				T[ i ].exec = true ;

				train[ T[ i ].lado ] ++ ;

				int aux_lado = T[ i ].lado ;
				bool valido = true ;
				int time = T[ i ].fim ;

				while( valido ){
					aux_lado ++ ; aux_lado %= 2 ;
					valido = false ;
					int j = 0 ;

					for( j = 0 ; j < na + nb ; j++ ){
						if( !T[ j ].exec && T[ j ].lado == aux_lado ){
							if( T[ j ].ini >= time ){ valido = true ; break ; }
						}
					}

					if( valido ){ T[ j ].exec = true ; time = T[ j ].fim ; }

				}

			}

		}

		printf("Case #%d: %d %d\n", caso++ , train[ 0 ] , train[ 1 ] ) ;

	}

	return 0 ;
}

