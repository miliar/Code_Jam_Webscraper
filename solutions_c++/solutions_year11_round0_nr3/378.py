#include <iostream>

using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   for( int i = 0 ; i < n_case ; i++ ){
      int n;
      cin >> n ;
      int num = 0;
      int m = 10000000;
      long long ans = 0;
      for( int j = 0 ; j < n ; j++ ){
         int tmp;
         cin >> tmp;
         num = num ^ tmp;
         ans += tmp;
         m = min( m, tmp );
      }
      cout << "Case #" << i+1 << ": " ;
      if( num == 0 ){
         cout << ans-m << endl;
      }
      else{
         cout << "NO"<<endl;
      }
   }
   return 0;
}
