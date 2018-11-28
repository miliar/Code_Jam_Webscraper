#include <cstdio>
#include <cmath>
#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char** args) {
    string XWinStr = "Case #%d: X won\n";
    string OWinStr = "Case #%d: O won\n";
    string DrawStr = "Case #%d: Draw\n";
    string DoneStr = "Case #%d: Game has not completed\n";

    int a = 4*'X';
    int b = 3*'X'+'T';
    int c = 4*'O';
    int d = 3*'O'+'T';
    ;
    ////////// Read //////////
    ifstream file;
    file.open ("Alarge");

    string tmp = "";
    getline( file, tmp );
    int T = atoi(tmp.c_str());

    for(int t = 1; t<=T; t++)
    {
        string C = "";
        for(int j = 0; j<4; j++)
        {
            getline( file, tmp );
            C += tmp;
        }

        // All combinations
        int hi[10] = {
            C[ 0]+C[ 1]+C[ 2]+C[ 3],
            C[ 4]+C[ 5]+C[ 6]+C[ 7],
            C[ 8]+C[ 9]+C[10]+C[11],
            C[12]+C[13]+C[14]+C[15],

            C[ 0]+C[ 4]+C[ 8]+C[12],
            C[ 1]+C[ 5]+C[ 9]+C[13],
            C[ 2]+C[ 6]+C[10]+C[14],
            C[ 3]+C[ 7]+C[11]+C[15],

            C[ 0]+C[ 5]+C[10]+C[15],
            C[ 3]+C[ 6]+C[ 9]+C[12]
        };

        // Check for winning conditions
        bool hasWinner = false;
        for(int j = 0; j<10; j++)
        {
            int q = hi[j];
            if (q == a || q == b)
            {
                printf(XWinStr.c_str(), t);
                hasWinner = true;
                break;
            }
            if (q == c || q == d)
            {
                printf(OWinStr.c_str(), t);
                hasWinner = true;
                break;
            }
        }

        if(!hasWinner)
        {
            // Determine if draw or if match is done
            string::size_type loc = C.find( ".", 0 );
            if(loc == string::npos)
            {
                printf(DrawStr.c_str(), t);
            }
            else
            {
                printf(DoneStr.c_str(), t);
            }
        }
        // Get rid of newline
        getline(file, tmp);
    }
    //////////////////////////
}
