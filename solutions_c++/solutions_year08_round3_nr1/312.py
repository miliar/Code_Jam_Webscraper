#include <iostream>
#include <algorithm>

const int MAX = 1000;

int P, K, L, F[MAX];

void ReadData()
{
   std::cin >> P >> K >> L;
   for( int i = 0; i<L; ++i )
      std::cin >> F[i];
}

long long Work()
{
   if( P*K<L )
      return -1;
   std::sort( F, F+L );
   long long res = 0;
   int m = 0;
   for( int i = 0; i<L; ++i )
   {
      if( i%K==0 )
         ++m;
      res += static_cast<long long>( F[L-1-i] )*m;
   }
   return res;
}

void Output( int t, long long res )
{
   std::cout << "Case #" << t << ": ";
   if( res==-1 )
      std::cout << "Impossible";
   else
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
