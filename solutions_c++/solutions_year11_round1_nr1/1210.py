#include<iostream>
#include<fstream>
using namespace std;

int gcd(int a , int b) {
   while((a %= b) && (b %= a)) ;
   return a | b ;
}

int main(int argc , char * argv[]) {
   ifstream fi (argv[1]) ;
   ofstream fo (argv[2]) ;

   int T ;

   int a[] = {
      100 , 50 , 25 , 20 , 10 , 5 , 4 , 2 , 1
   } ;
   int b[] = {
      1 , 2 , 4 , 5 , 10 , 20 , 25 , 50 , 100
   } ;

   int size = sizeof(a) / sizeof(int) ;
   fi >> T ;

   for (int t = 1 ; t <= T ; ++ t) {
      bool flag = false ;
      int Pd , Pg ;
      long long N ;
      fi >> N >> Pd >> Pg ;

      int g = gcd(Pg , 100) ;
      if (Pg == 100 || Pg == 0) {
         if (Pg == Pd) {
            flag = true ;
            goto RESULT ;
         } else {
            flag = false ;
            goto RESULT ;
         }
      }

      for (int i = 0 ; i < size ; ++ i) {
         if (Pd % a[i] == 0 && b[i] <= N) {
            int x = Pd / a[i] ;
            int y = 100 * x - Pg * b[i] ;

            int lcm = y * g / gcd(y , g) ;
            if (y == 0 || (lcm / y) * b[i] <= N) {
               if (Pg != 100 || lcm >= 0) {
                  flag = true ;
                  goto RESULT ;
               }
            }
         }

         /*
            r * x + k     Pg
            --------- = ------
            r * b + K     100

            r * (100 * x - Pg * b) == Pg * K - 100 * k
         */
      }
RESULT:
      fo << "Case #" << t << ": " << (flag ? "Possible" : "Broken") << endl ;
   }
   return 0;
}

