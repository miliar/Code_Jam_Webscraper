#include <cstdio>
#include <iostream>
#include <set>

using namespace std;
typedef unsigned long long ull;

int main()
{
  int T;
  scanf("%d", &T);
  for( int C = 1; C <= T; ++C )
  {
    int a, b;
    scanf("%d %d", &a, &b);
    
    int q = 1;
    while( a / q >= 10 )
      q *= 10;

    set<pair<int,int> > all;
    
    int A = a;
    for( ; a <= b; ++a )
    {
      for( int p = 10; p <= a; p *= 10 )
      {
        int c = (10*q/p)*(a%p) + (a/p);
        if( A <= c && c < a )
          all.insert(make_pair(c, a));
      }
    }
    
    printf("Case #%d: %d\n", C, all.size());
  }
  return 0;
}