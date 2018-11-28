#include <stdio.h>
#include <string.h>

int N, S, Q ;

char name[128][128] ;
bool used[128] ;
int left ;


int ind(char* str){
	int i ;
	for( i=0 ; i<S ; i++){
		if( !strcmp(str, name[i]) )
			break ;
	}
	return i ;
}

int main(void){

	int cases ;
	char now[128] ;
	int i, j, ans ;
	
	gets(now) ;
	sscanf(now, "%d", &N) ;
	for( cases=1 ; cases<=N ; cases++){
		gets(now) ;
		sscanf(now, "%d", &S) ;
		for( i=0 ; i<S ; i++)
			gets(name[i]) ;
			
			
		gets(now) ;
		sscanf(now, "%d", &Q) ;
		
		ans = 0 ;
		memset(used, 0, sizeof(used)) ;
		left = S ;
		
		for( i=0 ; i<Q ; i++){
			j = ind(gets(now)) ;
			if( !used[j] ){
				used[j] = true ;
				left -- ;
				
				if( left == 0 ){
					ans ++ ;
					memset(used, 0, sizeof(used)) ;
					used[j] = true ;
					left = S-1 ;
				}
			}
		}			

		printf("Case #%d: %d\n", cases, ans) ;
	}
	
	return 0 ;
}


