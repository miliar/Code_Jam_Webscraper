#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <map>


int t, n;
char buffer[ 2000 ];
int number[ 10 ];

std::map< long long , long long > Was[ 11 ];

long long convert( long long num , int base )
{
    long long ret = 0;
    
    long long g = 1;
    while( g * base <= num ) g *= base;
    
    while( g > 0 )
    {
        long long z = num / g;
        ret += z * z;
        num %= g;
        g /= base;
    }
    
    return ret;
}

bool good( long long num , int base )
{
    if( num == 1 ) return true;
    std::map<long long,long long>::iterator it = Was[base].find( num );
    
    if( it != Was[base].end( ) )
    {
        if( it -> second == 1 ) return true;
        else return false;      
    }

    Was[base][num] = 0;
    bool ret=false;
    Was[base][num] = (ret=good( convert( num,base), base)) ? 1 : 2;
    return ret;
}

int main( )
{
    scanf( "%d\n", &t);
    for( int test = 1 ; test <= t ; ++test )
    {
        gets(buffer);
        n = 0;
        int curr = 0;
        int index = 0;
        int len = strlen( buffer );
        while( index <= len )
        {
            if( len == index || buffer[ index ] == ' ' )
            {
                if( curr != 0 ) number[ n++ ] = curr;
                curr = 0;
            }
            else
            {
                curr = 10 * curr + buffer[ index ] - '0';
            }
            ++index;
        }
        long long ret = 1;
        
        
        BEGIN:
            ret++;  
            for( int i = n - 1 ; i >= 0 ; --i )
                if( !good( ret , number[ i ] ) ) goto BEGIN;   
        
        printf("Case #%d: %I64d\n",test,ret);
    }
    
    return 0;
}