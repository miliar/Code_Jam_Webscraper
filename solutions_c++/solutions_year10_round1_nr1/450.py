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

	int T;
    input>>T;
    for(int caseNum=0;caseNum<T;caseNum++)
    {
        int N,K;
        input>>N>>K;
        ImportantMessage("N = "<<N<<"  K = "<<K);
        
        char** ppBoard = new char*[N];
        for(int i=0;i<N;i++) ppBoard[i] = new char[N];

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++)
            {
                input>>ppBoard[j][N-i-1];
            }
        }
        cout<<"Original Board:"<<endl;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++) cout<<ppBoard[j][N-i-1];
            cout<<endl;
        }

        cout<<"Rotated Board:"<<endl;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++) cout<<ppBoard[i][j];
            cout<<endl;
        }

        cout<<"After Gravity:"<<endl;
        for(int j=0;j<N;j++)
        {
            int base = N-1;
            for(int i=N-1;i>=0;i--) if(ppBoard[i][j]!='.') ppBoard[base--][j] = ppBoard[i][j];
            for(int i=base;i>=0;i--) ppBoard[i][j] = '.';
        }
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<N;j++) cout<<ppBoard[i][j];
            cout<<endl;
        }

        cout<<"Determining Wins..."<<endl;
        bool redWins = false;
        bool blueWins = false;
        // horizontal
        for(int i=0;i<N;i++)
        {
            int red = 0;
            int blue = 0;
            for(int j=0;j<N;j++)
            {
                if(ppBoard[i][j]=='R'){red++;blue=0;}
                else if(ppBoard[i][j]=='B'){red=0;blue++;}
                else red=blue=0;
                if(red==K) redWins = true;
                if(blue==K) blueWins = true;
            }
        }
        // vertical
        for(int j=0;j<N;j++)
        {
            int red = 0;
            int blue = 0;
            for(int i=0;i<N;i++)
            {
                if(ppBoard[i][j]=='R'){red++;blue=0;}
                else if(ppBoard[i][j]=='B'){red=0;blue++;}
                else red=blue=0;
                if(red==K) redWins = true;
                if(blue==K) blueWins = true;
            }
        }
        //diagonal +
        for(int i=-N+1;i<N;i++)
        {
            int red = 0;
            int blue = 0;
            for(int j=0;j<N;j++)
            {
                if(i+j<0||i+j>=N) continue;
                if(ppBoard[i+j][j]=='R'){red++;blue=0;}
                else if(ppBoard[i+j][j]=='B'){red=0;blue++;}
                else red=blue=0;
                if(red==K) redWins = true;
                if(blue==K) blueWins = true;
            }
        }
        //diagonal -
        for(int i=0;i<2*N;i++)
        {
            int red = 0;
            int blue = 0;
            for(int j=0;j<N;j++)
            {
                if(i-j<0||i-j>=N) continue;
                if(ppBoard[i-j][j]=='R'){red++;blue=0;}
                else if(ppBoard[i-j][j]=='B'){red=0;blue++;}
                else red=blue=0;
                if(red==K) redWins = true;
                if(blue==K) blueWins = true;
            }
        }
        
        string answer = "Neither";
        if(redWins) answer = "Red";
        if(blueWins) answer = "Blue";
        if(redWins&&blueWins) answer = "Both";
        output<<"Case #"<<caseNum+1<<": "<<answer<<endl;

        for(int i=0;i<N;i++) delete[] ppBoard[i];
        delete[] ppBoard;
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
