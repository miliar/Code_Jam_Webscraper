// Google Code Jam 2011 - Bot Trust.cpp : main project file.

#include <iostream>
#include <queue>
#include <stdlib.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int cases;
    cin >> cases;

    for (int i=0; i<cases; i++)
    {
        queue<int> blueInstructions, orangeInstructions;
        queue<char> turns;
        int instructions;
        cin >> instructions;

        int posBlue=1, posOrange=1, goToPosition;
        int seconds=0;
        char botTurn;

        int blueCanWalkPos = 0;
        int orangeCanWalkPos = 0;

        for (int j=0; j<instructions; j++)
        {
            cin >> botTurn;
            cin >> goToPosition;

            turns.push(botTurn);

            if (botTurn == 'B')
                blueInstructions.push(goToPosition);
            else
                orangeInstructions.push(goToPosition);

            // Do both have instructions? If not, keep reading
            // We need them both to have at least 1 instruction so we 
            // know what we are supposed to do
            while (blueInstructions.size() > 0 && orangeInstructions.size() > 0)
            {
                char currentTurn = turns.front(); turns.pop();
                int blueGoTo = blueInstructions.front(); 
                int orangeGoTo = orangeInstructions.front();

                int bluePosToWalk = abs(blueGoTo-posBlue);
                int orangePosToWalk = abs(orangeGoTo-posOrange);

                if (currentTurn == 'B')
                {
                    blueInstructions.pop();
                    // Are blue credits enough?
                    if (blueCanWalkPos >= bluePosToWalk)
                    {
                        orangeCanWalkPos += 1; // we only need 1 second to press the button
                        seconds += 1; // we only need 1 second to press the button
                    }
                    else
                    {
                        // We need to walk blue
                        orangeCanWalkPos += (bluePosToWalk - blueCanWalkPos) + 1;
                        seconds += (bluePosToWalk - blueCanWalkPos) + 1;
                    }

                    blueCanWalkPos = 0; // Reset creds
                    posBlue = blueGoTo;
                }
                else
                {
                    orangeInstructions.pop();
                    // Are blue credits enough?
                    if (orangeCanWalkPos >= orangePosToWalk)
                    {
                        blueCanWalkPos += 1; // we only need 1 second to press the button
                        seconds += 1; // we only need 1 second to press the button
                    }
                    else
                    {
                        // We need to walk blue
                        blueCanWalkPos += (orangePosToWalk - orangeCanWalkPos) + 1;
                        seconds += (orangePosToWalk - orangeCanWalkPos) + 1;
                    }

                    orangeCanWalkPos = 0;
                    posOrange = orangeGoTo;
                }

                //char currentTurn = turns.front(); turns.pop();
                //int blueGoTo = blueInstructions.front(); blueInstructions.pop();
                //int orangeGoTo = orangeInstructions.front(); orangeInstructions.pop();

                //int bluePosToWalk = abs(blueGoTo-posBlue);
                //int orangePosToWalk = abs(orangeGoTo-posOrange);

                //if (currentTurn == 'B')
                //{
                //    orangeCanWalkPos += bluePosToWalk;
                //    posBlue = blueGoTo;

                //    while (turns.front() == 'B')
                //    {
                //        turns.pop();
                //        blueGoTo = blueInstructions.front(); blueInstructions.pop();
                //        posBlue = blueGoTo;

                //        bluePosToWalk = abs(blueGoTo-posBlue);
                //        orangeCanWalkPos += bluePosToWalk;
                //    } 

                //    seconds += orangeCanWalkPos+1;
                //    if (orangeCanWalkPos > orangePosToWalk)
                //    {
                //        // Orange can walk enough, we just have to add 1 second for it to wait for blue before pressing the button
                //        seconds += 1;
                //    }
                //    else
                //    {
                //        // We also have to add the walking from
                //    }
                //}
                //else
                //{
                //}
            }
        }

        // Process the last turns
        while (!blueInstructions.empty())
        {
            int blueGoTo = blueInstructions.front(); 
            int bluePosToWalk = abs(blueGoTo-posBlue);

            blueInstructions.pop();
            // Are blue credits enough?
            if (blueCanWalkPos >= bluePosToWalk)
            {
                seconds += 1; // we only need 1 second to press the button
            }
            else
            {
                // We need to walk blue
                seconds += (bluePosToWalk - blueCanWalkPos) + 1;
            }

            blueCanWalkPos = 0; // Reset creds
            posBlue = blueGoTo;
        }

        while (!orangeInstructions.empty())
        {
            int orangeGoTo = orangeInstructions.front();
            int orangePosToWalk = abs(orangeGoTo-posOrange);

            orangeInstructions.pop();
            // Are blue credits enough?
            if (orangeCanWalkPos >= orangePosToWalk)
            {
                seconds += 1; // we only need 1 second to press the button
            }
            else
            {
                // We need to walk blue
                seconds += (orangePosToWalk - orangeCanWalkPos) + 1;
            }

            orangeCanWalkPos = 0;
            posOrange = orangeGoTo;
        }

        cout << "Case #" << (i+1) << ": " << seconds << endl; 
    }

    return 0;
}
