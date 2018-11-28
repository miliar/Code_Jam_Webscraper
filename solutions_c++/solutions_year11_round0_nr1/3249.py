#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
struct Moves
{
  vector<bool> completed;
  vector<char> botColour;
  vector<int> btnNumber;
  vector<int> order;
};
int determine(struct Moves oMoves,struct Moves bMoves, int oLoc, int bLoc);
int main()
{
    ofstream output ("output.txt");
    ifstream input ("input.txt");

    int cases;
    input >> cases;
    for(int a = 0; a < cases; a++)
    {
        int numberButtons;
        input >> numberButtons;
        Moves moves;

        for(int b = 0; b < numberButtons; b ++)
        {

            int tempI;
            char tempC;
            input >> tempC >> tempI;
            moves.completed.push_back(false);
            moves.botColour.push_back(tempC);
            moves.btnNumber.push_back(tempI);

        }

        bool exit = false;
        int orangeLoc = 1;
        int blueLoc = 1;
        int counter = 0;
        Moves orangeMoves;
        Moves blueMoves;
        for(int x = moves.completed.size()-1; x >=0 ; x --)
        {
            if(moves.botColour[x] == 'O')
            {
                orangeMoves.completed.push_back(moves.completed[x]);
                orangeMoves.botColour.push_back('O');
                orangeMoves.btnNumber.push_back(moves.btnNumber[x]);
                orangeMoves.order.push_back(x);
            }
            else if(moves.botColour[x] == 'B')
            {
                blueMoves.completed.push_back(false);
                blueMoves.botColour.push_back('B');
                blueMoves.btnNumber.push_back(moves.btnNumber[x]);
                blueMoves.order.push_back(x);
            }

        }



        int numberMoves = moves.completed.size()-1;
 counter = determine(orangeMoves, blueMoves, 1, 1);


output << "Case #" << a+1 << ": " <<counter << endl;




    }


    return 0;
}

int determine(struct Moves oMoves,struct Moves bMoves, int oLoc, int bLoc)
{

    int orderTracker = 0;

    int counter = 0;


    bool ex = false;
    while (oMoves.btnNumber.size() > 0  || bMoves.btnNumber.size() >0)
    {

        bool justPressed = false;
        bool moveHappened = false;
        if(oMoves.btnNumber.size()!=0 )
        {
            if( oLoc < oMoves.btnNumber[oMoves.btnNumber.size()-1] )
            {
                oLoc++;
                moveHappened = true;
            }
            else if( oLoc > oMoves.btnNumber[oMoves.btnNumber.size()-1])
            {
                oLoc--;
                moveHappened = true;
            }
            else if( oLoc == oMoves.btnNumber[oMoves.btnNumber.size()-1] && (bMoves.order.size() == 0 || oMoves.order[oMoves.order.size()-1] < bMoves.order[bMoves.order.size()-1] ) )
            {
                justPressed = true;
                oMoves.btnNumber.pop_back();
                oMoves.order.pop_back();
                orderTracker++;
                moveHappened = true;
            }
        }
        if(bMoves.btnNumber.size() != 0)
        {
            if(  bLoc < bMoves.btnNumber[bMoves.btnNumber.size()-1])
            {
                bLoc++;
                moveHappened = true;
            }
            else if( bLoc > bMoves.btnNumber[bMoves.btnNumber.size()-1] )
            {
                bLoc--;
                moveHappened = true;
            }
            else if(  bLoc == bMoves.btnNumber[bMoves.btnNumber.size()-1] && (oMoves.order.size() == 0  || bMoves.order[bMoves.order.size()-1] <oMoves.order[oMoves.order.size()-1]))
            {
                if(justPressed != true)
                {
                    bMoves.btnNumber.pop_back();
                    bMoves.order.pop_back();
                    orderTracker++;
                    moveHappened = true;
                }

            }
        }


        if(moveHappened == true)
        {
            counter ++;
        }


    }
    return counter;

}

