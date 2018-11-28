#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int T;
int N;
int g[100];
int p;
int s;

int main( ){

   scanf( "%i", &T);

   for( int Case = 1;Case <= T; Case++)
   {
      scanf("%i %i %i", &N, &s, &p );
      for( int i =0 ; i< N;i++)
         scanf("%i", &g[i] );
      int tot = 0;
      for (int i = 0;i<N;i++)
      {
         if( g[i] == 0 )
         {
            if( p == 0 )
            {
               tot++;
            }
         }
         else
         if( g[i] / 3 >= p )
            tot++;
         else if( g[i] % 3 == 2 )
         {
            if( g[i] / 3 +1 >= p )
               tot++;
            else if( g[i] / 3 +2 >= p && s>0)
               tot++,s--;
         }
         else if( g[i] % 3 == 1 )
         {
            if( g[i] /3 +1 >= p )
                  tot++;
         }
         else
         {
            if( g[i] / 3 + 1 >= p && s>0 )
               tot++,s--;
         }
      }
      printf("Case #%i: %i\n", Case, tot);
   }
   return 0;

}
