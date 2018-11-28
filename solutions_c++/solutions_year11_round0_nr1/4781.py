///
/// @brief  Problem_A.cpp in codejam 2011
/// @author Dohyun Yun ( dualistmage@wisenut.co.kr )
/// @date   2011.05.08
///

#include <iostream>
#include <fstream>

using namespace std;



///////////////////////////////////////////////////////////////////////////////////////////////////
// Main
///////////////////////////////////////////////////////////////////////////////////////////////////
int main(int argc, char* argv[])
{
    int testNo, buttonNo, count = 1;

    int robot[2][2]; // First : [0] orange [1] blue, Second : [0] position [1] turn
    int lastTurn, targetButton;
    int index;
    char robotType;

    cin >> testNo;
    while( testNo > 0 )
    {
        lastTurn = 0;
        robot[0][0] = 1;
        robot[0][1] = 0;
        robot[1][0] = 1;
        robot[1][1] = 0;

        cin >> buttonNo;
        while( buttonNo > 0 )
        {
            cin >> robotType;
            if ( robotType == 'O' )
                index = 0;
            else
                index = 1;
            cin >> targetButton;

            // Move and increase turn
            if ( robot[index][0] != targetButton )
            {
                robot[index][1] += abs( targetButton - robot[index][0] );
                robot[index][0] = targetButton;
            }

            // Check if push button is available
            if ( lastTurn >= robot[index][1] )
                lastTurn++;
            else
                lastTurn = robot[index][1] + 1;
            robot[index][1] = lastTurn;

            buttonNo--;
        }

        cout << "Case #" << count++ << ": " << lastTurn << endl;
        testNo--;
    }
} // end - int main()

