#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

int numberLength( int N )
{
    int count = 0;
    while( N != 0 )
    {
        ++count;
        N /= 10;
    }
    return count;
}

int firstDigit( int N )
{
    while( (N/10) != 0 )
    {
        N /= 10;
    }

    return N;
}

int solve( int A, int B )
{
    vector<bool> recycled( B+1, false );

    int lowerA = A;
    int result = 0;

    while( A <= B )
    {
        /*if( recycled[A] )
        {
            ++A;
            continue;
        }*/

        recycled[A] = true;
        int oldA = A;

        int length = numberLength( A );
        int currentRes = 0;
        do
        {
            int aCopy = A;
            int last = A % 10;

            A /= 10;
            A += last * pow(10, length-1);

            // leading zero
            if( numberLength(A) < numberLength(aCopy) )
            {
                continue;
            }
            if( A <= B && A >= lowerA && !recycled[A] )
            {
                if( !recycled[A] )
                {
                   // cout << oldA << ", " << A << endl;
                }
                recycled[A] = true;
                ++currentRes;
            }

        }
        while( A != oldA );

        result += (currentRes*(currentRes+1)) / 2;

        ++A;
    }

    return result;
}

int main()
{
    ifstream input("B-large.in");
    ofstream output("output.txt");
    unsigned int N;
    input >> N;

    for( unsigned int i=1; i <= N; i++ )
    {
        output << "Case #" << i << ": ";

        int A, B;
        input >> A >> B;

        int result = solve( A, B );

        output << result << endl;
    }

    return 0;
}
