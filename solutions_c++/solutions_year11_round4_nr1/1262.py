#include<iostream>
#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;

class Corr {
   public:
   double L ;
   double w ;
   bool operator<(const Corr&x) const {
      return w < x.w ;
   }
} c[1000] ;

int main(int argc , char * argv[]) {
   int T ;
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;

   fi >> T ;
   for (int _t = 1 ; _t <= T ; ++ _t) {
      int X , S , R , t , N , v ;
      fi >> X >> S >> R >> t >> N ;
      for (int i = 0 ; i < N ; ++ i) {
         int B , E , w ;
         fi >> B >> E >> w ;
         c[i].L = E - B ;
         c[i].w = w ;
         X -= (E - B) ;
      }

      sort(c , c + N) ;
      double left = t , total = 0 ;
      double run = 1. * X / R ;
      if (left > run) {
         left -= run ;
         total += run ;
      } else {
         total += left + 1.*(X - left * R)/(S) ;
         left = 0 ;
      }

      for (v = 0 ; v < N ; ++ v) {
         double x = 1. * (c[v].L) / (c[v].w + R) ;
         if (left > x) {
            left -= x ;
            total += x ;
         } else if (left > 0) {
            total += left + 1.*(c[v].L - left * (c[v].w + R))/(c[v].w + S) ;
            left = 0 ;
         } else {
            total += 1.*(c[v].L) /(c[v].w + S) ;
         }
      }

      fo << "Case #" << _t << ": " << fixed << setprecision(6) << total << endl ;
   }
   return 0;
}

