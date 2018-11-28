// 14.04.2011    Problem C. Recycled Numbers
//
// Case #1: 2 3

# include <stdio.h>

const int N = 3001;

int n, k, a, b, d;
bool e [N][N];
int i, ii, j, l, j2, ll, p;

int main ()
{
//
   freopen ("C.IN", "r", stdin);
   freopen ("C.OUT", "w", stdout);
//

   scanf ("%d\n", &n);
//   printf ("%d\n", n);
   for ( i=1; i <= n; i++ )
   {
      scanf ("%d %d", &a, &b);
//printf ("%d %d %d\n", i, a, b);
      for ( l=a, p=1, ll=0, k=0; l > 0; l/=10, p*=10, ll++ )
         ;
      p /= 10;

      for ( int ii=1, jj; ii <= b; ii++ )
         for ( j=1; j < ii; j++ )
            e [ii][j] = false;

      for ( j=a; j <= b; j++ )
      {
         for ( l=j, j2=1; j2 < ll; j2++ )
         {
            d = l%10, l /= 10;
            l += p*d;
            if ( l >= a && l <= b && l < j )
               {
                  e [j][l] = true; 
//                  printf ("%3d) n=%5d m=%5d\n", k, l, j);
//                  break;
               }
         }
      }

      for ( int ii=1, jj; ii <= b; ii++ )
         for ( j=1; j < ii; j++ )
            k += e [ii][j];

      printf ("Case #%d: %d\n", i, k);
   }

   return 0;
}
