////////////////////////////////////////////////////////////////
//                                                            //
//  Google Code Jam Template (2011)                           //
//  by MooseBoys                                              //
//                                                            //
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////
//                                            //
//  Generic Code                              //
//                                            //
////////////////////////////////////////////////

#pragma region Standard Includes
////////////////////////////////
//  Standard Includes         //
////////////////////////////////

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <cassert>
#pragma endregion

#pragma region Non-Standard Includes
////////////////////////////////
//  Non-Standard Includes     //
////////////////////////////////

#include "Windows.h"
//#include "BigIntegerLibrary.hh"         // from http://mattmccutchen.net/bigint/
//#include "boost/math/common_factor.hpp" // from http://www.boost.org/
#pragma endregion

#pragma region Typedefs and Macros
////////////////////////////////
//  Typedefs and Macros       //
////////////////////////////////

typedef long long           LL;
typedef unsigned long long  ULL;
#define pb push_back
#pragma endregion

#pragma region Debug Helpers
////////////////////////////////
//  Debug Helpers             //
////////////////////////////////

// colored console messages
#define GoodMessage(message) {setColor(GOOD);std::cout<<message<<std::endl;setColor(NORMAL);}
#define BadMessage(message) {setColor(BAD);std::cout<<message<<std::endl;setColor(NORMAL);}
#define ImportantMessage(message) {setColor(IMPORTANT);std::cout<<message<<std::endl;setColor(NORMAL);}
enum consoleColor{NORMAL,GOOD,BAD,IMPORTANT};
inline void setColor(consoleColor c)
{
    WORD wAttributes = 0x07;
    if(c==GOOD) wAttributes = 0x0A;
    if(c==BAD) wAttributes = 0x0C;
    if(c==IMPORTANT) wAttributes = 0xF9;
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),wAttributes);
}
#pragma endregion

#pragma region Common Functions
////////////////////////////////
//  Common Functions          //
////////////////////////////////

// find and open a problem input
int loadProblemFile(std::ifstream &inputFile, std::string &inputFileName)
{
    for(char cProblem='A';cProblem<='Z';cProblem++)
    {
        inputFileName = std::string(1,cProblem)+"-test";
        inputFile.open(inputFileName+".in",std::ifstream::in);
        if(inputFile.is_open()) return 0;
        inputFileName = std::string(1,cProblem)+"-large";
        inputFile.open(inputFileName+".in",std::ifstream::in);
        if(inputFile.is_open()) return 0;
        for(char cAttempt='9';cAttempt>='0';cAttempt--)
        {
            inputFileName = std::string(1,cProblem)+"-small-attempt"+cAttempt;
            inputFile.open(inputFileName+".in",std::ifstream::in);
            if(inputFile.is_open()) return 0;
        }
    }
    return -1;
}

// load and create problem input and output streams
int getProblemIO(std::ifstream &input, std::ofstream &output)
{
    std::string fileName;
    if(loadProblemFile(input,fileName)){BadMessage("could not find any input files to load");return -1;}
    else{GoodMessage("successfully loaded input file \""<<fileName<<".in\"");}
    output.open(fileName+".out",std::ofstream::out);
    if(output.is_open()){GoodMessage("successfully created output file \""<<fileName<<".out\"");}
    else{BadMessage("could not create output file \""<<fileName<<".out\"");return -1;}
    return 0;
}
#pragma endregion


////////////////////////////////////////////////
//                                            //
//  Problem-Specific Code                     //
//                                            //
////////////////////////////////////////////////

using namespace std;

// problem entrypoint
int CodeJamMain()
{
    ifstream input;
    ofstream output;

    if(getProblemIO(input,output)) return -1;

    int T;
    input>>T;
    for(int caseNum=0;caseNum<T;caseNum++)
    {

        // thoughts:
        // -Patrick's "addition" is xor
        // -the set is "evenly" splittable iff for each bit position, the number of ones is even
        // -as long as the candy set satisfies this, Sean can give Patrick just the single least valuable candy
        int N;
        input>>N;

        int sum = 0;
        int badSum = 0;
        int minValue = 1<<30;
        for(int i=0;i<N;i++)
        {
            int n;
            input>>n;
            sum += n;
            badSum ^= n;
            if(n<minValue) minValue = n;
        }
        ostringstream out;
        if(badSum==0) out<<sum-minValue;
        else out<<"NO";

        output<<"Case #"<<caseNum+1<<": "<<out.str()<<endl;
        GoodMessage("Case #"<<caseNum+1<<": "<<out.str());
    }

    return 0;
}

#pragma region Generic Entrypoint
////////////////////////////////////////////////
//                                            //
//  Generic Entrypoint                        //
//                                            //
////////////////////////////////////////////////

int main(int argc, char* argv[])
{
    int ret = CodeJamMain();
    if(ret==0){GoodMessage(">>>> SUCCESS <<<<");}
    else{BadMessage(">>>> FAILURE <<<<");}
    system("pause");
    return ret;
}
#pragma endregion
