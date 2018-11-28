#include <iostream>
#include <algorithm>

const int MAX = 100;

int H, W, A[MAX][MAX];

void ReadData()
{
   memset( A, 0, sizeof(A) );
   int r;
   std::cin >> H >> W >> r;
   for( int i = 0; i<r; ++i )
   {
      int x, y;
      std::cin >> x >> y;
      A[x-1][y-1] = -1;
   }
}

int Work()
{
   A[0][0] = 1;
   for( int i = 0; i<H; ++i )
      for( int j = 0; j<W; ++j )
      {
         if( A[i][j]<=0 )
            continue;
         int i0 = i+2, j0 = j+1;
         if( i0<H && j0<W && A[i0][j0]!=-1 )
            A[i0][j0] = (A[i][j]+A[i0][j0])%10007;
         i0 = i+1;
         j0 = j+2;
         if( i0<H && j0<W && A[i0][j0]!=-1 )
            A[i0][j0] = (A[i][j]+A[i0][j0])%10007;
      }
   return A[H-1][W-1]%10007;
}

void Output( int t, int res )
{
   std::cout << "Case #" << t << ": ";
   //if( res<0 )
   //   std::cout << "IMPOSSIBLE";
   //else
      std::cout << res;
   std::cout << std::endl;
}

int main()
{
   int t;
   std::cin >> t;
   for( int i = 1; i<=t; ++i )
   {
      ReadData();
      Output( i, Work() );
   }
   return 0;
}

