#include <iostream>

using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   for( int i = 0 ; i < n_case ; i++ ){
      int n;
      cin >> n ;
      int num = 0;
      int count = 1;
      for( int j = 0 ; j < n ; j++ ){
         int tmp;
         cin >> tmp;
         if( count != tmp ) num++;
         count ++;
      }
      double ans = (double) num;
      cout << "Case #" << i+1 << ": " ;
      cout.setf(ios::fixed, ios::floatfield);
      cout.precision(6);
      cout << ans <<endl;
   }
   return 0;
}
