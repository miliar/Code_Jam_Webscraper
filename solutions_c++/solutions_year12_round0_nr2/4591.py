#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

#define MAXN 120

int T , N , S , P;
int t[MAXN];

int best ( int N , int S , int P ) {

    int Best = 0;

    int maxP = 0;

    if ( P != 1 )
     maxP = P + 2*(P-2);
    else
     maxP = 1;


    for ( int j = 1; j <= N; ++j ) {

     if ( t[j] >= (maxP+2) ) {
      ++Best;
     }else if ( t[j] < maxP ) {
      continue;
     }else {
      if ( S != 0 ) {
       ++Best;
       --S;
       if ( S == 0 )
        maxP += 2;
      }
     }

    }

    return ( Best );

}

int main ( ) {

    freopen("in.txt","r",stdin);
    freopen("out.out","w",stdout);

    scanf ( "%d" , &T );

    for ( int i = 1; i <= T; ++i ) {

     scanf ( "%d %d %d" , &N , &S , &P );

     for ( int j = 1; j <= N; ++j )
      scanf ( "%d" , &t[j] );

     printf ( "Case #%d: %d\n" , i , best(N,S,P) );

    }

    return 0;

}
