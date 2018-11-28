#include <cstdio>

int X, S, R, T, N;
double corridor[101];

int main( void ) {
   int tc;
   scanf( "%d", &tc );
   for( int t = 1; t <= tc; ++t ) {
      scanf( "%d %d %d %d %d", &X, &S, &R, &T, &N );

      for( int i = 0; i <= 100; ++i ) corridor[i] = 0;
      corridor[0] = X;

      for( int i = 0; i < N; ++i ) {
         int b, e, w;
         scanf( "%d %d %d", &b, &e, &w );
         corridor[w] += e-b;
         corridor[0] -= e-b;
      }

      double rem = T;
      double ans = 0;
      for( int i = 0; i <= 100; ++i ) {
         double fast = corridor[i] / (R+i);
         if( fast > rem ) fast = rem;
         ans += fast;
         rem -= fast;
         corridor[i] -= (R+i)*fast;
         ans += corridor[i] / (S+i);
      }
      printf( "Case #%d: %lf\n", t, ans );
   }
   return 0;
}

