#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

#define pii pair < int, int >
#define x first
#define y second

struct fenwick {
  int a [ 10004 ];

  void init ( void ){ memset ( a, 0, sizeof(a) ); }

  int sum ( int x ){ 
    int ret = 0; 
    for ( ; x > 0; x -= x & -x ) ret += a[x]; 
    return ret; 
  }
  void update ( int x, int val ){ for ( ; x <= 10000; x += x & -x ) a[x] += val; }

  int query ( int i, int j ){ return sum(j) - sum(i-1); }
};

int t, test;
fenwick log;
pii p [ 1003 ];

int main ( void ){
  scanf("%d",&t);
  while ( t-- > 0 ){
    ++test;
    log.init();
    int n;
    scanf("%d",&n);
    for ( int i = 0; i < n; ++i ) scanf("%d %d",&p[i].x,&p[i].y);
    sort ( p, p + n );

    int sol = 0;

    for ( int i = 0; i < n; ++i ){
      sol += log.query ( p[i].y, 10000 );
      log.update ( p[i].y, 1 );
    }

    printf("Case #%d: %d\n",test,sol);
  }
  return 0;
}
