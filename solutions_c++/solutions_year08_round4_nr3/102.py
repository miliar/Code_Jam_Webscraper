#include  <cstdio>
#include <cmath>
#include <algorithm>

const int MAX = 1000;
const int DIV = 20;
const int SHIFT = 5;
const double INF = 1e30;
const double EPS = 1e-7;

int N;
int X[MAX], Y[MAX], Z[MAX], P[MAX];

void ReadData()
{
   scanf( "%d", &N );
   for( int i = 0; i<N; ++i )
      scanf( "%d %d %d %d", &X[i], &Y[i], &Z[i], &P[i] );
}

double MaxDist( double x, double y, double z )
{
   double res = 0;
   for( int i = 0; i<N; ++i )
      res = std::max( res, (fabs(x-X[i])+fabs(y-Y[i])+fabs(z-Z[i]))/P[i] );
   return res;
}

int Min( const int *a )
{
   int m = a[0];
   for( int i = 1; i<N; ++i )
      if( a[i]<m )
         m = a[i];
   return m;
}

int Max( const int *a )
{
   int m = a[0];
   for( int i = 1; i<N; ++i )
      if( a[i]>m )
         m = a[i];
   return m;
}

double Work()
{
   double ax = Min( X ), bx = Max( X );
   double ay = Min( Y ), by = Max( Y );
   double az = Min( Z ), bz = Max( Z );
   for( ; fabs( bx-ax )>EPS || fabs( by-ay )>EPS || fabs( bz-az )>EPS; )
   {
      double dx = (bx-ax)/DIV;
      double dy = (by-ay)/DIV;
      double dz = (bz-az)/DIV;
      double best = INF;
      int best_i = 0, best_j = 0, best_k = 0;
      for( int i = 1; i<DIV; ++i )
         for( int j = 1; j<DIV; ++j )
               for( int k = 1; k<DIV; ++k )
               {
                  double tx = ax+dx*i;
                  double ty = ay+dy*j;
                  double tz = az+dz*k;
                  double t = MaxDist( tx, ty, tz );
                  if( t<best )
                  {
                     best_i = i;
                     best_j = j;
                     best_k = k;
                     best = t;
                  }
               }
      ax = ax+dx*best_i-SHIFT*dx;
      bx = ax+2*SHIFT*dx;
      ay = ay+dy*best_j-SHIFT*dy;
      by = ay+2*SHIFT*dy;
      az = az+dz*best_k-SHIFT*dz;
      bz = az+2*SHIFT*dz;
   }
   //printf( "%lf %lf %lf\n", ax, ay, az );
   return MaxDist( ax, ay, az );
}

void Output( int t, double res )
{
   printf( "Case #%d: %.6lf\n", t, res );
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

