#include <iostream>
#include <algorithm>

const int MAX = 10000;
const int INF = 1000000;

int M, V, G[MAX], C[MAX], Z[MAX], E[MAX];

void ReadData()
{
   std::cin >> M >> V;
   for( int i = 0; i<(M-1)/2; ++i )
      std::cin >> G[i] >> C[i];
   for( int i = 0; i<(M+1)/2; ++i )
   {
      int k = (M-1)/2+i;
      std::cin >> G[k];
      C[k] = 0;
      Z[k] = (G[k]==0 ? 0 : INF);
      E[k] = (G[k]==1 ? 0 : INF);
   }
}

int Work()
{
   for( int i = (M-1)/2-1; i>=0; --i )
   {
      if( !C[i] )
      {
         if( G[i] )
         {
            int l = 2*i+1, r = 2*i+2;
            if( E[l]!=INF && E[r]!=INF )
               E[i] = E[l]+E[r];
            else
               E[i] = INF;
            if( Z[l]!=INF || Z[r]!=INF )
               Z[i] = std::min( Z[l], Z[r] );
            else
               Z[i] = INF;
         }
         else
         {
            int l = 2*i+1, r = 2*i+2;
            if( E[l]!=INF || E[r]!=INF )
               E[i] = std::min( E[l], E[r] );
            else
               E[i] = INF;
            if( Z[l]!=INF && Z[r]!=INF )
               Z[i] = Z[l]+Z[r];
            else
               Z[i] = INF;
         }
      }
      else
      {
         if( G[i] )
         {
            int l = 2*i+1, r = 2*i+2;
            if( E[l]!=INF )
               E[i] = std::min( E[l]+E[r], E[l]+Z[r]+1 );
            else if( E[r]!=INF )
               E[i] = std::min( E[l]+E[r], E[r]+Z[l]+1 );
            else
               E[i] = INF;
            if( Z[l]!=INF || Z[r]!=INF )
               Z[i]  = std::min( Z[l], Z[r] );
            else
               Z[i] = INF;
         }
         else
         {
            int l = 2*i+1, r = 2*i+2;
            if( Z[l]!=INF )
               Z[i] = std::min( Z[l]+Z[r], Z[l]+E[r]+1 );
            else if( Z[r]!=INF )
               Z[i] = std::min( Z[l]+Z[r],  Z[r]+E[l]+1 );
            else
               Z[i] = INF;
            if( E[l]!=INF || E[r]!=INF )
               E[i] = std::min( E[l], E[r] );
            else
               E[i] = INF;
         }
      }
   }
   /*for( int i = 0; i<M; ++i )
      std::cout << E[i] << ' ';
   std::cout << std::endl;
   for( int i = 0; i<M; ++i )
      std::cout << Z[i] << ' ';
   std::cout << std::endl;*/
   return V ? E[0] : Z[0];
}

void Output( int t, int res )
{
   std::cout << "Case #" << t << ": ";
   if( res!=INF )
      std::cout << res;
   else
      std::cout << "IMPOSSIBLE";
   std::cout << std::endl;
}

int main()
{
   int t;
   scanf( "%d", &t );
   for( int i = 1; i<=t; ++i )
   {
      ReadData();
      Output( i, Work() );
   }
   return 0;
}

