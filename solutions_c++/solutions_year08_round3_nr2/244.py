#include <iostream>
#include <algorithm>

const int MAX = 50;

int S[MAX], N;

void ReadData()
{
   char tmp[MAX];
   std::cin >> tmp;
   N = 0;
   for( const char *p = tmp; *p; ++p, ++N )
      S[N] = (*p-'0');
}

int Pow3( int k )
{
   int res = 1;
   for( int i = 0; i<k; ++i )
      res *= 3;
   return res;
}

int Sign( int k )
{
   return k==1 ? 1 : -1;
}

long long Calc( int a, int b, const int *sg )
{
   int i;
   long long t = S[a];
   for( i = a; i<b; ++i )
   {
      if( sg[i]!=0 )
         return t+Calc( i+1, b, sg )*Sign( sg[i] );
      t *= 10;
      t += S[i+1];
   }
   return t;
}

bool Check( int t )
{
   int r[MAX];
   for( int i = 0; i<N-1; ++i )
   {
      r[i] = t%3;
      t /= 3;
   }
   long long p = Calc( 0, N-1, r );
   if( p%2==0 || p%3==0 || p%5==0 || p%7==0 )
      return true;
   return false;
}

int Work()
{
   int res = 0;
   int p = Pow3( N-1 );
   for( int i = 0; i<p; ++i )
      if( Check( i ) )
         ++res;
   return res;
}

void Output( int t, int res )
{
   std::cout << "Case #" << t << ": " << res << std::endl;
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
