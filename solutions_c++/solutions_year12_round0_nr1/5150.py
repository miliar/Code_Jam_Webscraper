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
#include <cassert>


////////////////////////////////
//  Non-Standard Includes     //
////////////////////////////////

#include "Windows.h"
//#include "BigIntegerLibrary.hh"         // from http://mattmccutchen.net/bigint/
//#include "boost/math/common_factor.hpp" // from http://www.boost.org/


////////////////////////////////
//  Typedefs and Macros       //
////////////////////////////////

typedef long long           LL;
typedef unsigned long long  ULL;


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

    char refInput[] = 
        "ejp mysljylc kd kxveddknmc re jsicpdrysi" \
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" \
        "de kr kd eoya kw aej tysr re ujdr lkgc jv";

    char refOutput[] = 
        "our language is impossible to understand" \
        "there are twenty six factorial possibilities" \
        "so it is okay if you want to just give up";

    char conversion[26] = {0};

    // givens
    conversion['y' - 'a'] = 'a';
    conversion['e' - 'a'] = 'o';
    conversion['q' - 'a'] = 'z';

    // reference
    for (int i = 0; i < sizeof(refInput); i++)
    {
        if (refInput[i] != ' ')
        {
            conversion[refInput[i] - 'a'] = refOutput[i];
        }
    }

    // still one missing
    bool used[26] = {false};
    int missingIndex = -1;
    for (int i = 0; i < 26; i++)
    {
        if(conversion[i] != 0) used[conversion[i] - 'a'] = true;
        else missingIndex = i;
    }
    for (int i = 0; i < 26; i++)
    {
        if(!used[i]) conversion[missingIndex] = 'a' + i;
    }

	int T;
    input>>T;
    // get bad line
    char bad[256];
    input.getline(bad, sizeof(bad));
    for(int caseNum=0;caseNum<T;caseNum++)
    {
        char line[256];
        input.getline(line, sizeof(line));
        ImportantMessage(line);
        for(int i = 0; i < strlen(line); i++)
        {
            if(line[i] != ' ') line[i] = conversion[line[i] - 'a'];
        }
        output<<"Case #"<<caseNum+1<<": "<<line<<endl;
        GoodMessage("Case #"<<caseNum+1<<": "<<line);
    }

    return 0;
}

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
