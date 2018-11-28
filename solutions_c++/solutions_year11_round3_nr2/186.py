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
      long long L,t,N,C;
      cin >> L >> t >> N >> C;
      vector<int> as;
      for(int i = 0 ; i < C ; i++ ){
         int tmp;
         cin >> tmp;
         as.push_back(tmp);
      }
      vector< long long > vec;
      long long ans = 0;
      long long rest = t/2;
      for( int i = 0 ; i < N ; i++ ){
         int curdist = as[i%C];
         ans += curdist;
         if( rest == 0 ){
            vec.push_back( curdist );
         }
         else if( curdist-rest > 0 ){
            vec.push_back(curdist-rest);
            rest = 0;
         }
         else rest -= curdist;
      }
      sort(vec.begin(), vec.end() , greater<long long>() );
      long long quickdist = 0;
      for( int i = 0 ; i < min(L,(long long)vec.size()) ; i++ ){
        quickdist += vec[i]; 
      }
      cout << "Case #" << loop+1 << ": " << (2*ans -quickdist)<< endl; 
      
   }
   return 0;
}
