#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <set>
#include <map>
using namespace std;

map< string , bool > here;
string str;
char inp[ 99 ];
int L;
pair< double , string > node[ 9000 ];
int edge[ 9000 ][ 2 ];
int nnode = 0;
int A , T;
/*
(0.5 cool
  ( 1.000)
  (0.5 ))
*/

pair< int , int > build( int i )
{
    int gogo = nnode;
    pair< int , int > res;
    int end;
    while( str[ i ] != '(' )i ++;
    i ++;
    string numer = "";
    /// getting number
    
    while( !isdigit ( str[ i ] ) )i ++;
    
    while( isdigit( str[ i ] ) || str[ i ] == '.' )
    {
        numer += str[ i ];
        i ++;
    }
    sscanf( numer.c_str() , "%lf" ,&node[ nnode ].first );
    /// getting string
    while( !isalpha( str[ i ] ) )
    {
        if( str[ i ] == ')' )
        {
            edge[ nnode ][ 0 ] = -1;
            nnode ++;
            end = i;
            goto endy;
        }
        i ++;
    }
    numer = "";
    while( isalpha( str[ i ] ) )
    {
       numer += str[ i ];
       i ++; 
    }
    
    node[ nnode ].second = numer;
    nnode ++;
    
    
    res = build( i );
    end = res.first;
    edge[ gogo ][ 0 ] = res.second;
    res = build( end + 1 );
    end = res.first;
    edge[ gogo ][ 1 ] = res.second;
    while( str[ end ] != ')' )
        end ++;
    
    endy:;
    return make_pair( end , gogo );
}

double rec( int ind )
{
    if( edge[ ind ][ 0 ] == -1 )return node[ ind ].first;
    double ret = node[ ind ].first;
    if( here[ node[ ind ].second ] )
        ret *= rec( edge[ ind ][ 0 ] );
    else 
        ret *= rec( edge[ ind ][ 1 ] );
    return ret;
}

int main()
{
    freopen( "F.out" , "w" , stdout );
    FILE *in = fopen( "A-large.in" , "r" );
    fscanf( in , "%d\n" ,&T );
    for( int TT = 1 ; TT <= T ; TT++ )
    {
        printf( "Case #%d:\n" ,TT );
        str = "";
        fscanf( in , "%d\n" ,&L );
        for( int c = 0 ; c < L ; c++ )
        {
            char ch;
            fscanf( in , "%c" ,&ch );
            while( ch != '\n' )
            {
                str += ch;
                fscanf( in , "%c" ,&ch );
            }
        }
        memset( edge , -1 , sizeof edge );
        nnode = 0;
        build( 0 );
        
        fscanf( in , "%d\n" ,&A );
        for( int c = 0 ; c < A ; c++ )
        {
            fscanf( in , "%s" ,inp );
            int F;
            fscanf( in , "%d" ,&F );
            here.clear();
            for( int c1 = 0 ; c1 < F ; c1++ )
            {
                fscanf( in , "%s" ,inp );
                here[ string( inp ) ] = 1;
            }
            double ret = rec( 0 );
            printf( "%lf\n" ,ret );
        }
        
    }
    return 0;
}
