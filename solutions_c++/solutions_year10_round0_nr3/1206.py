#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

#define MaxN 1003
#define LL long long

int R, t, k, N, test;
int G [ MaxN ];
int bio [ MaxN ], next [ MaxN ], cookie;
LL suma [ MaxN ], sol;

void solve_test ( void ){
  sol = 0;
  memset ( bio, 0, sizeof(bio) );
  memset ( suma, 0, sizeof(suma) );

  scanf("%d %d %d",&R,&k,&N);
  for ( int i = 0; i < N; ++i )
    scanf("%d",&G[i]);

  cookie = 1;
  int idx = 0;

  while ( !bio[idx] && R-- > 0 ){
    int room = k, start = idx;
    bio[idx] = cookie;
    ++cookie;

    idx = ( idx + 1 ) % N;
    room -= G[start];
    suma[start] += G[start];

    while ( idx != start && room >= G[idx] ){
      room -= G[idx];
      suma[start] += G[idx];
      idx = ( idx + 1 ) % N;
    }    

    next [ start ] = idx;
    sol += suma[start];
  }
  LL cyc = 0;
  int len = 0;
  memset ( bio, 0, sizeof(bio) );

  while ( !bio[idx] && R-- > 0 ){
    sol += suma[idx];
    cyc += suma[idx];

    bio[idx] = 1;
    ++len;
    idx = next[idx];
  }

  if ( R > 0 ){
    int tot = R / len;
    sol += tot * cyc;
    R %= len;
  }

  while ( R-- > 0 ){
    sol += suma[idx];    
    idx = next[idx];
  }
  
  printf("%I64lld\n",sol);
}

int main ( void ){
  scanf("%d",&t);
  while ( t-- > 0 ){
    ++test;
    printf("Case #%d: ",test);
    solve_test();
  }

  return 0;
}
