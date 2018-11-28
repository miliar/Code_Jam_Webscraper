#include<fstream>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(int argc , char * argv[]) {
   ifstream fi(argv[1]) ;
   ofstream fo(argv[2]) ;

   int T ;
   fi >> T ;
   for (int t = 1 ; t <= T ; ++ t) {
      int C , total = 0 , mid , D;
      fi >> C >> D ;
      vector<int> P(C) ;
      vector<int> V(C) ;
      vector<int> array ;
      vector<int> delta ;
      for (int i = 0 ; i < C ; ++ i) {
         fi >> P[i] >> V[i] ;
         total += V[i] ;
         array.insert(array.end() , V[i] , P[i]) ;
      }

      sort(array.begin() , array.end()) ;

      delta.reserve(array.size()) ;

      //cout << D << ": " ;

      int next = 0 ;

      for (int i = 0 , sz = array.size() ; i < sz ; ++ i) {
         delta[i] = next - array[i] + array[0];
         if (delta[i] < 0) {
            next = array[i] - array[0] ;
            delta[i] = 0 ;
         }
         next += D ;
         //cout << delta[i] << ' ' ;
      }
      //cout << endl ;

      int max , min ;
      max = min = delta[0] ;

      for (int i = 0 , sz = array.size() ; i < sz ; ++ i) {
         if (max < delta[i]) max = delta[i] ;
         if (min > delta[i]) min = delta[i] ;
      }

      fo << "Case #" << t << ": " << max - 1. * (max + min) / 2 << endl ;

      // int tmp ;
      // cin >> tmp ;
   }
   return 0;
}

