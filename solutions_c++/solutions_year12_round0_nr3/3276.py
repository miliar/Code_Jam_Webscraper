#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cmath>
#define  MAX 2000000
#define  REP(i,n) for( int i =0;i<n;i++)
#define  REPi(i,a,n) for(int i =a;i<n;i++)
using namespace std;
int a,b;
int n[9];
int tot;

void dign( int x )
{
   int dig = 0;
   int xo = x;
   while( x > 0 )
   {
      n[dig++] = x % 10;
      x /= 10;
   }
   int digN = dig;
   for( int k = 1;k<digN; k++)
   {
      //n[0] = n[dig-1]
      int t = n[0];
      for( int j = 1; j<dig; j++)
         n[j-1] = n[j];
      n[dig-1] = t;
      if( t == 0 )
      {
         dig--;
         return;
      }
      int number = 0;
      bool zero = false;
      for( int j = 0; j< dig; j++)
      {
         if( n[j] == 0)
            zero = true;
         number += pow( 10, j ) * n[j];
      }
      if( number == xo )
         return;
      if( number >= a && number <= b )
      {
         if( number < xo )
         {
            tot++;
         }
         else if( zero && number > xo )
         {
            tot++;
         }
      }
   }
}
int main( )
{
   int T;

   scanf("%i", &T);

   for( int Case = 1;Case <=T;Case++)
   {
      printf("Case #%i: ", Case);
      tot =0;
      scanf("%i %i", &a, &b );
      for( int i = b; i>=a; i--)
      {
         dign( i );
      }
      printf("%i\n", tot );
   }

   return 0;
}
