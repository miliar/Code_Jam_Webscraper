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

typedef unsigned int        uint;
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
        
//#if 0
//        // read in problem parameters
//        string s;
//
//        // combinations
//        int C;
//        vector<string> combinations;
//        input>>C;
//        for(int i=0;i<C;i++) input>>s, combinations.pb(s);
//
//        // exclusions
//        int D;
//        vector<string> exclusions;
//        input>>D;
//        for(int i=0;i<D;i++) input>>s, exclusions.pb(s);
//
//        // operations
//        int N;
//        string operations;
//        input>>N;
//        input>>operations;
//
//        // print case summary
//        vector<string>::iterator it;
//        string caseSummary = "C:[ ";
//        for(it=combinations.begin();it!=combinations.end();it++) caseSummary+=*it+" ";
//        caseSummary += "]  X:[ ";
//        for(it=exclusions.begin();it!=exclusions.end();it++) caseSummary+=*it+" ";
//        caseSummary += "]  O:[ "+operations+" ]";
//        ImportantMessage(caseSummary);
//
//        // solve (naive)
//        string out = "";
//        for(uint i=0;i<operations.length();i++)
//        {
//            char invoked = operations[i];
//            cout<<"invoking "<<invoked<<"... ";
//
//            // check for combinations
//            bool foundCombo = false;
//            char lastChar = -1;
//            if(out.length()>0) lastChar = out[out.length()-1];
//            for(uint j=0;j<combinations.size();j++)
//            {
//                string combo = combinations[j];
//                if(combo[0]==lastChar&&combo[1]==invoked || combo[1]==lastChar&&combo[0]==invoked)
//                {
//                    foundCombo = true;
//                    cout<<"combining "<<combo[0]<<" and "<<combo[1]<<" to make "<<combo[2]<<" ";
//                    out[out.length()-1] = combo[2];
//                }
//            }
//
//            // check for exclusions
//            bool foundExclusion = false;
//            if(!foundCombo)
//            {
//                for(uint j=0;j<exclusions.size();j++)
//                {
//                    string exclusion = exclusions[j];
//                    char lookingFor = -1;
//                    if(exclusion[0]==invoked) lookingFor=exclusion[1];
//                    if(exclusion[1]==invoked) lookingFor=exclusion[0];
//                    for(uint k=0;k<out.length();k++)
//                    {
//                        if(out[k]==lookingFor)
//                        {
//                            foundExclusion = true;
//                            cout<<"conflict between "<<lookingFor<<" and "<<invoked<<" ";
//                            out = "";
//                        }
//                    }
//                }
//            }
//
//            // otherwise just append
//            if(!foundCombo && !foundExclusion)
//            {
//                cout<<"appending "<<invoked;
//                out += invoked;
//            }
//            cout<<endl;
//        }
//#endif

        // can optimize most of this
        char merge[26][26];
        memset(merge,-1,sizeof(merge));
        string die[26];
        for(int i=0;i<26;i++) die[i] = "";

        string caseSummary = "#:[ ";

        string s;

        int C;
        input>>C;
        for(int i=0;i<C;i++)
        {
            input>>s;
            merge[s[0]-'A'][s[1]-'A']=merge[s[1]-'A'][s[0]-'A']=s[2];
            caseSummary += s+" ";
        }

        caseSummary += "]  X:[ ";

        int D;
        input>>D;
        for(int i=0;i<D;i++)
        {
            input>>s;
            die[s[0]-'A'] += s[1];
            die[s[1]-'A'] += s[0];
            caseSummary += s+" ";
        }

        caseSummary += "]  O:[ ";

        int N;
        input>>N;
        input>>s;
        caseSummary += s+" ]";

        ImportantMessage(caseSummary);

        string out = "";
        int count[26] = {0};
        for(int i=0;i<s.length();i++)
        {
            if(out.length()>0)
            {
                char c = merge[*(out.end()-1)-'A'][s[i]-'A'];
                if(c!=-1)
                {
                    cout<<s[i]<<" merged with "<<*(out.end()-1)<<" to form "<<c<<" ";
                    count[*(out.end()-1)-'A']--;
                    *(out.end()-1) = c;
                }
                else
                {
                    bool died = false;
                    string conf = die[s[i]-'A'];
                    for(int j=0;j<conf.length()&&!died;j++)
                    {
                        if(count[conf[j]-'A']>0)
                        {
                            cout<<s[i]<<" conflicted with an existing "<<conf[j]<<" ";
                            out = "";
                            memset(count,0,sizeof(count));
                            died = true;
                        }
                    }
                    if(!died)
                    {
                        cout<<s[i]<<" was added ";
                        out += s[i];
                        count[s[i]-'A']++;
                    }
                }
            }
            else
            {
                out+=s[i];
                count[s[i]-'A']++;
                cout<<s[i]<<" was added ";
            }
            cout<<"[ "<<out<<" ]"<<endl;
        }

        // output result
        string strOut = "[";
        if(out.length()>0)
        {
            for(string::iterator sit = out.begin();sit!=out.end()-1;sit++) {strOut+=*sit;strOut+=", ";}
            strOut+=out[out.length()-1];strOut+="]";
        }
        else strOut+="]";
        output<<"Case #"<<caseNum+1<<": "<<strOut<<endl;
        GoodMessage("Case #"<<caseNum+1<<": "<<strOut);
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
