#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

#include <boost/lexical_cast.hpp>
#include <boost/assign.hpp>

using namespace std;
using namespace boost;
using namespace boost::assign;



int main(int argc, char** argv)
{
    // ifstream in("in");
    //ofstream out("A-large-1.out");
    auto& in = cin;
    auto& out = cout;

    out << setprecision(7);

    string line;
    getline(in, line);
    int nLines = boost::lexical_cast<int>(line); 


    for (int caseNo=0; caseNo < nLines; ++caseNo)
    {
        out << "Case #" << caseNo+1 << ": ";
    
        char board[4][4];
        int xMoves = 0;
        int oMoves = 0;
        int remaining = 0;
        auto isOwned = [&board](int x, int y, bool isX)
        {
            char tile = board[x][y];
            return tile == 'T' || (isX ? tile == 'X' : tile == 'O');
        };

        for (int i = 0; i < 4; ++i)
        {
            for (int j=0; j < 4; ++j)
            {
                char tile;
                in >> tile;
                board[i][j] = tile;
                if (tile == 'X') xMoves++;
                if (tile == 'O') oMoves++;
                if (tile == '.') remaining++;
            }
        }

        bool turnOfX = (xMoves > oMoves);
        bool hasWon = false;
        for (int i=0; i< 4; ++i)
        {
            hasWon = hasWon || (isOwned(i,0, turnOfX) && isOwned(i,1,turnOfX) && isOwned(i,2, turnOfX) && isOwned(i,3,turnOfX));
            hasWon = hasWon || (isOwned(0,i, turnOfX) && isOwned(1, i ,turnOfX) && isOwned(2, i, turnOfX) && isOwned(3, i,turnOfX));
        }

        hasWon = hasWon || (isOwned(0,0,turnOfX) && isOwned(1,1,turnOfX) && isOwned(2,2,turnOfX) && isOwned(3,3, turnOfX));
        hasWon = hasWon || (isOwned(0,3,turnOfX) && isOwned(1,2,turnOfX) && isOwned(2,1,turnOfX) && isOwned(3,0, turnOfX));

        if (hasWon && turnOfX)
        {
            out << "X won";
        }
        else if (hasWon && !turnOfX)
        {
            out << "O won";
        }
        else if (remaining == 0)
        {
            out << "Draw";
        }
        else
        {
            out << "Game has not completed";
        }

        out << endl;
    }


    return 0;
}

