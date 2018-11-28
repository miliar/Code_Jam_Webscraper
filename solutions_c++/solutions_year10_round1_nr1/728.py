#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

using namespace std;

char A[51][51];
char B[51][51];

char C[51][51];
char D1[102][51];
char D2[102][51];

int main(int argc, char** argv)
{
    ifstream input(argv[1], ios_base::in);
    
    int T, K, N;
    int ii, jj, kk, ll;
    bool red, blue;
    char current;
    int count;

    char tmp_red[51];
    char tmp_blue[51];
    
    input >> T;

    for ( ii = 0; ii < T; ++ii )
    {
        input >> N >> K;

        for ( jj = 0; jj < N; ++jj )
            for ( kk = 0; kk < N; ++kk )
                input >> A[jj][kk];

        for ( kk = 0; kk < N; ++kk )
        {
            ll = N-1;
            for ( jj = N-1; jj >=0; --jj )
            {
                if ( A[N-1-kk][jj] != '.' )
                {
                    B[ll][kk] = A[N-1-kk][jj];
                    --ll;
                }
            }

            for ( ; ll >= 0; --ll )
                B[ll][kk] = '.';

            B[kk][N] = '\0';
        }

        for ( jj = 0; jj < N; ++jj )
        {
            for ( kk = 0; kk < N; ++kk )
                C[jj][kk] = B[kk][jj];

            C[jj][N] = '\0';
        }

        for ( jj = N-1; jj >=0; --jj )
        {
            for ( kk = 0; kk <= N-1-jj; ++kk )
            {
                D1[N-1-jj][kk] = B[jj+kk][kk];
                D2[N-1-jj][kk] = B[jj+kk][N-1-kk];
            }
            D1[N-1-jj][kk] = '\0';
            D2[N-1-jj][kk] = '\0';

        }

        for ( jj = 1; jj < N-1; ++jj )
        {
            for ( kk = 0; kk <= N-1-jj; ++kk )
            {
                D1[N-1+jj][kk] = B[kk][jj+kk];
                D2[N-1+jj][kk] = B[kk][N-1-jj-kk];
            }
            D1[N-1+jj][kk] = '\0';
            D2[N-1+jj][kk] = '\0';
        }

        // test join K
        for ( jj = 0; jj < K; ++jj )
        {
            tmp_red[jj] = 'R';
            tmp_blue[jj] = 'B';
        }
        tmp_red[K] = '\0';
        tmp_blue[K] = '\0';

        red = false;
        blue = false;

        for ( jj = 0; jj < N; ++jj )
        {
            if ( strstr( B[jj], tmp_red ) != NULL )
                red = true;
            
            if ( strstr( B[jj], tmp_blue ) != NULL )
                blue = true;

            if ( strstr( C[jj], tmp_red ) != NULL )
                red = true;
            
            if ( strstr( C[jj], tmp_blue ) != NULL )
                blue = true;
        }

        for ( jj = 0; jj < 2*N-1; ++jj )
        {
            if ( strstr( D1[jj], tmp_red ) != NULL || strstr( D2[jj], tmp_red ) != NULL )
                red = true;
            
            if ( strstr( D1[jj], tmp_blue ) != NULL || strstr( D2[jj], tmp_blue ) != NULL)
                blue = true;
        }

        if ( red && blue )
            cout << "Case #" << ii+1 << ": " << "Both" << endl;

        if ( red && !blue )
            cout << "Case #" << ii+1 << ": " << "Red" << endl;

        if ( !red && blue )
            cout << "Case #" << ii+1 << ": " << "Blue" << endl;

        if ( !red && !blue )
            cout << "Case #" << ii+1 << ": " << "Neither" << endl;

    }


    input.close();
    return 0;
}
