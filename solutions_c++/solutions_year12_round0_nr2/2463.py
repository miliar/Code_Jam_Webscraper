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

struct Data{
    int a , b , c;
    Data( int aa , int bb , int cc ): a( aa ) , b( bb ) , c( cc ){}
};

vector< Data > surprising[ 35 ] , no_surprising[ 35 ];

//vector< int > P[ 15 ];
//All possible triples
void init(){
    bool seen[ 15 ][ 15 ][ 15 ];
    int ii , jj , kk;
    memset( seen , 0 , sizeof( seen ) );
    for( int i = 0 ; i <= 10 ; ++i ){
        for( int j = 0 ; j <= 10 ; ++j ){
            if( abs( i - j ) > 2 ) continue;
            for( int k = 0 ; k <= 10 ; ++k ){
                ii = i; jj = j; kk = k;
                if( i > j ) swap( i , j );
                if( i > k ) swap( i , k );
                if( j > k ) swap( j , k );
                if( abs( i - k ) > 2 || abs( j - k ) > 2 || seen[ i ][ j ][ k ] ){
                    i = ii; j = jj; k = kk;
                    continue;
                }

                //surprising
                if( abs( i - j ) == 2 || abs( i - k ) == 2 || abs( j - k ) == 2 ){
                    surprising[ i + j + k ].push_back( Data( i , j , k ) );
                }
                else{
                    no_surprising[ i + j + k ].push_back( Data( i , j , k ) );
                }

                //P[ k ].push_back( i + j + k );

                //cout<< i + j + k <<" : "<<i<<" "<<j<<" "<<k<<endl;
                seen[ i ][ j ][ k ] = 1;
                i = ii;
                j = jj;
                k = kk;
            }
        }
    }
}

int a[ 105 ];


bool seen[ 105 ];
int main(){
    init();
    /*for( int i = 0 ; i <= 30 ; ++i ){
        cout<<i<<" "<<"surp "<<surprising[ i ].size()<<" no s "<<no_surprising[ i ].size()<<endl;
    }*/
    int t , n , S , p , len , x , ans;
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    scanf("%d" , &t );

    for( int q = 1 ; q <= t ; ++q ){
        ans = 0;
        scanf("%d %d %d" , &n , &S , &p );
        len = 0;
        memset( seen , 0 , sizeof( seen ) );
        for( int i = 0 ; i < n ; ++i ){
            scanf("%d" , &x );
            if( x <= 1 || x >= 29 ){
                if( no_surprising[ x ][ 0 ].c >= p ) ans++;
            }
            else{
                a[ len++ ] = x;
            }
        }

        n = len;
        for( int i = 0 ; i < n ; ++i ){
            if( S > 0 && surprising[ a[ i ] ][ 0 ].c >= p && no_surprising[ a[ i ] ][ 0 ].c < p ){
                S--; ans++; seen[ i ] = 1;
            }
        }

        for( int i = 0 ; i < n ; ++i ){
            if( !seen[ i ] && surprising[ a[ i ] ][ 0 ].c >= p && no_surprising[ a[ i ] ][ 0 ].c >= p ){
                if( S > 0 ) S--;
                ans++;
                seen[ i ] = 1;
            }
        }

        for( int i = 0 ; i < n ; ++i ){
            if( !seen[ i ] && no_surprising[ a[ i ] ][ 0 ].c >= p ){
                ans++;
            }
        }
        printf("Case #%d: %d\n" , q , ans );
    }
    return 0;
}
