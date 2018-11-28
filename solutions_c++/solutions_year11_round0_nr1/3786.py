#include<iostream>
#include<map>
#include<vector>
#include<set>
#include<string>
#include<fstream>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    for( int i = 0; i < n; i++ ) {

         int x;
         cin >> x;
         
         vector < int > o, b;
         vector < int > tko;
         
         for( int j = 0; j < 2 * x; j += 2 ) {
         
              char c;
              int a;
              cin >> c >> a;
              
              if( c == 'O' ) {
                  o.push_back( a );
                  tko.push_back( 1 );    
              }
              else {
                   b.push_back( a );
                   tko.push_back( 0 );
              }
              
         }
         
         o.push_back( 1000 );
         b.push_back( 1000 );
         
         int rj = 0;
         
         int di1 = 1, di2 = 1;
         int k1 = 0, k2 = 0;
         
         for( int j = 0; j < tko.size(); j++ ) {
         
              while( 1 ) {
                     rj++;
                     if( tko[ j ] ) {
                     
                         if( di1 == o[ k1 ] ) {
                             k1++;
                             if( di2 < b[ k2 ] ) di2++;
                             if( di2 > b[ k2 ] ) di2--;
                             break;
                         }
                         if( di1 < o[ k1 ] ) di1++;
                         if( di1 > o[ k1 ] ) di1--;
                         if( di2 < b[ k2 ] ) di2++;
                         if( di2 > b[ k2 ] ) di2--;
                         
                     } else {
                     
                       if( di2 == b[ k2 ] ) {
                             k2++;
                             if( di1 < o[ k1 ] ) di1++;
                             if( di1 > o[ k1 ] ) di1--;
                             break;
                       }
                       if( di1 < o[ k1 ] ) di1++;
                       if( di1 > o[ k1 ] ) di1--;
                       if( di2 < b[ k2 ] ) di2++;
                       if( di2 > b[ k2 ] ) di2--;
                            
                     }
                     
                     
              }
              
         }
         
         cout << "Case #" << i+1 << ": " << rj << endl;
         
    }
    

    return 0;
}
