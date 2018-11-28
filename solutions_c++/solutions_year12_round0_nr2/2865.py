#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <sstream>

using namespace std;

int main()
{
    ifstream inputFile("B-large.in");
    ofstream outputFile("B-large.out");

    if (inputFile.is_open() && inputFile.good() && outputFile.is_open() && outputFile.good())
    {
        string line;
        int numOfCases;

        getline(inputFile, line);
        numOfCases = atoi(line.c_str());

        for (int i=0; i<numOfCases; ++i)
        {
            int numOfGooglers, numOfSur, bestResult, y = 0;
            vector<int> totalScores;

            getline(inputFile, line, ' ');
            numOfGooglers = atoi(line.c_str());
            getline(inputFile, line, ' ');
            numOfSur = atoi(line.c_str());
            getline(inputFile, line, ' ');
            bestResult = atoi(line.c_str());

            getline(inputFile, line);
            istringstream iss(line);
            while (getline(iss, line, ' '))
            {
                totalScores.push_back(atoi(line.c_str()));
            }

            for (int ii=0; ii<numOfGooglers; ++ii)
            {
                bool isTrue = false;
                int newBest = bestResult;

                while (isTrue == false && newBest < 11)
                {
                    int low = bestResult - 1 >= 0 ? bestResult-1 : 0;
                    int low2 = bestResult -2 >= 0 ? bestResult-2 : 0;

                    //if (remaining - (newBest*2) == 0 || remaining - (newBest-1) - newBest == 0 || remaining - ((newBest-1)*2) == 0)
                    if (bestResult + (low*2) <= totalScores.at(ii))
                    {
                        y++;
                        isTrue = true;
                    }
                    else if (numOfSur > 0)
                    {
                        //if (remaining - (newBest-2) - (newBest-1) == 0 || remaining - ((newBest-2)*2) == 0 || remaining - newBest - (newBest-2) == 0)
                        if (bestResult + (low2*2) <= totalScores.at(ii))
                        {
                            y++;
                            numOfSur--;
                            isTrue = true;
                        }
                    }

                    newBest++;
                }
            }

            outputFile << "Case #" << i+1 << ": " << y << "\n";
        }
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
