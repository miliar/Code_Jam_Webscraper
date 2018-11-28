/* 
 * File:   main.cpp
 * Author: Bill
 *
 * Created on 2009年9月27日, 上午1:01
 */

#include <stdlib.h>
#include <cstdio>
#include <cstring>

/*
 * 
 */

int N , K , Ans , use ;
int S[110][60] ;
int D[110] ;
int P[110] ;
int que[110][110] ;
bool f[110][110] ;

bool can( int a , int b ){
    for( int i = 1 ; i < K ; ++i ){
        if( (S[a][i] > S[b][i] ) ^ (S[a][i-1]>S[b][i-1]) ) return true ;
        if( S[a][i] == S[b][i] || S[a][i-1] == S[b][i-1] ) return true ;
    }
    return false ;
}
bool DFS( int now ){
    if( now == N ){
        return true ;
    }
    bool find = false ;
    for( int i = 0 ; i < use ; ++i ){
        int cus = true ;
        for( int j = 1 ; j <= que[i][0] ; ++j ){
            if( f[now][que[i][j]] ){
                cus = false ;
            }
        }
        if( cus ){
            que[i][0]++ ;
            que[i][que[i][0]] = now ;
            if( DFS( now+1 ) ) return true ;
            que[i][0]-- ;
        }
    }
    if( !find ){
        if( use < Ans ){
            que[use][0] = 1 ;
            que[use][1] = now ;
            use++ ;
            if( DFS( now+1 ) ) return true ;
            else{
                use-- ;
                return false ;
            }
        }else return false ;
    }
    return false ;
}
void solve(){
    memset( D , 0 , sizeof( D ) ) ;
    scanf("%d%d",&N,&K);
    for( int i = 0 ; i < N ; ++i )
        for( int j = 0 ; j < K ; ++j ){
            scanf("%d",&S[i][j]);
        }
    for( int i = 0 ; i < N ; ++i )
        for( int j = i+1 ; j < N ; ++j ){
            f[i][j] = f[j][i] = can( i , j ) ;
            if( f[i][j] ){
                D[i]++ ;
                D[j]++ ;
            }
        }
    for( int i = 0 ; i < N ; ++i ) P[i] = i ;
    for( int i = 0 ; i < N ; ++i )
        for( int j = i+1 ; j < N; ++j )
            if( D[P[i]] < D[P[j]] ){
                int Tmp = P[i] ;
                P[i] = P[j] ;
                P[j] = Tmp ;
            }
    Ans = 1 ;
    use = 0 ;
    while( !DFS( 0 ) ){
        Ans++ ;
        use = 0 ;
    }
    printf("%d\n",Ans);
}
int main(int argc, char** argv) {
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T ;
    scanf("%d",&T);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d: ",i);
        solve();
    }
    return (EXIT_SUCCESS);
}

