#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std ;

void solve(int tC) {
	int N ;
	int pR[2], p ;
	int pos[100], tip[100],  uPos[100][2] ;	
	char S[5] ;
	int res = 0 ;
	int i, j ;
	pR[0] = 1, pR[1] = 1 ;
	
	scanf("%d",&N ) ;
	for( i=0; i<N; i++ ) {
		scanf("%s%d",S,&p ) ;
		pos[i] = p ;
		if(  S[0]=='B' )
			tip[i] = 0 ;
		else
			tip[i] = 1 ;
	}
	uPos[i][0] = 1 ;
	uPos[i][1] = 1 ;
	
	for( i=N-1; i>=0; i-- ) {
		uPos[i][0] = uPos[i+1][0] ;
		uPos[i][1] = uPos[i+1][1] ;
		uPos[i][ tip[i] ] = pos[i] ;
	}
	for( i=0; i<N; i++ ) {
		while(  pR[  tip[i]  ]  !=  pos[i]   )   {
			res ++ ;
			for( j=0; j<2; j++ )
				if(  pR[j] < uPos[i][j]  )
					pR[j] ++ ;
				else if(  pR[j] > uPos[i][j]  )
					pR[j] -- ;
		} 
		if( 1 ) {
			res ++ ;
			for( j=0; j<2; j++ )
				if(  pR[j] < uPos[i][j]  )
					pR[j] ++ ;
				else if(  pR[j] > uPos[i][j]  )
					pR[j] -- ;
		}
	}
	
	printf("Case #%d: %d\n", tC,  res  ) ;
}

int main() {
	int T, i ;
	
	scanf("%d",&T ) ;
	for( i=1; i<=T; i++ )
		solve( i ) ;
	
	return 0 ;
}

