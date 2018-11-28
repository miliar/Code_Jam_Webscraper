#include <fstream>
#include <iostream>
#include <utility>
#include <string>

using namespace std;

#define MAX_CELL 110

int cells[MAX_CELL][MAX_CELL];

int main( int argc, char** argv )
{
    ifstream input(argv[1], ios_base::in);

    int C, R;
    int x1, x2, y1, y2;
    int ii, jj, kk, ll;
    int num;
    int t;
    
    input >> C;

    for ( ii = 0; ii < C ; ++ii )
    {
        for ( jj = 0; jj < MAX_CELL; ++jj )
            for ( kk = 0; kk < MAX_CELL; ++kk )
                cells[jj][kk] = 0;

        input >> R;
        for ( ll = 0; ll < R; ++ll )
        {
            input >> x1 >> y1 >> x2 >> y2;
            
            for ( jj = x1 ; jj <= x2; ++jj )
                for ( kk = y1; kk <= y2; ++kk )
                    cells[jj][kk] = 1;
        }

        num = 0;
        for ( jj = 0; jj < MAX_CELL; ++jj )
            for ( kk = 0; kk < MAX_CELL; ++kk )
                if ( cells[jj][kk] == 1 )
                    ++num;

        t = 0;
        while ( num != 0 )
        {
            
            for ( jj = MAX_CELL-1; jj >=1; --jj )
            {
                for ( kk = MAX_CELL-1; kk >= 1; --kk )
                {
                    if ( cells[jj][kk] == 1 && cells[jj-1][kk] != 1 && cells[jj][kk-1] != 1 )
                        cells[jj][kk] = 0;

                    if ( cells[jj][kk] == 0 && cells[jj-1][kk] == 1 && cells[jj][kk-1] == 1 )
                        cells[jj][kk] = 1;
                }
            }

            num = 0;
            for ( jj = 0; jj < MAX_CELL; ++jj )
                for ( kk = 0; kk < MAX_CELL; ++kk )
                    if ( cells[jj][kk] == 1 )
                        ++num;

            ++t;
        }

        cout << "Case #" << ii+1 << ": " << t << endl;
    }
        

    input.close();
    return 0;
}
