#include<iostream>
#include<fstream>
#include<iomanip>
#include<vector>
using namespace std;

int main(int argc , char * argv[]) {
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;

   int T ;
   fi >> T ;
   for (int t = 1 ; t <= T ; ++ t) {
      char table[105][105] ;

      int N ;
      fi >> N ;
      vector<int> win(N , 0) ;
      vector<int> total(N , 0) ;

      for (int n = 0 ; n < N ; ++ n) {
         fi >> table[n] ;
         total[n] = 0 ;

         for (int i = 0 ; i < N ; ++ i) {
            if (table[n][i] == '1') {
               total[n] ++ ;
               win[n] ++ ;
            } else if (table[n][i] == '0') {
               total[n] ++ ;
            }
         }
      }

      vector<double> OWP(N , 0.0) ;
      for (int i = 0 ; i < N ; ++ i) {
         int count = 0 ;
         for (int j = 0 ; j < N ; ++ j) {
            if (table[i][j] != '.') {
               if (table[i][j] == '1') {
                  OWP[i] += 1. * (win[j]) / (total[j] - 1) ;
               } else if (table[i][j] == '0') {
                  OWP[i] += 1. * (win[j] - 1) / (total[j] - 1);
               }
               count ++ ;
            }
         }
         OWP[i] /= count ;
         //cout << "OWP[" << i << "] = " << OWP[i] << endl ;
      }

      fo << "Case #" << t << ":" << endl ;
      for (int i = 0 ; i < N ; ++ i) {
         double rpi = 0.25 * win[i] / total[i] + 0.5 * OWP[i] ;
         double tmp = 0.0 , count = 0.0 ;
         for (int j = 0 ; j < N ; ++ j) {
            if (table[i][j] != '.') {
               tmp += OWP[j] ;
               count += 1 ;
            }
         }
         rpi += 0.25 * tmp / count ;
         fo << rpi << endl ; 
      }

   }
   return 0;
}

