#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int T, N, K, test;

int main ( void ){
  scanf("%d",&T);
  while ( T-- > 0 ){
    ++test;

    scanf("%d %d",&N,&K);
    int pow = 1 << N;

    printf("Case #%d: ",test);
    if ( K + 1 >= pow && (K+1) % pow == 0 )
      puts("ON");
    else
      puts("OFF");

  }

  return 0;
}
