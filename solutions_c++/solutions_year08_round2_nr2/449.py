#include  <iostream>
#include <algorithm>

const int MAX = 1001;

int A, B, P;
int S[MAX],  D[MAX];

void Eratosphen()
{
   for( int i = 2; i<MAX; ++i )
      if( D[i]==0 )
         for( int j = 2*i; j<MAX; j += i )
            D[j] = 1;
}

void Merge( int a, int b )
{
   for( int i = A; i<=B; ++i )
      if( S[i]==a )
         S[i] = b;
}

void ReadData()
{
   std::cin >> A >> B >> P;
   for( int i = A; i<=B; ++i )
      S[i] = i;
}

bool Has( int a, int b )
{
   for( int i = P; i<=std::min( a, b ); ++i )
      if( D[i]==0 && a%i==0 && b%i==0 )
         return true;
      return false;
}

int Work()
{
   bool f = true;
   for( ; f; )
   {
      f = false;
      for( int i = A; i<=B; ++i )
         for( int j = i+1; j<=B; ++j )
            if( S[i]!=S[j] && Has( i, j ) )
            {
               f = true;
               Merge( S[i], S[j] );
            }
   }
   int res  = 0;
   for( int i = A; i<=B; ++i )
   {
      if( S[i] )
      {
         ++res;
         Merge( S[i], 0 );
      }
   }
   return res;
}

void Output( int t, int res )
{
   std::cout << "Case #" << t << ": " << res << std::endl;
}

int main()
{
   Eratosphen();
   int t;
   std::cin >> t;
   for( int i = 1; i<=t; ++i )
   {
      ReadData();
      Output( i, Work() );
   }
   return 0;
}

