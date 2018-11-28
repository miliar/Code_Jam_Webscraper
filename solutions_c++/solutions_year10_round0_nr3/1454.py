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

int to[ 1100 ];int64 has[ 1100 ];
int N , R , K , arr[ 1100 ] , siz[ 1100 ];
int main()
{
    int TT;
    fscanf( in , "%d" ,&TT );
    for( int T = 1 ; T <= TT ; T++ )
    {
        fscanf( in , "%d%d%d" ,&R ,&K ,&N );
        for( int c = 0 ; c < N ; c++ )
            fscanf( in , "%d" ,&arr[ c ] );
        int64 sum = arr[ 0 ]; int ind = 1 % N , ss = 1;
        while( sum + arr[ ind ] <= K && ss < N )
        {
            sum += arr[ ind ]; ind = (ind + 1) % N; ss ++;
        }
        to[ 0 ] = ind; has[ 0 ] = sum;siz[ 0 ] = ss;
        for( int c = 1 ; c < N ; c++ )
        {
            sum = has[ c - 1 ] - arr[ c - 1 ]; ind = to[ c - 1 ];ss --;
            while( sum + arr[ ind ] <= K && ss < N )
            {
                sum += arr[ ind ]; ind = (ind + 1) % N;ss ++;
            }
            has[ c ] = sum; to[ c ] = ind;siz[ c ] = ss;
        }
        int64 ans = 0; int i = 0;
        for( int r = 0 ; r < R ; r++ )
        {
            ans += has[ i ]; i = to[ i ];
        }
        fprintf( out , "Case #%d: %I64d\n" ,T ,ans );
    }
    return 0;
}

