#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<fstream>
using namespace std ;

int  t , cs = 1 , n , m , f[105][105] ;
vector<string> mp(4) ;
int main(){
    freopen("t.out","w",stdout) ;
    cin >> t ;
    while ( t -- ){
        printf("Case #%d: ", cs ++ ) ;
        for ( int i = 0;i < 4 ;i ++)
            cin >> mp[i] ;
    // x win
    vector<string> xp(mp) ;
    vector<string> op(mp) ;
    for ( int i = 0;i < 4;i ++)
        for ( int j = 0;j < 4 ;j ++)
            if ( xp[i][j] == 'T' ) xp[i][j] = 'X' ;
    for (int i = 0;i<4;i ++)
        for ( int j = 0 ;j < 4;j ++)
            if ( op[i][j] == 'T' ) op[i][j] = 'O' ;
    for ( int i = 0 ; i < 4;i ++)
        if ( xp[i] == "XXXX" ) {
            printf("X won") ;
            goto l1 ;
        }
    for ( int i = 0;i < 4;i ++)
        if ( xp[0][i] == 'X' &&
             xp[1][i] == 'X' &&
             xp[2][i] == 'X' &&
             xp[3][i] == 'X' )
        {
            printf("X won") ;
            goto l1 ;
        }
    if ( xp[0][0] == 'X' &&
         xp[1][1] == 'X' &&
         xp[2][2] == 'X' &&
         xp[3][3] == 'X' ){
        printf("X won") ;
        goto l1 ;
    }
    if ( xp[0][3] == 'X' &&
         xp[1][2] == 'X' &&
         xp[2][1] == 'X' &&
         xp[3][0] == 'X' )
     {
        printf("X won") ;
        goto l1 ;
    }
    // o win

    for ( int i = 0 ; i < 4;i ++)
        if ( op[i] == "OOOO" ) {
            printf("O won") ;
            goto l1 ;
           }
    for ( int i = 0;i < 4;i ++)
        if ( op[0][i] == 'O' &&
             op[1][i] == 'O' &&
             op[2][i] == 'O' &&
             op[3][i] == 'O' )
        {
            printf("O won") ;
            goto l1 ;
        }
    if ( op[0][0] == 'O' &&
         op[1][1] == 'O' &&
         op[2][2] == 'O' &&
         op[3][3] == 'O' )
    {
        printf("O won") ;
        goto l1 ;
    }
    if ( op[0][3] == 'O' &&
         op[1][2] == 'O' &&
         op[2][1] == 'O' &&
         op[3][0] == 'O' )
    {
        printf("O won") ;
        goto l1 ;
    }
    for ( int i = 0;i < 4;i ++)
        for ( int j = 0;j < 4;j ++)
            if ( mp[i][j] == '.')
            {
                printf("Game has not completed") ;
                goto l1 ;
            }
    printf("Draw") ;
l1:printf("\n") ;  ;
}
return 0 ;
}
