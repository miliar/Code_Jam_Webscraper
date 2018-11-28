#include <cstdio>
#include <cmath>
using namespace std;
const int MAXN = 500;
const double EPS = 1e-7;

int P[MAXN][3], V[MAXN][3];

double sqr( double x ) { return x * x; }

double calc_dist( double t, int n )
{
  double pos[3] = { 0, 0, 0 };
  for( int i = 0; i < n; ++i ) 
    for( int j = 0; j < 3; ++j )
      pos[j] += P[i][j] + V[i][j] * t;
  
  return sqrt( sqr( pos[0] / n ) + sqr( pos[1] / n ) + sqr( pos[2] / n ) );
}

int main()
{
  int t; scanf( "%d", &t );
  for( int t_case = 0; t_case < t; ++t_case ) {
    int n; scanf( "%d", &n );
    double sP[3] = { 0 }, sV[3] = { 0 };
    for( int i = 0; i < n; ++i ) {
      for( int j = 0; j < 3; ++j ) {
	scanf( "%d", &P[i][j] );
	sP[j] += P[i][j];
      }
      for( int j = 0; j < 3; ++j ) {
	scanf( "%d", &V[i][j] );
	sV[j] += V[i][j];
      }
    }
    
    double sol;
    if ( fabs( sqr( sV[0] ) + sqr( sV[1] ) + sqr( sV[2] ) ) > 1e-7 )
      sol = -( sV[0] * sP[0] + sV[1] * sP[1] + sV[2] * sP[2] ) / ( sqr( sV[0] ) + sqr( sV[1] ) + sqr( sV[2] ) );
    else
      sol = 0;
    if ( sol < 0 ) sol = 0;

    printf( "Case #%d: %lf %lf\n", t_case + 1, calc_dist( sol, n ), sol );
  }
  return 0;
}
