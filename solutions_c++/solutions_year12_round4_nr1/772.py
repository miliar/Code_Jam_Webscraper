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
     int n_vine;
     cin >> n_vine;
     vector<pair<int,int> >data;
     for( int i = 0 ; i < n_vine; i++ ){
      int d,l;
      cin >> d>>l;
      data.push_back( make_pair( d, l ) );
     }
     int D;
     cin >> D;
     sort( data.begin(), data.end() );
     int dp[10001];
     memset( dp , -1 , sizeof(dp) );
     dp[0] = data[0].first;
     bool flag = false;
     for( int i = 0 ; i < n_vine; i++ ){
       int position = data[i].first;
       int length = dp[i];
       int reachable = position + length;
       //cout << position << "," << length << " , " << reachable << endl;
       if( reachable >= D ) {flag=true;break;}
       for( int j = i+1 ; j < n_vine; j++ ){
        if( data[j].first > reachable ) break;
        else{
          dp[j] = max( dp[j], min( data[j].second, data[j].first-position ) );
        }
      }
     }
     if( !flag ){
       cout << "Case #" << loop+1 << ": " <<"NO"<< endl;
     }
     else{
       cout << "Case #" << loop+1 << ": " <<"YES"<< endl;
     }
   }
   return 0;
}
