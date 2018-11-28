#include <stdio.h>
#include <string.h>

int n ;

int end[64] ;
char str[64] ;

int main(void){
    int T ;
    int ans ;

    scanf("%d", &T) ;
    for( int i_cases=1 ; i_cases<=T ; i_cases++ ){
        scanf("%d", &n) ;
        for( int i=0 ; i<n ; i++ ){
            scanf("%s", str) ;
            end[i] = -1 ;

            for( int j=0 ; j<n ; j++ ){
                if( str[j] !='0' )
                    end[i] = j ;
            }
        }
        
        ans = 0 ;
        
        for( int i=0 ; i<n ; i++ ){
            int j ;
            for( j=i ; j<n ; j++ ){
                if( end[j] <= i )
                    break ;
            }
            
            int tmp = end[j] ;
            for( ; j>i ; j-- ){
                end[j] = end[j-1] ;
                ans ++ ;
            }
            end[i] = end[j] ;
        }
        
        printf("Case #%d: %d\n", i_cases, ans) ;
    }

    return 0 ;
}

