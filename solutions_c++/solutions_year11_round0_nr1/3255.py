
#include <math.h>
#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

int min(int a, int b)
{
    if (a<b)
    {
        return a;
    } else {
        return b;
    }
}

int max(int a, int b)
{
    if (a>b)
    {
        return a;
    } else {
        return b;
    }
}

int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output");


    if(!inputFile)
    {
        cout << endl << "Failed to open file " << argv[0];
        return 0;
    }


    int testCases;
    inputFile >> testCases;

    for (size_t i=0; i<testCases;i++)
    {
        int totalTime = 0, timeForO = 0, timeForB = 0, currentOperationTime = 0;
        int stateOfB = 1, stateOfO = 1;

        int numberOfButtons;
        inputFile>>numberOfButtons;
        char previousRobot;

        for (size_t j=0; j<numberOfButtons; j++)
        {
            char robot;
            int button;
            inputFile>>robot>>button;

            if (robot == 'B')
            {
                currentOperationTime = abs(stateOfB - button)+1;
                stateOfB = button;

//                if (timeForB==0)
//                {
                    timeForO += /*currentOperationTime*/abs(max(1,currentOperationTime-timeForB));
//                }

                totalTime += abs(max(1,currentOperationTime-timeForB));
                timeForB = 0;/*max(0,timeForB-currentOperationTime);*/

            } else {

                currentOperationTime = abs(stateOfO - button)+1;
                stateOfO = button;

//                if (timeForO == 0)
//                {
                    timeForB += /*currentOperationTime*/abs(max(1,currentOperationTime-timeForO));
//                }

                totalTime += abs(max(1,currentOperationTime-timeForO));
                timeForO = 0;/*max(0,timeForO-currentOperationTime);*/
            }

        }
        outputFile<<"Case #"<<i+1<<": "<<totalTime<<endl;

    }


}
