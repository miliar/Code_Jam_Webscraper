#include <QtCore/QCoreApplication>

#include <math.h>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>


bool isBaseCharacter(char unknownChar)
{
    if ((unknownChar == 'Q') ||
        (unknownChar == 'W') ||
        (unknownChar == 'E') ||
        (unknownChar == 'R') ||
        (unknownChar == 'A') ||
        (unknownChar == 'S') ||
        (unknownChar == 'D') ||
        (unknownChar == 'F'))
    {
        return true;
    } else {
        return false;
    }
}


int getBaseCharacterIndex(char baseChar)
{

    if (baseChar == 'Q')
    {
        return 0;
    }
    else if (baseChar == 'W')
    {
        return 1;
    } else if (baseChar == 'E')
    {
        return 2;
    } else if (baseChar == 'R')
    {
        return 3;
    } else if (baseChar == 'A')
    {
        return 4;
    } else if (baseChar == 'S')
    {
        return 5;
    } else if (baseChar == 'D')
    {
        return 6;
    } else if (baseChar == 'F')
    {
        return 7;
    } else {
        return -1;
    }

}


using namespace std;

int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output");


    if(!inputFile)
    {
        cout << endl << "Failed to open file " << argv[0];
        return 0;
    }

    char combinations[8][8];
    char oppositions[8][8];


    int testCases;
    inputFile >> testCases;

    for (size_t i=0; i<testCases;i++)
    {

        for (size_t i=0; i<8; i++)
        {
            for (size_t j=0; j<8; j++)
            {
                combinations[i][j] = '.';
                oppositions[i][j] = '.';
            }
        }


        int noCombinations = 0, noOppositions = 0;
        string invokeCharacters;
        int invokeCharactersSize;

        inputFile >> noCombinations;

        for (size_t j=0; j<noCombinations; j++)
        {
            string basePair;
            inputFile >> basePair;

            if ((!isBaseCharacter(basePair[0])) || (!isBaseCharacter(basePair[1])))
            {
                cout<<"Not base pair caracter in combination"<<endl;
                return 0;
            }
            combinations[getBaseCharacterIndex(basePair[0])][getBaseCharacterIndex(basePair[1])] = basePair[2];
        }

        inputFile >> noOppositions;

        for (size_t j=0; j<noOppositions; j++)
        {
            string basePair;
            inputFile >> basePair;

            if ((!isBaseCharacter(basePair[0])) || (!isBaseCharacter(basePair[1])))
            {
                cout<<"Not base pair caracter in combination"<<endl;
                return 0;
            }
            oppositions[getBaseCharacterIndex(basePair[0])][getBaseCharacterIndex(basePair[1])] = 'G';
        }



        inputFile >> invokeCharactersSize;
        inputFile >> invokeCharacters;
        std::vector<char> elementList;

        for (size_t j=0; j<invokeCharacters.length();j++)
        {
            elementList.push_back(invokeCharacters[j]);
            if (elementList.size()>1)
            {
                char L1 = elementList[elementList.size()-1];
                char L2 = elementList[elementList.size()-2];
                // combinations
                if ((isBaseCharacter(L2)) &&
                    ((combinations[getBaseCharacterIndex(L1)][getBaseCharacterIndex(L2)] != '.') ||
                    (combinations[getBaseCharacterIndex(L2)][getBaseCharacterIndex(L1)] != '.')))
                {
                    // there is a combination

                    char resultingLetter;
                    if (combinations[getBaseCharacterIndex(L1)][getBaseCharacterIndex(L2)] != '.')
                    {
                        resultingLetter = combinations[getBaseCharacterIndex(L1)][getBaseCharacterIndex(L2)];
                    } else {
                        resultingLetter = combinations[getBaseCharacterIndex(L2)][getBaseCharacterIndex(L1)];
                    }
                    elementList.pop_back();
                    elementList.pop_back();
                    elementList.push_back(resultingLetter);
                } else {
                    // check all characters in the element list for opposition
                    for (size_t k=0; k<elementList.size()-1;k++)
                    {
                        L2 = elementList[k];
                        if ((isBaseCharacter(L2)) && (oppositions[getBaseCharacterIndex(L1)][getBaseCharacterIndex(L2)] != '.'))
                        {
                            elementList.clear();
                            break;
                        } else if ((isBaseCharacter(L2)) && (oppositions[getBaseCharacterIndex(L2)][getBaseCharacterIndex(L1)] != '.'))
                        {
                            elementList.clear();
                            break;
                        }
                    }
                }
            }

        }

        outputFile<<"Case #"<<i+1<<": [";
        for (size_t k=0; k<elementList.size();k++)
        {
            outputFile<<elementList[k];
            if (k!=elementList.size()-1)
            {
                outputFile<<", ";
            }

        }
        outputFile<<"]"<<endl;

    }


}
