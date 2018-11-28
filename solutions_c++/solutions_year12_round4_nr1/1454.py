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
#define MAX 10005
int n, k;
int d[ MAX ] , l[ MAX ];
//int dp[ MAX ][ MAX ];

//int dp[ MAX ];

map< int , map< int , bool > > dp;
bool end;

bool solve( int len , int last ){
    if( end ) return 1;
    if( d[ last ] + len  >= k ){ end = 1; return 1;}
    //if( len >= n ) return 0;
    //if( l[ last ] + d[ last ] - 1 >= k ){ end = 1; return 1;}
    //if( dp[ len ][ last ] != -1 ) return dp[ len ][ last ];

    //if( dp[ last ] != -1 ) return dp[ last ];

    if( dp.find( len ) != dp.end() ) {
        if( dp[ len ].find( last ) != dp[ len ].end() )
        return dp[ len ][ last ];
    }
    //cout<<len<<" "<<last<<endl;
    bool b = false, bb = false;
   // for( int i = 0 ; i < n ; ++i ){
    for( int i = last + 1 ; i < n ; ++i ){
        if( d[ i ] <= d[ last ] + len )
        //if( i != last && ( d[ i ] <= d[ last ] + len  && d[ i ] >= ( d[ last ] - len  ) ) )//d[ last ] + l[ last ] - 1 )
        {
            bb = true;
            /*
            int val = abs( d[ i ] - d[ last ] );
            if( val >= l[ i ] ){
                val = l[ i ] - 1;
            }
            b |= solve( val , i );*/
            b |= solve( min( abs( d[ i ] - d[ last ] ) , l[ i ] ) , i );
            //if( end ) return 1;
        }
    }
    //dp[ last ] = b;
    //if( !bb ) return 0;
    //return b;
    //return dp[ last ] = b;
    return dp[ len ][ last ] = b;
}
int main(){

    int t;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );
    //cout<<t<<endl;
    for( int q = 1 ; q <= t ; ++q ){
        scanf("%d" , &n );
        //cout<<q<<endl;
        for( int i = 0 ; i < n ; ++i ){
            scanf("%d %d" , &d[ i ] , &l[ i ] );
            //d[ i ] = i + 1; l[ i ] = i + 5;
        }
        scanf("%d" , &k );
        printf("Case #%d: " , q  );
        //memset( dp , -1 , sizeof( dp ) );
        dp.clear();
        end = false;
        if( solve( d[ 0 ] , 0 ) ) puts("YES");
        else puts("NO");
    }
    return 0;
}
