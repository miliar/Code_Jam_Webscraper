#include <stdio.h>
#include <string.h>


int H, W ;
int ans[128][128] ;
char map[128][128] ;


int get( int r, int c){

	if( r<1 || r>H )
		return 0 ;
	if( c<1 || c>W )
		return 0 ;

	if( map[r][c] )
		return 0 ;
	if( r==1 && c==1 )
		return 1 ;
	return ans[r][c] ;
}



int main(void){

	int n, R ;
	int r, c ;
	int cases ;

	scanf("%d", &n) ;

	for( cases=1 ; cases<=n ; cases++){
		scanf("%d%d%d", &H, &W, &R) ;
			
		memset(map, 0, sizeof(map)) ;
		while(R--){
			scanf("%d%d", &r, &c) ;
			map[r][c] = 1 ;
		}

		for( r=1 ; r<=H ; r++ ){
			for( c=1 ; c<=W ; c++){
				ans[r][c] = 0 ;

				ans[r][c] += get(r-1, c-2) ;
				ans[r][c] += get(r-2, c-1) ;
				ans[r][c] %= 10007 ;
			}
		}
		ans[1][1] = 1 ;

		printf("Case #%d: %d\n", cases, ans[H][W]) ;
	}

	return 0 ;
}
