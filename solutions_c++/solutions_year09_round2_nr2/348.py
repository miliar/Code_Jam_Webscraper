#include <stdio.h>
#include <string.h>


int num[10] ;
int len ;
char ans[32] ;
char str[32] ;

int run(int ind, int state){
    if( ind == len )
        return state ;
    
    int digit = 0 ;
    if( state == 0 ){
        ans[ind] = str[ind] ;
        digit = str[ind]-'0' ;
        num[digit] -- ;
        if( run( ind+1, 0 ) )
            return 1 ;
        num[digit] ++ ;
        digit++ ;
    }

    state = 1 ;
    for( ; digit<=9 ; digit++ ){
        if( num[digit] <= 0)
            continue ;
            
        ans[ind] = digit + '0' ;
        num[digit] -- ;
        if( run(ind+1, state) )
            return 1 ;
        num[digit] ++ ;
    }
    return 0 ;
}

void run_1(int ind){
    if( ind == len )
        return ;

    int digit ;
    if( ind == 0 )
        digit = 1 ;
    else
        digit = 0 ;

    for( ; digit<=9 ; digit++ ){
        if( num[digit] <= 0)
            continue ;

        ans[ind] = digit + '0' ;
        num[digit] -- ;
        run_1(ind+1) ;
        return ;
    }
}


int main(void){
    int T ;

    scanf("%d", &T) ;
    for( int i_cases=1 ; i_cases<=T ; i_cases++ ){
        memset(num, 0, sizeof(num)) ;
        scanf("%s", str) ;
        len = 0 ;
        for( char *s=str ; *s ; s++ ){
            num[(*s)-'0'] ++ ;
            len ++ ;
        }
        
        if( run(0, 0) ){
            ans[len] = 0 ;
            printf("Case #%d: %s\n", i_cases, ans) ;
        }
        else{
            len ++ ;
            num[0] ++ ;
            run_1(0) ;
            ans[len] = 0 ;
            printf("Case #%d: %s\n", i_cases, ans) ;
        }
    }

    return 0 ;
}

