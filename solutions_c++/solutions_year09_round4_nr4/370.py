/* 
 * File:   main.cpp
 * Author: Bill
 *
 * Created on 2009年9月27日, 上午12:41
 */

#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std ;

/*
 * 
 */

int N ;
int x[60] , y[60] , r[60] ;

double dis( int a , int b ){
    return sqrt( (x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b])*(y[a]-y[b]) );
}
void solve(){
    scanf("%d",&N);
    for( int i = 0 ; i < N ; ++i ){
        scanf("%d%d%d",&x[i],&y[i],&r[i]);
        
    }
    if( N == 1 ){
        printf("%.6lf\n",r[0]*1.0);
        return ;
    }
    if( N == 2 ){
        printf("%.6lf\n",max(r[0],r[1])*1.0);
        return ;
    }
    if( N == 3 ){
        double Ans = 1e10 ;
        double tmp = max( r[2]*1.0 , ( r[0]+r[1]+dis( 0 , 1 ) ) / 2 ) ;
        if( tmp < Ans ) Ans = tmp ;
        tmp = max( r[0]*1.0 , ( r[2]+r[1]+dis( 2 , 1 ) ) / 2 ) ;
        if( tmp < Ans ) Ans = tmp ;
        tmp = max( r[1]*1.0 , ( r[0]+r[2]+dis( 0 , 2 ) ) / 2 ) ;
        if( tmp < Ans ) Ans = tmp ;
        printf("%.8lf\n",Ans);
        return ;
    }
}

int main(int argc, char** argv) {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    int T ;
    scanf("%d",&T);
    for( int i = 1 ; i <= T ; ++i ){
        printf("Case #%d: ",i);
        solve();
    }
    return (EXIT_SUCCESS);
}

