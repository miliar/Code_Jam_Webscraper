#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<algorithm>
#include<stdlib.h>
#include<queue>
#include<iostream>
typedef long long LL;
using namespace std;

#define MAX 1000002
int sieve[MAX];


int main( void )
{
  memset( sieve, 0x1, sizeof(sieve) );
  sieve[0] = 0;
  sieve[1] = 0;
  long long PC = 0;
  for( int i = 2; i < MAX; i ++ ){
    if( sieve[i] ){
      PC += i;
      for( int j = i * 2; j < MAX; j += i )
        sieve[j] = 0;
    }
  }

  int T;
  cin >> T;
  for( int CC = 1; CC <= T; ++ CC ){
    int D, K;
    cin >> D >> K;
    vector<int> S(K);
    int maxS = 0;
    for( int i = 0; i < K; i ++ ){
      cin >> S[i];
      maxS = max( maxS, S[i] + 1 );
    }

    int max = 1;
    for( int i = 0; i < D; i ++ )
      max *= 10;

    int ans = -1;

    if( K == 1 ) goto IDN;
    if( K == 2 ){
      if( S[0] == S[1] )
        ans = S[0];
      else
        goto IDN;
      goto ANS;
    }
//    cerr << maxS << endl;
    for( int P = maxS; P <= max; P ++ ){
      if( sieve[P] ){
        LL S12 = (S[1] - S[2] + P) % P;
        LL S01 = (S[0] - S[1] + P) % P;
        LL invS01 = 1;
        for( LL t = 1, x = S01; t <= P-2; t <<= 1, x = (x * x) % P ){
          if( (P-2) & t ){
            invS01 = (invS01 * x) % P;
          }
        }
        LL A = (S12 * invS01) % P;
        LL B = (S[1] - (S[0] * A) % P + P) % P;
        for( int i = 1; i < K; i ++ )
          if( (S[i-1] * A + B) % P != S[i] )
            goto NGA;
        int v = (S[K-1] * A + B) % P;
//        cerr << P << " " << A << " " << B << " -> " << v << endl;
        if( ans < 0 || ans == v )
          ans = v;
        else
          goto IDN;
        NGA:;
      }
    }
    ANS:
    printf( "Case #%d: %d\n", CC, ans );
    continue;
    IDN:
    printf( "Case #%d: %s\n", CC, "I don't know." );
  }
}
