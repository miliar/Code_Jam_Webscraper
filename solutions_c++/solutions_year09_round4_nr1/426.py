/* 
 * File:   main.cpp
 * Author: Bill
 *
 * Created on 2009年9月27日, 上午12:08
 */

#include <stdlib.h>
#include <cstdio>
#include <cstring>

/*
 * 
 */
int N ;
char st[70] ;
int H[70] ;

void swap( int&a , int&b ){
    int c = a ;
    a = b ;
    b = c ;
}
void solve(){
    scanf("%d",&N);
    for( int i = 0 ; i < N ; ++i ){
        scanf("%s",st);
        int L = strlen( st ) ;
        H[i] = 0 ;
        for( int j = L-1 ; j >= 0 ; --j )
            if( st[j] == '1' ){
                H[i] = j ;
                break ;
            }
    }
    int Ans = 0 ;
    for( int i = 0 ; i < N ; ++i ){
        if( H[i] <= i ) continue ;
        int j = 0 ;
        for( j = i+1 ; j < N ; ++j ){
            if( H[j] <= i ) break ;
        }
        if( j > N ) continue ;
        for( int k = j ; k > i ; --k ){
            swap( H[k] , H[k-1] );
            Ans++ ;
        }
    }
    printf("%d\n",Ans);
}
int main(int argc, char** argv) {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T ;
    scanf("%d",&T);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d: ",i);
        solve();
    }
    return (EXIT_SUCCESS);
}

