#include <iostream>
#include <algorithm>
#include <cstdio>
#include <utility>
#include <map>
using namespace std ;
#define par pair<char,char>
#define f first
#define s second


void solve(  int T  )  {
	map <par,char>  C,  D  ;
	char S[105],  res[105],  tmp[5] ;
	int N, N2 ;
	int i ,j ;
	
	scanf("%d",&N ) ;
	while( N ) {
		N -- ;
		scanf("%s",tmp ) ;
		C[ par(  tmp[0],  tmp[1] ) ] = tmp[2] ;
		C[ par(  tmp[1],  tmp[0] ) ] = tmp[2] ;
	}
	scanf("%d",&N ) ;
	while( N ) {
		N -- ;
		scanf("%s",tmp ) ;
		D[ par(  tmp[0],  tmp[1] ) ] = 1 ;
		D[ par(  tmp[1],  tmp[0] ) ] = 1 ;
	}
	
	scanf("%d",&N ) ;
	scanf("%s",S ) ;
	N2 = 1 ;
	res[0] = S[0] ;
	for( i=1; i<N; i++ )   {
		res[ N2++ ] = S[i] ;
		if(  N2>1  &&  C.find(  par( res[N2-2], res[N2-1] )  )  !=  C.end()   )   {
			N2 -- ;
			res[ N2-1 ] = C[  par( res[N2-1], res[N2] )   ]   ;
		}
		else {
			for( j=0; j<N2-1; j++ )  {
				if(  D.find(  par( res[j], res[N2-1] )  )  !=  D.end()   )   {
					N2 = 0 ;
					break ;
				}
			}
		}
	}
	
	printf("Case #%d: [", T ) ;
	for( i=0; i<N2; i++ ) {
		if( i )
			printf(", ");
		printf("%c",res[i] ) ;
	}
	printf("]\n" ) ;
}

int main() {
	int T, i ;
	
	scanf("%d",&T ) ;
	for( i=0; i<T; i++ )
		solve(i+1) ;
	
	return 0 ;
}

