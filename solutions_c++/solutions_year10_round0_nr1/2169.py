#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <climits>

using namespace std;


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

    int T, N, K;
    int ii, jj;
    string is_on; 

    input >> T;

    for ( ii = 0; ii < T; ++ii )
    {
        input >> N >> K;

        for ( jj = 0; jj < N; ++jj )
        {
            if ( K % 2 == 0 )
                break;
            else 
                K = K/2;
        }

        if ( jj == N )
            is_on = "ON";
        else
            is_on = "OFF";

        cout << "Case #" << ii+1 << ": " << is_on << endl;
    }


    input.close();
    return 0;
}
