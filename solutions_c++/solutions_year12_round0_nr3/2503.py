#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <numeric>
#include <utility>
#include <deque>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <queue>
#include <limits>
#include <fstream>
#include <list>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

map< int , map< int , bool > > seen;

int toInt( string str ){ int n; istringstream buffer(str); buffer>>n; return n; }
string toStr( int  n){ string s; ostringstream buffer; buffer<<n; s = buffer.str(); return s; }
vector<int> dp[ 2000005 ];

int main(){


    int t , a , b , len , n2 , ans ;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

    a = 1; b = 2000000;
    string bb = toStr( b );
    len = bb.length();
    ans = 0;

    for( int i = a ; i <= b ; ++i ){
        string s = toStr( i ) ,s2 = s ;
        while( 1 ){
            rotate( s2.begin() , s2.begin() + 1 , s2.end() );
            if( s2 == s ) break;
            if( s2[ 0 ] == '0' ) continue;
            n2 = toInt( s2 );
            if( n2 > i && n2 <= b  && !seen[ i ][ n2 ] ){
                dp[ i ].push_back( n2 );
                seen[ i ][ n2 ] = 1;
            }
        }
        sort( dp[ i ].begin() , dp[ i ].end() );
    }

    scanf("%d" , &t );
    for( int q = 1 ; q <= t ; ++q ){
        scanf("%d %d" , &a , &b );
        ans = 0;
        for( int i = a ; i <= b ; ++i ){
            int R = upper_bound( dp[ i ].begin() , dp[ i ].end() , b ) - dp[ i ].begin();
            ans += R;
        }
        printf("Case #%d: %d\n" , q , ans );
    }

    return 0;
}
