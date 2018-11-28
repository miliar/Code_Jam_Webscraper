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
      int n , m;
      cin >> n >> m;
      vector<string> val;
      for( int i = 0 ; i < n ; i++ ){
         string line;
         cin >> line;
         val.push_back(line);
      }
      bool flag = true;
      for( int i = 0 ; i < n ; i++ ){
         for( int j = 0; j < m ; j++ ){
            if( val[i][j] == '#' ){
               if( i == n-1 || j == m-1 ){
                  flag = false;
                  break;
               }
               if( val[i][j+1] != '#' || val[i+1][j] != '#' || val[i+1][j+1] != '#' ){
                  flag = false;
                  break;
               }
               val[i][j] = '/';
               val[i][j+1] = '\\';
               val[i+1][j] = '\\';
               val[i+1][j+1] = '/';
            }
         }
         if( !flag ){
            break;
         }
      }
      cout << "Case #" << loop+1 << ": " << endl;
      if( !flag ){
         cout << "Impossible" << endl;
      }
      else{
         for( int i = 0 ; i < n ; i++ ){
           cout << val[i] << endl;
         }
      }
   }
   return 0;
}
