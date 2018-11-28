#include <ctime>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>

using namespace std;

const double pi = acos( -1.0 );

struct Job {
   double x1, y1, x2, y2;

   Job( double X1, double Y1, double X2, double Y2 ) {
      x1 = X1; y1 = Y1; x2 = X2; y2 = Y2;
   }
};

#define ITER_PER_TEST_CASE 600000000

int main( void ) {
   int T;
   scanf( "%d", &T );

   double ttt = clock();

   for( int tt = 1; tt <= T; ++tt ) {
      double fly, R, thickness, r, gap;
      scanf( "%lf%lf%lf%lf%lf", &fly, &R, &thickness, &r, &gap );

      double P = R * R * pi;
      double Pmiss = 0.0;

      vector<Job> jobs;
      double flyR = R - thickness - fly;
      double square_size = gap - 2*fly;

      if( flyR > 0 && square_size > 0 ) {
         for( int x = 0; x <= 512; ++x ) {
            for( int y = 0; y <= 512; ++y ) {
               double x1 = r + fly + x * (gap+2*r);
               double x2 = r + gap - fly + x * (gap+2*r);
               double y1 = r + fly + y * (gap+2*r);
               double y2 = r + gap - fly + y * (gap+2*r);

               int inside = 
                  (x1*x1 + y1*y1 <= flyR*flyR) + 
                  (x1*x1 + y2*y2 <= flyR*flyR) + 
                  (x2*x2 + y1*y1 <= flyR*flyR) + 
                  (x2*x2 + y2*y2 <= flyR*flyR);

               if( inside == 4 ) Pmiss += square_size*square_size;
               else if( inside > 0 ) jobs.push_back( Job( x1, y1, x2, y2 ) );
            }
         }
      } 

      if( jobs.size() ) {
         int sqrt_iter_per_job = 1;
         while( sqrt_iter_per_job * sqrt_iter_per_job * jobs.size() <= ITER_PER_TEST_CASE )
            ++sqrt_iter_per_job;

         double delta = 1.0 / (2.0*sqrt_iter_per_job) * square_size;
         
         for( vector<Job>::iterator it = jobs.begin(); it != jobs.end(); ++it ) {         
            int accepted = 0;
            for( double x = it->x1 + delta; x < it->x2; x += 2*delta )
               for( double y = it->y1 + delta; y < it->y2; y += 2*delta )
                  accepted += (x*x + y*y <= flyR*flyR);
            Pmiss += square_size * square_size * accepted / (sqrt_iter_per_job * sqrt_iter_per_job);
         }
      }

      double ret = 1 - 4 * Pmiss / P;
      if( ret < 0 ) ret = 0.0;
      printf( "Case #%d: %.10lf\n", tt, ret );
      fprintf( stderr, "Case #%d: %.10lf    %.3lf\n", tt, ret, (clock()-ttt) / CLOCKS_PER_SEC );
   }
   return 0;
}
