#include <stdio.h>
#include <string.h>

int g[10240], c[10240] ;
bool set[10240][2], able[10240][2] ;
int cost[10240][2] ;

int m, v ;

int dp(int node, int value){
	int i ;
	int lv, rv, ans, gate ;
	int re, sum, min ;
	
	if( set[node][value] )
		return cost[node][value] ;
	
	if( node *2 > m ){
		if( g[node] == value )
			return 0 ;
		else
			return -1 ;
	}
		
	if( c[node]==0 ){
		min = 0x7FFFFFFF ;
		for(lv=0 ; lv<=1 ; lv++ ){
			for( rv=0 ; rv<=1 ; rv++){
			
				if(g[node]==0)
					ans = lv|rv ;
				else
					ans = lv&rv ;
					
				if(ans == value ){
					re = dp(node*2, lv) ;
					if( re < 0 )
						continue ;
					sum = re ;
					
					re = dp(node*2+1, rv) ;
					if( re < 0 )
						continue ;
					sum += re ;
					
					if( min > sum )
						min = sum ;
				}				
			}
		}		
	}
	else{
		min = 0x7FFFFFFF ;
		for(lv=0 ; lv<=1 ; lv++ ){
			for( rv=0 ; rv<=1 ; rv++){
			
				for(gate=0 ; gate<=1 ; gate++ ){
					if(gate==0)
						ans = lv|rv ;
					else
						ans = lv&rv ;
				
					if(ans == value ){
						re = dp(node*2, lv) ;
						if( re < 0 )
							continue ;
						sum = re ;
						
						re = dp(node*2+1, rv) ;
						if( re < 0 )
							continue ;
						sum += re ;
						
						if( gate != g[node] )
							sum ++ ;
						if( min > sum )
							min = sum ;
					}	
				}
			}
		}		
	}
	
	if(min==0x7FFFFFFF){
		cost[node][value] = -1 ;
		able[node][value] = false ;
	}
	else{
		cost[node][value] = min ;
		able[node][value] = true ;
	}
	set[node][value] = true ;
	return cost[node][value] ;
}


int main(void){

	int n, cases ;
	int i, e ;
	
	scanf("%d", &n) ;
	for( cases=1 ; cases<=n ; cases++){
		scanf("%d%d", &m, &v) ;
		
		e = (m-1)/2 ;
		for( i=1 ; i<=e ; i++)
			scanf("%d%d", &g[i], &c[i]) ;
		for( ; i<=m ; i++)
			scanf("%d", &g[i]) ;
			
		memset(set, 0, sizeof(set)) ;
		memset(able, 0, sizeof(able)) ;
		
		printf("Case #%d:", cases) ;
		if( dp(1,v)>=0 )
			printf(" %d\n", dp(1,v)) ;
		else
			puts(" IMPOSSIBLE") ;
	}
	
	return 0 ;
}
