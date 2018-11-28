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
int main ()
{
    int T ,kase = 0;cin >> T;
    string in;
    while ( T-- )
    {
          cin >> in;
          string tmp  = in;
          cout << "Case #"<<++kase<<": ";
          next_permutation ( in.begin() , in.end() );
         // while( in [0] == '0' ) next_permutation ( in.begin() , in.end() );
         int i = 0;
         while ( in [i] == '0' ) i++;
         swap ( in [i] , in [0] );
          if ( tmp >= in ) 
          {
               //int i ;
               cout << in [0] << 0;
               for ( i = 1 ; i < in.size() ;i++ ) cout << in [i]; 
          }
          else cout << in ;
          cout << "\n";
    }
    return 0;
}
