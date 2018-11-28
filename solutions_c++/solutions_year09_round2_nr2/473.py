#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

string lis;
string num;
int T , N;

int main()
{
    freopen( "F.out" , "w" , stdout );
    FILE *in = fopen( "B-large.in" , "r" );
    fscanf( in , "%d\n" ,&T );
    for( int TT = 1 ; TT <= T ; TT++ )
    {
        char inp[ 222 ];
        fscanf( in , "%s" ,inp );
        num = inp;
        num = string( 22 , '0' ) + num;
        next_permutation( num.begin() , num.end() );
        while( num[ 0 ] == '0' )num = num.substr( 1 );
        printf( "Case #%d: %s\n" , TT , num.c_str() );
    }
    scanf("%*d");
    return 0;
}
