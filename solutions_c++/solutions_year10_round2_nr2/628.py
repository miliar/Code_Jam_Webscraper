#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 100;

struct Chi
{
       __int64 xi;
       __int64 vi;
       int iS;
       bool bR;
};

__int64 B;
int N, K, T;
Chi chis[MAXN];

bool cmp( Chi a, Chi b )
{
     if( a.iS < b.iS )
     {
         return true;
     }
     else
     {
         return false;
     }
}

int main()
{
    freopen( "B-large.in", "r", stdin );
	freopen( "B-large.txt", "w", stdout );
    int cas;
    scanf( "%d", &cas );
    for( int iCas = 1; iCas <= cas; ++iCas )
    {
         scanf( "%d%d%I64d%d", &N, &K, &B, &T );
         int i, j;
         memset( chis, 0, sizeof( chis ) );
         for( i = 1; i <= N; ++i )
         {
              scanf( "%I64d", &chis[i].xi );
         }
         for( i = 1; i <= N; ++i )
         {
              scanf( "%I64d", &chis[i].vi );
         }
         for( i = N; i > 0; --i )
         {
			 if( chis[i].vi*T + chis[i].xi >= B )
              {
                  chis[i].bR = true;
                  for( j = i+1; j <= N; ++j )
                  {
                       if( !chis[j].bR )
                       {
                           ++chis[i].iS;
                       }
					   else if( chis[i].vi > chis[j].vi && 
						   (chis[j].xi - chis[i].xi)+chis[i].xi*(chis[i].vi - chis[j].vi) <= B*(chis[j].xi - chis[i].xi ) )
                       {
                           chis[i].iS += chis[j].iS;
						   break;
                       }
                  }
              }
         }
         i = 1;
         for( j = 1; j <= N; ++j )
         {
              if( chis[j].bR )
              {
                  chis[i++] = chis[j];
              }
         }
         N = i-1;
         printf( "Case #%d: ", iCas );
         if( N < K )
         {
             printf( "IMPOSSIBLE\n" );
         }
         else
         {
             sort( chis+1, chis+1+N, cmp );
             int nS = 0;
             for( i = 1; i <= K; ++i )
             {
                  nS += chis[i].iS;
             }
             printf( "%d\n", nS );
         }
               
    }
    scanf( "%d", &cas );
    return 0;   
}
