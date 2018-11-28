#include <iostream>
#include <set>
#include <string>
#include <map>
using namespace std;

int main( void ) {

 int test; cin >> test;

 for( int cs = 1; cs <= test; ++cs ) {

     string n; cin >> n;

     set<char> U;
     for( int i = 0; i < (int)n.size(); ++i ) U.insert( n[i] );

     set<int> dig;
     for( int i = 0; i < (int)U.size(); ++i ) dig.insert( i );

     map<char, int> val;
     val[ n[0] ] = 1;
     dig.erase(1);

     for( int i = 0; i < (int)n.size(); ++i )
        if( val.count(n[i]) == 0 ) {
            val[n[i]] = *dig.begin();
            dig.erase( dig.begin() );
        }

    //for( map<char, int> :: iterator it = val.begin(); it != val.end(); ++it )
    //    cout << it->first << " " << it->second << endl;

     long long sol = 0;
     int base = U.size();
     if( base < 2 ) base = 2;

     for( int i = 0; i < (int)n.size(); ++i )
        sol = sol * base + val[n[i]];

     cout << "Case #" << cs << ": " << sol << endl;

 }

 return 0;
}
