#include <iostream>
#include <algorithm>

const int MAX = 10;
const int MAX_W = (1 << MAX);

int M, N, A[MAX][MAX], B[MAX+1][MAX_W];

void ReadData()
{
   memset( A, 0, sizeof(A) );
   memset( B, -1, sizeof(B) );
   int r;
   std::cin >> M >> N;
   for( int i = 0; i<M; ++i )
   {
      char s[MAX+1];
      std::cin >> s;
      for( int j = 0; j<N; ++j )
         A[i][j] = (s[j]=='.' ? 0 : 1);
   }
}

bool IsBroken( int i, int k )
{
   for( int j = 0; j<N; ++j )
      if( A[i][j] && (k&(1<<j))!=0 )
         return true;
   return false;
}

bool IsBeat( int j, int k )
{
   if( j&(k<<1) )
      return true;
   if( j&(k>>1) )
      return true;
   for( int i = 0; i<N; ++i )
      if( (k&(1<<i))!=0 && (k&(1<<(i+1)))!=0 )
         return true;
   return false;
}

int BrokenMask( int i )
{
   int k = 0;
   for( int j = 0; j<N; ++j )
      if( A[i][j] )
         k |= (1<<j);
   return k;
}

int Count( int k )
{
   int res = 0;
   for( ; k; k/=2 )
      if( k&1 )
         ++res;
   return res;
}

int Work()
{
   B[0][0] = 0;
   for( int i = 0; i<M; ++i )
   {
      for( int j = 0; j<(1<<N); ++j )
      {
         if( B[i][j]<0 )
            continue;
         for( int k = 0; k<(1<<N); ++k )
         {
            if( IsBroken( i, k ) )
               continue;
            if( IsBeat( j, k ) )
               continue;
            int s = k;
            B[i+1][s] = std::max( B[i+1][s], B[i][j]+Count( k ) );
         }
      }
   }
   int res = 0;
   for( int i = 0; i<(1<<N); ++i )
   {
      //std::cout << B[M][i] << ' ';
      res = std::max( res, B[M][i] );
   }
   //std::cout << std::endl;
   return res;
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

