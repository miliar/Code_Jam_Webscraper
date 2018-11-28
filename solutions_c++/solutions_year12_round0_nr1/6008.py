//#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <errno.h>
#include <string>
#include <vector>
#include <conio.h>



typedef std::string String;
typedef std::vector<std::string> StringVector;

typedef unsigned int    U32;
typedef int             S32;
typedef float           F32;
typedef double          F64;



    char alphabet[26][2] = {        {'a', 'y'},
                                    {'b', 'n'},
                                    {'c', 'f'},
                                    {'d', 'i'},
                                    {'e', 'c'},
                                    {'f', 'w'},
                                    {'g', 'l'},
                                    {'h', 'b'},
                                    {'i', 'k'},
                                    {'j', 'u'},//guess z or u
                                    {'k', 'o'},
                                    {'l', 'm'},
                                    {'m', 'x'},
                                    {'n', 's'},
                                    {'o', 'e'},
                                    {'p', 'v'},
                                    {'q', 'z'},// guess z or u
                                    {'r', 'p'},
                                    {'s', 'd'},
                                    {'t', 'r'},
                                    {'u', 'j'},
                                    {'v', 'g'},
                                    {'w', 't'},
                                    {'x', 'h'},
                                    {'y', 'a'},
                                    {'z', 'q'}
                                };


int main(int argc, char* argv[])
{
    std::ofstream outFile;
    outFile.open ("A-small.out");
    std::ifstream inFile;
    inFile.open("A-small-attempt5.in");

    if(!(outFile.is_open() && inFile.is_open()))
        return -1;
    
   
    U32 inputLineCount = 0;
    std::string tmpStr;
    StringVector inVector;

    for ( ;inFile.good(); )
    {
        tmpStr.clear();
        getline(inFile, tmpStr);
        if(tmpStr.size())
            inVector.push_back(tmpStr);
    }
    inFile.close();

    U32 numberOfCases = inVector.size()-1;

    StringVector outVector;

    U32 currLen = 0;

    for(U32 x = 1; x < numberOfCases + 1; x++)
    {
        tmpStr.clear();

        currLen = inVector[x].size();
        for(U32 i = 0; i < currLen; i++)
            if(inVector[x].at(i) == ' ')
                tmpStr.push_back(inVector[x].at(i));
            else
                for(U32 u = 0; u < 26; u++)
                    if(inVector[x].at(i) == alphabet[u][1])
                        tmpStr.push_back(alphabet[u][0]);
        outVector.push_back(tmpStr);
    }


    printf("Input\n"
            "%d\n", numberOfCases);
    /*outFile << "Input\n" << numberOfCases << "\n";*/

    for(U32 x = 1; x < numberOfCases+1; x++)
    {
        printf("%s\n", inVector[x].c_str());
        /*outFile << inVector[x] << "\n";*/
    }
    printf("\n__________________________\n"
            "\n"
            "Output\n");
    /*outFile << "\n__________________________\n\nOutput\n";*/
    for(U32 x = 0; x < outVector.size(); x++)
    {
        printf("Case #%d: %s\n", x+1, outVector[x].c_str());
        outFile << "Case #"<< x + 1 << ": " << outVector[x] << "\n";
    }

    outFile.close();


    while(!kbhit()){}
    return 0;
}
