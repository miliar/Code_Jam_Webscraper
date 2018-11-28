#include <iostream>
#include <fstream>
#include <vector>
#include <stdint.h>

using namespace std;


int 
	main () 
{
	ifstream in = ifstream ("in.txt");
	ofstream out = ofstream ("out.txt");
		
	size_t test_count;	
	in >> test_count;


	for (size_t i = 1; i <= test_count; ++i) {
        
        const size_t DRAW = 0;
        const size_t X = 1;
        const size_t Y = 2;        
        const size_t NOT_FINISHED = 3;
        size_t result = DRAW;
            
        vector<uint32_t> xrows(4, 0);
        vector<uint32_t> xcols(4, 0);
        vector<uint32_t> xdiags(2, 0);
            
        vector<uint32_t> yrows(4, 0);
        vector<uint32_t> ycols(4, 0);
        vector<uint32_t> ydiags(2, 0);


        for (size_t row = 0; row < 4; ++row) {           
            for (size_t col = 0; col < 4; ++col) {
                char c;
                in >> c;

                if (c == '.') {
                    result = NOT_FINISHED;
                }

                if (c == 'X' || c == 'T') {
                    ++xrows[row];
                    ++xcols[col];

                    if (col == row) {
                        ++xdiags[0];
                    }

                    if ((col + row) == 3) {
                        ++xdiags[1];
                    }
                }

                if (c == 'O' || c == 'T') {
                    ++yrows[row];
                    ++ycols[col];

                    if (col == row) {
                        ++ydiags[0];
                    }

                    if ((col + row) == 3) {
                        ++ydiags[1];
                    }
                }
            }
        }


        for (size_t j = 0; j < 4; ++j) {
            if (xrows[j] == 4) {
                result = X;           
            }
            if (xcols[j] == 4) {
                result = X;
            }
            if (yrows[j] == 4) {
                result = Y;
            }
            if (ycols[j] == 4) {
                result = Y;
            }
        }

        for (size_t j = 0; j < 2; ++j) {
            if (xdiags[j] == 4) {
                result = X;
            }
            if (ydiags[j] == 4) {
                result = Y;
            }
        }

        out << "Case #" << i << ": ";
        if (result == DRAW) {
            out << "Draw" << endl;
        }
        if (result == X) {
            out << "X won" << endl;
        }
        if (result == Y) {
            out << "O won" << endl;
        }
        if (result == NOT_FINISHED) {
            out << "Game has not completed" << endl;
        }
    }

    in.close();
    out.close();
}
