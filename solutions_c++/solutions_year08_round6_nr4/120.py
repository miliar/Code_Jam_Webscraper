#include <stdio.h>
#include <string.h>

int n, m ;
bool adj_1[10][10], adj_2[10][10] ;

bool used[16] ;
int map[10] ;

bool test(){

	int i, j ;
	for( i=1 ; i<=m ; i++ ){
		for( j=1 ; j<=m ; j++ ){
			if( adj_2[i][j] && !(adj_1[map[i]][map[j]]) )
				return false ;
		}
	}

	return true ;
}


bool run( int index ){
	if( index > m )
		return test() ;

	for( int i=1 ; i<=n ; i++ ){
		if( used[i] )
			continue ;
		map[index] = i ;

		used[i] = true ;
		if( run(index+1) )
			return true ;
		used[i] = false ;
	}
	return false ;
}

int main(void){

	int cases, ca ;
	int i, p, q ;

	scanf("%d", &cases) ;
	for( ca=1 ; ca<=cases ; ca++ ){

		memset(adj_1, 0, sizeof(adj_1)) ;
		scanf("%d", &n) ;
		for( i=1 ; i<n ; i++ ){
			scanf("%d%d", &p, &q) ;
			adj_1[p][q] = adj_1[q][p] = true ;
		}

		memset(adj_2, 0, sizeof(adj_2)) ;
		scanf("%d", &m) ;
		for( i=1 ; i<m ; i++ ){
			scanf("%d%d", &p, &q) ;
			adj_2[p][q] = adj_2[q][p] = true ;
		}

		memset(used, 0, sizeof(used)) ;

		if( run(1) )
			printf("Case #%d: YES\n", ca) ;
		else
			printf("Case #%d: NO\n", ca) ;
	}

	return 0 ;
}
