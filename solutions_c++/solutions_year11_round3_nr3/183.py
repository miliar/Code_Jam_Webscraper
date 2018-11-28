#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;

int main(){
   int n_case;
   cin >> n_case;
   for( int loop = 0 ; loop < n_case ; loop++ ){
      int N,L,H;
      cin >> N >> L >> H;
      vector<int> vec;
      for( int i = 0 ; i < N ; i++ ){
         int tmp;
         cin >> tmp;
         vec.push_back(tmp);
      }
      int cand;
      for( cand = L ; cand <= H ; cand++ ){
         bool flag = true;
         for( int i = 0 ; i < N ; i++ ){
            if( max(vec[i],cand) % min(vec[i],cand) != 0 ){
               flag = false;
               break;
            }
         }
         if( flag ) break;
      }
      cout << "Case #" << loop+1 << ": " ;
      if( cand == H+1 ) cout << "NO" << endl;
      else cout << cand << endl;
   }
   return 0;
}
