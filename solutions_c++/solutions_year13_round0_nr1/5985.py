#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
using namespace std ;

struct node
{
    char map[5][5] ;
} ;

node pre ;

int judge( node pre )
{
    int i , j , k , ans ;
    char s[2] = {'X' , 'O'} ;
    for( i = 0 ; i < 2 ; i ++ )
    {
        ans = 0 ;
        for( j = 0 ; j < 4 ; j ++ )
        {
            if( pre.map[j][j] == 'T' || pre.map[j][j] == s[i] )
                ans ++ ;
        }
        if( ans == 4 )
            return i + 1 ;
        for( ans = 0 , j = 0 ; j < 4 ; j ++ )
        {
            if( pre.map[j][3 - j] == 'T' || pre.map[j][3 - j] == s[i] )
                ans ++ ;
        }
        if( ans == 4 )
            return i + 1 ;
    }
    for( i = 0 ; i < 2 ; i ++ )
    {
        for( j = 0 ; j < 4 ; j ++ )
        {
            for( k = 0 , ans = 0 ; k < 4 ; k ++ )
            {
                if( pre.map[j][k] == 'T' || pre.map[j][k] == s[i] )
                    ans ++ ;
            }
            if( ans == 4 )
                return i + 1 ;
        }
    }
    for( i = 0 ; i < 2 ; i ++ )
    {
        for( j = 0 ; j < 4 ; j ++ )
        {
            for( k = 0 , ans = 0 ; k < 4 ; k ++ )
            {
                if( pre.map[k][j] == 'T' || pre.map[k][j] == s[i] )
                    ans ++ ;
            }
            if( ans == 4 )
                return i + 1 ;
        }
    }
    for( i = 0 ; i < 4 ; i ++ )
    {
        for( j = 0 ; j < 4 ;j  ++ )
            if( pre.map[i][j] == '.' )
                return 3 ;
    }
    return 0 ;
}

int main()
{
    freopen("in.txt" , "r" , stdin) ;
    freopen("out.txt" , "w" , stdout) ;
    int cas , i , j , T ;
    scanf("%d" , &T) ;
    for( cas = 1 ; cas <= T ; cas ++ )
    {
        for( i = 0 ; i < 4 ; i ++ )
            scanf("%s" , pre.map[i]) ;
        if( judge( pre ) == 1 )
            printf("Case #%d: X won\n" , cas) ;
        else if( judge( pre ) == 2 )
            printf("Case #%d: O won\n" , cas) ;
        else if( judge( pre ) == 3 )
            printf("Case #%d: Game has not completed\n" , cas) ;
        else
            printf("Case #%d: Draw\n" , cas) ;
    }
    return 0 ;
}
