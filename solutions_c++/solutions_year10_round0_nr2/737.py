#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include "BigIntegerLibrary.hh" 
// Big Integer Library is avaliable at http://mattmccutchen.net/bigint/

using namespace std;

const BigUnsigned BigZero(0);

BigUnsigned CalculateGCD( BigUnsigned a, BigUnsigned b )
{
    if ( a == BigZero )
        return b;

    while ( b != BigZero )
    {
        if ( a > b )
            a = a - b;
        else
            b = b - a;
    }
    return a;
}

int main( int argc, char** argv )
{
    if ( argc != 2 )
    {
        cout << "Please input file name!" << endl;
        return 1;
    }

    ifstream input(argv[1], ios_base::in );

    if ( !input.is_open() )
    {
        cout << "Cannot open input file!" << endl;
        return 1;
    }
    
    int C, N;
    int ii, jj;

    vector<BigUnsigned> events;
    vector<BigUnsigned> difference;

    BigUnsigned gcd;
    BigUnsigned y;

    BigUnsigned tmp_bigint;
    string tmp_string;

    // 
    input >> C;

    for ( ii = 0; ii < C; ++ii )
    {
        events.clear();
        difference.clear();

        input >> N;
        for ( jj = 0; jj < N; ++jj )
        {
            input >> tmp_string;
            tmp_bigint = stringToBigUnsigned(tmp_string);
            events.push_back(tmp_bigint);
        }
        sort(events.begin(), events.end() );
        
        for ( jj = 1; jj < N; ++jj )
            difference.push_back( events[jj] - events[jj-1] );

        gcd = difference[0];

        for ( jj = 1; jj < N-1; ++jj )
            gcd = CalculateGCD( gcd, difference[jj] );

        y = BigZero;

        while ( y < events[N-1] )
            y += gcd;

        y -= events[N-1];

        cout << "Case #" << ii+1 << ": " << y << endl;
        
    }


    input.close();
    return 0;
}
