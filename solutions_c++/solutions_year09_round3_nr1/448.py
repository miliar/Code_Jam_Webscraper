/* 
 * File:   main.cpp
 * Author: Bill
 *
 * Created on 2009年9月13日, 下午5:53
 */

#include <stdlib.h>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std ;
/*
 * 
 */
int dir[257];
char st[70] ;

int T ;

void solve(){
    memset( dir , -1 , sizeof( dir ) );
    scanf("%s",st);
    dir[st[0]] = 1 ;
    int Len = strlen( st ) ;
    int Now = 0 ;
    for( int i = 1 ; i < Len ; ++i ){
        if( dir[st[i]] != -1 ) continue ;
        dir[st[i]] = Now ;
        if( Now == 0 ) Now = 2 ;
        else Now++ ;
    }
    long long Ans = 0 ;
    if( Now == 0 ) Now = 2 ;
    for( int i = 0 ; i < Len ; ++i ){
        Ans *= (long long)Now ;
        Ans += (long long)dir[st[i]] ;
    }
    cout<<Ans<<endl;
}
int main(int argc, char** argv) {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d: ",i);
        solve();
    }
    return (EXIT_SUCCESS);
}

