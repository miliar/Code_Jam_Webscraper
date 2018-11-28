#include <iostream>
#include <vector>

using namespace std;

int T,ans;
vector<char> robot;
vector<int> target;
int OPos, BPos;

int main() {
    cin>>T;
    for (int t = 0; t < T; t++) {
        int numActions;
        scanf("%i", &numActions);
        //printf("numActions: %d\n", numActions);


        for (int act = 0; act < numActions; act++)
        {
            char myRobot;
            int myTarget;
            scanf(" %c %i", &myRobot, &myTarget);
            
            robot.push_back(myRobot);
            target.push_back(myTarget);
        }

        OPos = BPos = 1;
        int counter = 0;

        while (!robot.empty())
        {
            /*
            printf("counter: %d\n", counter);
            printf("OPos=%d, BPos=%d, nextRobot=%c, nextPos=%d\n", OPos, BPos, robot.at(0), target.at(0));
            printf("robotlen=%d, targetlen=%d\n", robot.size(), target.size());*/

            counter++;
            bool OPressed = false;
            if ((robot.at(0) == 'O') && (target.at(0) == OPos))
            {
                // Press the button
                robot.erase(robot.begin());
                target.erase(target.begin());
                OPressed = true;

                if (robot.empty())
                {
                    // Removed last one
                    break;
                }
            }
            else {
                for (int firstO = 0; firstO < robot.size(); firstO++)
                {
                    if (robot.at(firstO) == 'O')
                    {
                        // Move to direction
                        if (target.at(firstO) < OPos)
                        {
                            OPos--;
                        }
                        else if (target.at(firstO) > OPos)
                        {
                            OPos++;
                        }
                        
                        break;
                    }
                }
            }

            if ((robot.at(0) == 'B') && (target.at(0) == BPos) && !OPressed)
            {
                // Press the button
                robot.erase(robot.begin());
                target.erase(target.begin());
            }
            else {
                for (int firstR = 0; firstR < robot.size(); firstR++)
                {
                    if (robot.at(firstR) == 'B')
                    {
                        // Move to direction
                        if (target.at(firstR) < BPos)
                        {
                            BPos--;
                        }
                        else if (target.at(firstR) > BPos)
                        {
                            BPos++;
                        }
                        
                        break;
                    }
                }
            }


        }

       cout << "Case #" << t+1 << ": "<< counter << endl;
    }
    

   return 0;   
}

