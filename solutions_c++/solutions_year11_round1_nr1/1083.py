// FreeCell_Statistics.cpp : Defines the entry point for the console application.
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
    typedef std::vector< int > Steps;


}

bool getStep(std::string str,Steps& step);
bool getMinSteps(Steps& step);
bool getMaxDiff(int num1, int num2,int& diffLarge,int& diffSmall);

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
        bool isPossible = getMinSteps(step);

        ofstream ofs;
        ofs.open(resultFile,ofstream::app);
        if (isPossible)
        {
            ofs<<"Case #"<<crrentCaseNum++<<": "<<"Possible"<<endl;
        }
        else
        {
            ofs<<"Case #"<<crrentCaseNum++<<": "<<"Broken"<<endl;
        }
        
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
    bool isGetBotType = false;
    while( is>>word )
    {
        int num = atoi(word.c_str());
        step.push_back(num);
    }
    if (step.size() != 3)
    {
        cout<<"err!!";
        return false;
    }
    return true;
}

bool getMinSteps( Steps& step )
{
    using namespace std;
    const int maxD = step[0];
    const int todayPrecision = step[1];
    const int totalPrecision = step[2];
    const int maxCount = 100;
    bool isPossible(false);
    int diffHigh,diffLow;
    getMaxDiff(maxCount,todayPrecision,diffHigh,diffLow);
    for (int i = 1; i <= maxD ; i++)
    {
    	if ((i%diffHigh) == 0)
    	{
            isPossible = true;
            break;
    	}
    }

    if (isPossible)
    {
        if (todayPrecision != 100 && totalPrecision == 100)
        {
            isPossible = false;
        }
        if (todayPrecision != 0 && totalPrecision == 0)
        {
            isPossible = false;
        }
    }

    return isPossible;
}

bool getMaxDiff( int num1, int num2,int& diffLarge,int& diffSmall )
{
    bool finished(false);
    int diff1(num1),diff2(num2),max(1);
    while(!finished)
    {
        int tempdiff1(diff1),tempdiff2(diff2);
        diff1 = tempdiff2 % tempdiff1;
        if (diff1 == 0)
        {
            max = tempdiff1;
            break;
        }
        diff2 = tempdiff1 % tempdiff2;
        if (diff2 == 0)
        {
            max = tempdiff2;
            break;
        }
    }
    if (num1%max != 0 && num2%max != 0)
    {
        std::cout<<"err!";
    }
    diffLarge = num1 / max;
    diffSmall = num2 / max;
    return false;
}