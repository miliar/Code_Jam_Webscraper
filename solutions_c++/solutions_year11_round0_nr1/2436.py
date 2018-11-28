// GoogleJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iosfwd>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <strstream>


namespace{
    int CaseNum;
    bool isGetCaseNum = false;
    const char* caseFile = "D:\\My Documents\\Visual Studio 2010\\Projects\\GoogleJam\\Debug\\A-large.in";
    const char* resultFile = "D:\\My Documents\\Visual Studio 2010\\Projects\\GoogleJam\\Debug\\resultFile.txt";
    std::vector<int> timeList;
    enum botType
    {
        Orange,BULE
    };
    typedef std::vector< std::pair< botType ,int > > Steps;


}

bool getStep(std::string str,Steps& step);
int getMinSteps(Steps& step);

int _tmain(int argc, _TCHAR* argv[])
{
    using namespace std;
    ifstream ifs;
    ifs.open(caseFile);
    string str;
    int crrentCaseNum = 1;

    while( getline(ifs,str) )
    {    
       if (!isGetCaseNum)
       {
           CaseNum = atoi( str.c_str() );
           isGetCaseNum = true;
           continue;
       }
       Steps step;
       getStep(str,step);
       int minStep = getMinSteps(step);

       ofstream ofs;
       ofs.open(resultFile,ofstream::app);
       ofs<<"Case #"<<crrentCaseNum++<<": "<<minStep<<endl;
       ofs.clear();
       ofs.close();


    }
	return 0;
}

bool getStep( std::string str,Steps& step )
{
    using namespace std;
    istrstream is(str.c_str());
    string word;
    bool isGetStepNum = false;
    int stepNum = 0;
    botType tempBotType ;
    bool isGetBotType = false;
    while( is>>word )
    {
        if (!isGetStepNum)
        {
            stepNum = atoi(word.c_str());
            isGetStepNum = true;
            continue;
        }
        if (!isGetBotType)
        {
            if (word == "O")
            {
                tempBotType = Orange;
            }
            else
            {
                tempBotType = BULE;
            }
            isGetBotType = true;
        }
        else
        {
            int action = atoi(word.c_str());
            step.push_back( make_pair(tempBotType,action) );
            isGetBotType = false;
        }
    }
    if (step.size() != stepNum)
    {
        cout<<"err!!";
        return false;
    }
    return true;
}

int getMinSteps( Steps& step )
{
    using namespace std;
    int orangeStepNum = 0;
    int buleStepNum = 0;
    int orangePos = 1;
    int bulePos = 1;

    bool isOrangeDone = false;
    bool isBuleDone = false;


    for (Steps::iterator it = step.begin(); it <  step.end(); it++)
    {
        if (it->first == Orange )
        {
            int newPos = it -> second; 
            orangeStepNum += abs(newPos - orangePos);     
            orangePos = newPos;
           if (isBuleDone)
           {
               if (buleStepNum > orangeStepNum)
               {
                   orangeStepNum = buleStepNum;
               }
               isBuleDone = false;
           }

           orangeStepNum++;
           isOrangeDone = true;
        }
        else
        {
            int newPos = it -> second;            
            buleStepNum += abs(newPos - bulePos);
            bulePos = newPos;
            if (isOrangeDone)
            {
                if (orangeStepNum > buleStepNum)
                {
                    buleStepNum = orangeStepNum;
                }
                isOrangeDone = false;
            }
            buleStepNum++;
            isBuleDone = true;
        }

        
    }

    return max(orangeStepNum,buleStepNum);
}