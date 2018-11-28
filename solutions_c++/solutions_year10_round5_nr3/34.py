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

int main( void )
{
  int T;
  cin >> T;
  for( int CC = 1; CC <= T; ++ CC ){
    int C;
    cin >> C;
    map<int,int> P;
    for( int i = 0; i < C; i ++ ){
      int a, b;
      cin >> a >> b;
      P[a] += b;
    }
    map<int,int> Q;
    long long ret = 0;
    while( 1 ){
      Q.clear();
      long long NG = 0; // count
      for( map<int,int>::const_iterator it = P.begin(), ite = P.end(); it != ite; ++ it ){
        Q[it->first - 1] += it->second / 2;
        Q[it->first + 1] += it->second / 2;
        Q[it->first    ] += it->second % 2;
        NG += it->second / 2;
      }
      if( NG == 0 )
      break;
      ret += NG;
      P.swap( Q );
    }

    printf( "Case #%d: %lld\n", CC, ret );
  }
}
