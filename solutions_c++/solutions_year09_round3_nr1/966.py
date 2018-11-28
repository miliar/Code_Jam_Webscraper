#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <sstream>
using namespace std;
string poss = "0123456789abcdefghijklmnopqrstuvwxyz";
long long LIM = 1LL<<61;
int main ()
{
    //cout << LIM <<"\n"; 
    //cout << poss.size() <<"\n";
    int T ,kase = 0; cin >> T;
    while ( T-- )
    {
          
          string in ; 
          cin >> in ;
          int i ,j,k;
          long long ans = LIM;
          map < char , bool > used ,found;
          map < char , long long  > val; 
          found.clear();
          for ( i = 0 , j = 0; i < in.size() ;i++ ) if ( !found [ in [i] ]) found [ in [i] ]= true , j++;
         // cout << j << "\n";
          for ( int base = max ( j, 2 ) ; base <= 36 ; base++ )
          {
              used.clear();found.clear();
              val.clear();
              used [ '1' ] = true ; val [ in [0] ] = 1LL; found [ in [0] ] = true;
              //cout <<"yes\n";
              //cout << base << "\n";
              for ( j = 1; j < in.size() ;j++ )
              {
                  if ( !found [ in [j] ] ) 
                  {
                       for ( k = 0 ; k < poss.size() ;k++ ) if ( !used [ poss [k] ] ) break;
                       found [ in [j] ] = true;used [ poss [k] ] = true;
                       val [ in [j] ] = (long long )k ;
                  }
              }
             // cout << base <<"\n";
              long long tmp = 0 , B = 1;
              for ( j = in.size() -1 ; j >= 0 ;j-- )
              {
                  tmp += B*val [ in [j] ];
                  //if ( base == 2) cout << tmp << " "<<B <<" "<<val [ in [j] ]<<"\n";
                  B *= (long long )base;
                  if ( B > LIM   || B < 0) break;
              }
             // cout << B << " "<< " " << tmp <<" "<<j << "\n";
            // if ( tmp == 2 ) cout << base << "\n";
              if ( j < 0 )
              ans = min ( ans , tmp );
          }
          cout <<"Case #"<<++kase<<": ";
          cout << ans << "\n";
    }
    return 0;
}
                  
                  
