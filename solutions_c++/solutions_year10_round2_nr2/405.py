#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

double X[60];
double V[60];
bool arrive[60];
bool is_swap[60][60];

int main(int argc, char** argv)
{
    ifstream input(argv[1], ios_base::in);

    int C, N, K;
    double B, T;
    int tmp_k, tmp_swap;

    int ii, jj, kk;

    input >> C;
    for ( ii = 0; ii < C; ++ii )
    {
        input >> N >> K >> B >> T;
        for ( jj = 0; jj < N; ++jj )
        {
            input >> X[jj];
        }
        for ( jj = 0; jj < N; ++jj )
        {
            input >> V[jj];
            arrive[jj] = false;
        }

        for ( jj = 0; jj < N; ++jj )
            for ( kk = 0; kk < N; ++kk )
                is_swap[jj][kk] = false;

        // check how many swap
        for ( jj = N-1; jj >= 0; --jj )
        {
            if ( B-X[jj] > T*V[jj] )
                continue;
            else
                arrive[jj] = true;
            
            for ( kk = jj+1; kk < N; ++kk )
            {
                if ( !arrive[kk] )
                {
                    is_swap[jj][kk] = true;
                }
            }
        }

        tmp_k = 0;
        tmp_swap = 0;

        for ( jj = N-1; jj >= 0; --jj )
        {
            if ( arrive[jj] )
                tmp_k++;

            for ( kk = jj+1; kk < N; ++kk )
                if ( is_swap[jj][kk] )
                    tmp_swap++;

            if ( tmp_k >= K )
                break;
        }

        if ( tmp_k >= K )
            cout << "Case #" << ii+1 << ": " << tmp_swap << endl;
        else
            cout << "Case #" << ii+1 << ": IMPOSSIBLE" << endl;
    }


    input.close();
    return 0;
}
