// cannySplit.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iosfwd>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <strstream>
#include <xutility>
#include <algorithm>
#include <numeric>



namespace{
    int CaseNum;
    bool isGetCaseNum = false;
    const char* caseFile = "D:\\My Documents\\Visual Studio 2010\\Projects\\GoogleJam\\Debug\\C-large.in";
    const char* resultFile = "D:\\My Documents\\Visual Studio 2010\\Projects\\GoogleJam\\Debug\\resultFile.txt";


}
bool getList( std::string str,std::vector<int>& );
bool isSplitable(std::vector<int>& candyList);

int _tmain(int argc, _TCHAR* argv[])
{
    using namespace std;
    ifstream ifs;
    ifs.open(caseFile);
    string str;
    int crrentCaseNum = 1;
    bool isGetCandyNum = false;
    int candyNum = 0;


    while( getline(ifs,str) )
    {    
        if (!isGetCaseNum)
        {
            CaseNum = atoi( str.c_str() );
            isGetCaseNum = true;
            continue;
        }
        if (!isGetCandyNum)
        {
            candyNum = atoi( str.c_str() );
            isGetCandyNum = true;
            continue;
        }


        vector<int> candyList;
        getList(str,candyList);
        if(isSplitable(candyList))
        {
            sort(candyList.begin(),candyList.end());
            int maxPart = accumulate(candyList.begin()+1,candyList.end(),0);
            ofstream ofs;
            ofs.open(resultFile,ofstream::app);
            ofs<<"Case #"<<crrentCaseNum++<<": "<<maxPart<<endl;
            ofs.clear();
            ofs.close();
        }
        else
        {
            ofstream ofs;
            ofs.open(resultFile,ofstream::app);
            ofs<<"Case #"<<crrentCaseNum++<<": NO"<<endl;
            ofs.clear();
            ofs.close();
        }

        isGetCandyNum = false;

       


    }
    return 0;
}

bool getList( std::string str,std::vector<int>& candyList )
{
    using namespace std;
    istrstream is(str.c_str());
    string word;

    while( is>>word )
    {
      candyList.push_back(atoi(word.c_str())) ;
    }

    return true;
}

bool isSplitable( std::vector<int>& candyList )
{
    using namespace std;
    const int maxNum = *max_element(candyList.begin(),candyList.end());

    for (int divNum = 1,i = 0; divNum < maxNum ; divNum = pow(2.,i))
    {
        int sumNum = 0;
    	for (vector<int>::iterator it = candyList.begin(); it < candyList.end(); it++)
    	{
            int remainder = static_cast<int> (*it / divNum);
            sumNum += remainder%2;      
    	}
        if (static_cast<bool> (sumNum % 2))
        {
            return false;
        }
        i++;
    }
    return true;

}