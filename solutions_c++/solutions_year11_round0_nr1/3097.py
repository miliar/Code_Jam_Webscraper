#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>

#include "Utilities.h"
#include "PrimeManager.h"

using namespace std;

int main()
{
    int cases;

    ifstream inputFileStream("G:\\GoogleCodeJam\\A-large.in");
    ofstream ouputFileStream("G:\\GoogleCodeJam\\A-large.out");

    while (inputFileStream >> cases)
    {
        for (int c = 0;c < cases;c++)
        {
			int moves;
			int currentO = 1;
			int currentB = 1;
			char targetRobot;
			int targetLocation;
			int result = 0;
			int saveForAnother = 0;
			char lastRobot = 'N';

			inputFileStream >> moves;

			while (moves--)
			{
				int moveSteps = 0;

				inputFileStream >> targetRobot >> targetLocation;

				if (targetRobot == 'O')
				{
					moveSteps = abs(targetLocation - currentO) + 1;
				}
				else
				{
					moveSteps = abs(targetLocation - currentB) + 1;
				}
				
				if (lastRobot != targetRobot)
				{
					if (saveForAnother >= moveSteps)
					{
						moveSteps = 1;
					}
					else
					{
						moveSteps -= saveForAnother;
					}

					lastRobot = targetRobot;
					saveForAnother = 0;
				}

				if (targetRobot == 'O')
				{
					currentO = targetLocation;
				}
				else
				{
					currentB = targetLocation;
				}

				saveForAnother += moveSteps;
				result += moveSteps;
			}

            //Output
            ouputFileStream << "Case #" << (c + 1) << ": " << result << endl;
        }
    }

    return 0;
}