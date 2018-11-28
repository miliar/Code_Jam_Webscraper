#include<iostream>
#include<fstream>
using namespace std;

int main(int argc , char * argv[]) {
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;
   int T ;
   fi >> T ;

   for (int t = 1 ; t <= T ; ++ t) {
      int min = 1<<30 , sum = 0 , now , N , bin = 0 ;
      fi >> N ;
      for (int n = 0 ; n < N ; ++ n) {
         fi >> now ;
         sum += now ;
         bin ^= now ;
         if (min > now) {
            min = now ;
         }
      }

      if (bin == 0) {
         fo << "Case #" << t << ": " << sum - min << endl ;
      } else {
         fo << "Case #" << t << ": NO" << endl ;
      }
   }
   return 0;
}

