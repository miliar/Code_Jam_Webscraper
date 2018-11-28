#include <stdio.h>
#include <string.h>

int sr, sc ;
char map[16][16] ;


int dp[16][1024] ;


void set0(){

	int c, num ;
	int i ;

	for( c=(1<<sc)-1 ; c>=0 ; c-- ){
		num = 0 ;
		for( i=0 ;i<sc ; i++ ){
			if( c & (1<<i) ){
				if( map[0][i]=='x' )
					break ;
				if( i-1>=0 && (c&(1<<(i-1)) ) )
					break ;
				num ++ ;
			}
		}
		if( i<sc )
			dp[0][c] = -1 ;
		else
			dp[0][c] = num ;
	}
}

void run(int r, int c){

	int last_c, num ;
	int i, last_i ;
	int opt = 0 ;

	for( last_c=(1<<sc)-1 ; last_c>=0 ; last_c-- ){
		if( dp[r-1][last_c] < 0 )
			continue ;

		num = 0 ;
		for( i=0 ;i<sc ; i++ ){
			if( c & (1<<i) ){
				if( map[r][i]=='x' ){
					dp[r][c] = -1 ;
					return ;
				}
				if( i-1>=0 && (c&(1<<(i-1)) )){
					dp[r][c] = -1 ;
					return ;
				}

				last_i = i-1 ;
				if( last_i>=0 && (last_c&(1<<last_i)) )
					break ;
				last_i = i+1 ;
				if( last_i<sc && (last_c&(1<<last_i)) )
					break ;

				num ++ ;
			}
		}
		if( i<sc )
			continue ;

		num += dp[r-1][last_c] ;
		if(opt<num)
			opt = num ;
	}

	dp[r][c] = opt ;
}



int main(void){

	int n, cases ;
	int r, c ;
	int ans ;


	scanf("%d", &n) ;
	for( cases=1 ; cases<=n ; cases++ ){
		scanf("%d%d", &sr, &sc) ;

		for(r=0 ; r<sr ; r++)
			scanf("%s", map[r]) ;

		set0() ;
		for(r=1 ; r<sr ; r++ ){
			for( c=(1<<sc)-1 ; c>=0 ; c-- )
				run(r,c) ;
		}

		ans = 0 ;
		for( c=(1<<sc)-1 ; c>=0 ; c-- ){
			if( ans < dp[sr-1][c] )
				ans = dp[sr-1][c] ;
		}

		printf("Case #%d: %d\n", cases, ans) ;
	}
	return 0 ;
}
