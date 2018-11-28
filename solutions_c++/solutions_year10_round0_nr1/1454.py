#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <stdio.h>
#include <queue>
#include <set>
#include <map>
#include <stdlib.h>
#include <string.h>
using namespace std;

typedef long long int64;
typedef vector< int > vi;
typedef vector< vi > vii;
typedef vector< string > vs;
#define clr(a,b) memset(a,b,sizeof a)
#define all(a) a.begin(),a.end()
#define MP make_pair
FILE *in = fopen( "F.in" , "r" );
FILE *out = fopen( "F.out" , "w" );

int main()
{
    int N , K , T;
    fscanf( in , "%d" ,&T );
    for( int t = 1 ; t <= T ; t++ )
    {
        fscanf( in , "%d%d" ,&N ,&K );
        bool f = 1;
        for( int c = 0 ; c < N ; c++ )
            if( (K & (1 << c)) == 0 )f = 0;
        if( f )fprintf( out, "Case #%d: ON\n" ,t );
        else fprintf( out, "Case #%d: OFF\n" ,t );
    }
    return 0;
}
