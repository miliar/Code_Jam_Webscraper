#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <sstream>

using namespace std;

int main()
{
    ifstream inputFile("C-small-attempt0.in");
    ofstream outputFile("C-small-attempt0.out");

    if (inputFile.is_open() && inputFile.good() && outputFile.is_open() && outputFile.good())
    {
        string line;
        int numOfCases;

        getline(inputFile, line);
        numOfCases = atoi(line.c_str());

        for (int i=0; i<numOfCases; ++i)
        {
            string temp1, temp2, line;
            int num1, num2, tempNum[2], total = 0;

            getline(inputFile, line, ' ');
            num1 = atoi(line.c_str());
            getline(inputFile, line);
            num2 = atoi(line.c_str());
            tempNum[1] = num2;

            while (tempNum[1] > num1)
            {
                tempNum[0] = num1;

                while (tempNum[0] < tempNum[1])
                {
                    char tempStr1[8], tempStr2[8];
                    string str1, str2;

                    sprintf(tempStr1, "%d", tempNum[0]);
                    sprintf(tempStr2, "%d", tempNum[1]);
                    str1 = tempStr1;
                    str2 = tempStr2;

                    for (int ii=0; ii<str1.length()-1; ++ii)
                    {
                        if (str1.substr(1+ii) + str1.substr(0, 1+ii) == str2)
                        {
                            total++;
                            break;
                        }
                    }

                    tempNum[0]++;
                }

                tempNum[1]--;
            }

            outputFile << "Case #" << i+1 << ": " << total << "\n";
        }
    }

    inputFile.close();
    outputFile.close();

    return 0;
}
