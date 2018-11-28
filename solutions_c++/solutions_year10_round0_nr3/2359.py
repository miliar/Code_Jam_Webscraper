#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

void proc(int caso) {
    int R, k, N;
    int g[1000] ;
    int fin[1000], sub[1000] ;
    bool usado[1000] ;
    int rep[1001], m = 0;
    int I, J ;
    scanf("%d%d%d",&k,&R,&N);
    for( I=0; I<N; I++ ) {
        scanf("%d",&g[I] ) ;
        fin[I] = 0 ;
        sub[I] = 0 ;
        rep[I] = 0 ;
        usado[I] = 0 ;
    }
    rep[N] = 0 ;
    for( I=0; I<N; I++ ) {
        sub[I] = g[I] ;
        for( fin[I] = (I+1)%N; fin[I]!=I && sub[I]<=R; fin[I]=(fin[I]+1)%N ) {
            sub[I] += g[ fin[I] ] ;
        }
        if( sub[I]>R ) {
            fin[I] = (fin[I]+N-1)%N ;
            sub[I] -= g[ fin[I] ] ;
        }
        //printf("    %d %d\n",sub[I],fin[I]);
    }
    int pos = 0 ;
    //printf("    ?%d\n",k);
    for( I=1; I<=k ; I++ ) {
        //printf("    ->%d\n",pos);
         rep[I] = rep[I-1] + sub[pos] ;
         //usado[pos] = 1 ;
         pos = fin[pos] ;
         m++;
         if( usado[pos] ) {
            break ;
         }
    }
    int ans = rep[m]*(k/m) + rep[k%m] ;
    printf("Case #%d: %d\n",caso,ans);
    return ;
}

int main() {
    int T, I ;
    scanf("%d",&T);
    for( I=0; I<T; I++ ) {
        proc(I+1);
    }
    return 0;
}
