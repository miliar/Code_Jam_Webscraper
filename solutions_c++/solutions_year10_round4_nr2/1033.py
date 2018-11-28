#pragma region Template Code
////////////////////////////////////////////////////////////////
//                                                            //
//  Google Code Jam Template                                  //
//  by MooseBoys                                              //
//                                                            //
////////////////////////////////////////////////////////////////

////////////////////////////////////////////////
//                                            //
//  Generic Code                              //
//                                            //
////////////////////////////////////////////////

////////////////////////////////
//  Standard Includes         //
////////////////////////////////

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <map>


////////////////////////////////
//  Non-Standard Includes     //
////////////////////////////////

#include "Windows.h"                    // from http://www.msdn.com/windows
#include "BigIntegerLibrary.hh"         // from http://mattmccutchen.net/bigint/
#include "boost/math/common_factor.hpp" // from http://www.boost.org/


////////////////////////////////
//  Typedefs and Macros       //
////////////////////////////////

typedef long long           LL;
typedef unsigned long long  ULL;


////////////////////////////////
//  Debug Helpers             //
////////////////////////////////

// colored console messages
#define GoodMessage(message) setColor(GOOD),std::cout<<message<<std::endl,setColor(NORMAL)
#define BadMessage(message) setColor(BAD),std::cout<<message<<std::endl,setColor(NORMAL)
#define ImportantMessage(message) setColor(IMPORTANT),std::cout<<message<<std::endl,setColor(NORMAL)
#define CaseVarMessage(message) setColor(CASEVAR),std::cout<<message<<std::endl,setColor(NORMAL)
enum consoleColor{NORMAL,GOOD,BAD,IMPORTANT,CASEVAR};
inline void setColor(consoleColor c)
{
    WORD wAttributes = 0x07;
    if(c==GOOD) wAttributes = 0x0A;
    if(c==BAD) wAttributes = 0x0C;
    if(c==IMPORTANT) wAttributes = 0xF9;
    if(c==CASEVAR) wAttributes = 0x79;
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),wAttributes);
}


////////////////////////////////
//  Common Functions          //
////////////////////////////////

// find and open a problem input
int loadProblemFile(std::ifstream &inputFile, std::string &inputFileName)
{
    for(char cProblem='A';cProblem<='Z';cProblem++)
    {
        inputFileName = std::string(1,cProblem)+"-large-practice";
        inputFile.open(inputFileName+".in",std::ifstream::in);
        if(inputFile.is_open()) return 0;
        inputFileName = std::string(1,cProblem)+"-small-practice";
        inputFile.open(inputFileName+".in",std::ifstream::in);
        if(inputFile.is_open()) return 0;
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

// display the case number
#define casenum() ImportantMessage("Case #"<<caseNum)

// display a case argument
#define casevar(var) CaseVarMessage(#var<<" = "<<var)

// output and display case answer
#define caseans(ans) output<<"Case #"<<caseNum<<": "<<ans<<std::endl,GoodMessage("Case #"<<caseNum<<": "<<ans)

// common case loop
#define caseloop() int numCases=-1;input>>numCases;for(int caseNum=1;caseNum<=numCases;caseNum++)

////////////////////////////////////////////////
//                                            //
//  Generic Entrypoint                        //
//                                            //
////////////////////////////////////////////////

int CodeJamMain(std::ifstream& input, std::ofstream& output);  // forward-declaration of main problem function
int main(int argc, char* argv[])
{
    std::ifstream input;
    std::ofstream output;
    int ret = -1;
    if(getProblemIO(input,output)==0) ret = CodeJamMain(input,output);
    if(ret==0) GoodMessage(">>>> SUCCESS <<<<");
    else BadMessage(">>>> FAILURE <<<<");
    system("pause");
    return ret;
}

#pragma endregion
////////////////////////////////////////////////
//                                            //
//  Problem-Specific Code                     //
//                                            //
////////////////////////////////////////////////

using namespace std;

int CodeJamMain(std::ifstream& input, std::ofstream& output)
{
    caseloop()
    {
        casenum();

        int P;
        input>>P;
        casevar(P);

        int constraints[1024];
        for(int i=0;i<(1<<P);i++) input>>constraints[i];
        int gamePrice;
        for(int i=0;i<P;i++) for(int j=0;j<(1<<(P-i-1));j++) input>>gamePrice; // small test only!

        int games = 0;
        for(int i=0;i<P;i++)
        {
            for(int j=0;j<(1<<(P-i-1));j++)
            {
                constraints[j] = min(constraints[2*j],constraints[2*j+1]);
                if(constraints[j]==0) games++;
                else constraints[j]--;
            }
        }

        caseans(games*gamePrice);
    }

    return 0;
}
