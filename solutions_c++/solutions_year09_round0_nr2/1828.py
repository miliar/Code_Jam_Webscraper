/* 
 * File:   GCJ_B.cpp
 * Author: Bill
 *
 * Created on 2009年9月3日, 下午8:13
 */

#include <stdlib.h>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std ;
/*
 * 
 */

const int dir[4][2] = { -1 , 0 , 0 , -1 , 0 , 1 , 1 , 0 } ;
int T , H , W ;
char Chnow ;
char Ans[102][102] ;
int alt[102][102] ;

char DFS( int x , int y ){
    if( isalpha(Ans[x][y]) ){
        return Ans[x][y] ;
    }
    int low = alt[x][y] ;
    int find = -1 ;
    for( int i = 0 ; i < 4 ; ++i ){
        int tx = x + dir[i][0] ;
        int ty = y + dir[i][1] ;
        if( tx==0 || ty==0 || tx > H || ty > W ) continue ;
        if( alt[tx][ty] < alt[x][y] ){
            if( alt[tx][ty] < low ){
                low = alt[tx][ty] ;
                find = i ;
            }
        }
    }
    if( find == -1 ){
        return Ans[x][y] = Chnow++ ;
    }
    return Ans[x][y] = DFS( x+dir[find][0] , y+dir[find][1] ) ;
}
void solve(){
    Chnow = 'a' ;
    memset( Ans , 0 , sizeof( Ans ) ) ;
    scanf("%d%d",&H,&W);
    for( int i = 1 ; i <= H ; ++i )
        for( int j = 1 ; j <= W ; ++j ){
            scanf("%d",&alt[i][j]);
        }
    for( int i = 1 ; i <= H ; ++i )
        for( int j = 1 ; j <= W ; ++j )
            if( !isalpha(Ans[i][j]) ){
                DFS( i , j ) ;
            }
    for( int i = 1 ; i <= H ; ++i ){
        for( int j = 1 ; j < W ; ++j ) printf("%c ",Ans[i][j]);
        printf("%c\n",Ans[i][W]);
    }

}
int main(int argc, char** argv) {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&T);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d:\n",i);
        solve();
    }
    return (EXIT_SUCCESS);
}

