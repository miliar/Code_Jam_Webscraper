#include <stdio.h>
#include <sstream>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

typedef long long int64;

int isgd[ 90000 ][ 11 ];

string add( string x , string y , int b )
{
    
    int siz = max( x.size() , y.size() ) + 2;
    x = string( siz - (int)x.size() , '0' ) + x;
    y = string( siz - (int)y.size() , '0' ) + y;
    int rem = 0;
    string ret = "";
    for( int c = siz - 1 ; c >= 0 ; c-- )
    {
        rem += x[ c ] + y[ c ] - '0' - '0';
        ret = char( '0' + rem % b ) + ret;
        rem /= b;
    }  
    while( ret[ 0 ] == '0' && ret.size() > 1 )ret = ret.substr( 1 );
    return ret;
}
string mul( string x , int b )
{
    string ret = x;
    int e = x[ 0 ] - '0';
    for( int c = 1 ; c < e ; c++ )
        ret = add( ret , x , b );
    return ret;
}
string doit( string x , int b )
{
    string ret = "";
    for( int c = 0 ; c < x.size() ; c++ )
    {
        string tmp = "";
        int d = x[ c ] - '0';
        string sd = ""; 
        sd += char( '0' + d );
        tmp = mul( sd , b );
        
        ret = add( ret , tmp , b );
        
    }
    return ret;
}

string tob( int x , int b )
{
    string ret = "";
    while( x )
    {
        ret = char( '0' + x % b ) + ret;
        x /= b;
    }
    return ret;
}
int tot( string x , int b )
{
    int ret = 0 , p = 1;
    for( int c = x.size() - 1 ; c >= 0 ; c-- )
    {
        ret += p * ( x[ c ] - '0' );
        p *= b;
    }
    return ret;
}

bool good( int x , int b )
{
    if( x == 1 )return 1;
    if( x < 90000 && isgd[ x ][ b ] != -1 )return isgd[ x ][ b ];
    
    string num = tob( x , b );
    num = doit( num , b );
    
    int ret = tot( num , b );
    
    if( x >= 90000 )return good( ret , b );
    
    isgd[ x ][ b ] = 0;
    return isgd[ x ][ b ] = good( ret , b );
    /// getting it to base 10
}
int T;

int main()
{
    freopen( "F.out" , "w" , stdout );
    
    memset( isgd , -1 , sizeof isgd );
    freopen( "A-small.in" , "r" , stdin );
    scanf( "%d\n" ,&T );
    for( int cc = 0 ; cc < T ; cc++ )
    {
        int arr[ 11 ]; 
        int carr = 0;
        stringstream is;
        string inp = "";
        char ch;
        scanf( "%c" ,&ch );
        while( ch != '\n' )
        {
            inp += ch;
            scanf( "%c" ,&ch );
        }
        is << inp;
        int k;
        while( is >> k )
        {
            arr[ carr ++ ] = k;
        } 
        int ret;
        for( int c = 2 ; 1 ; c++ )
        {
            bool g = 1;
            for( int d = 0 ; d < carr ; d++ )
                if( !good( c , arr[ d ] ) )
                {
                    g = 0;
                    break;
                }
            if( g )
            {
                ret = c;
                break;
            }
        }
        printf( "Case #%d: %d\n" , cc + 1 , ret );
    }
    return 0;
}
