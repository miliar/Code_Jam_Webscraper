/* 
 * File:   GCJ_C.cpp
 * Author: Bill
 *
 * Created on 2009年9月3日, 下午8:53
 */

#include <stdlib.h>
#include <cstring>
#include <cstdio>
/*
 * 
 */
int T ;
const char str[20] = "welcome to code jam";
char st[505] ;
int f[21] ;

void solve(){
    memset( f , 0 , sizeof(f) ) ;
    f[0] = 1 ;
    int Len = strlen( st ) ;
    for( int i = 0 ; i < Len ; ++i ){
        for( int j = 18 ; j >= 0 ; --j )
            if( st[i] == str[j] ){
                f[j+1] += f[j] ;
                f[j+1] %= 10000 ;
            }
    }
    if( f[19] < 10 ) printf("000%d\n",f[19]) ;
    else if( f[19] <100 ) printf("00%d\n",f[19]) ;
    else if( f[19] < 1000 ) printf("0%d\n",f[19]) ;
    else printf("%d\n",f[19]);
}
int main(int argc, char** argv) {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&T);
    gets(st);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d: ",i);
        gets( st );
        solve();
    }
    return (EXIT_SUCCESS);
}

