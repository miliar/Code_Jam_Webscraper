// GoogleTest3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <iostream>
#include <cmath>
using namespace std;

void find_num_of_maches(const char *pattern,const char *source,int& count) {
	int lenP = strlen(pattern);
	int lenS = strlen(source);
	for(int i=0;i<lenS;++i) {
		if(source[i]==pattern[0]){
			if(lenP == 1){
				++count;
			}
			find_num_of_maches(pattern+1,source+i+1,count);
		}
	}	
}

void IntToString(double i, string & s)
{
    s = "";
    if (i == 0)
    {
        s = "0";
        return;
    }
    int count = log10(i);
    while (count >= 0)
    {
        s += ('0' + i/pow(10.0, count));
        i -= static_cast<int>(i/pow(10.0,count)) * static_cast<int>(pow(10.0,count));
        count--;
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("C:\\indrajitpractice.txt");
	ofstream fout("C:\\Output.txt");
	int numCases = 0;
	string str = "welcome to code jam";
	char Val[101];
	fin.getline(Val,101);
	numCases = atoi(Val);
	for(int i=0; i<numCases; ++i)
	{
		string strVal;
		getline(fin,strVal);
		int count = 0;
		find_num_of_maches(str.c_str(),strVal.c_str(),count);
		if(count >= 10000)
		{
			count = count%10000;
		}
		string outStr;
		IntToString(count , outStr);

		int n = outStr.size();
		string outputMainStr;
		if(n == 1)
		{
			outputMainStr = "000" + outStr;
		}
		else if(n==2)
		{
			outputMainStr = "00" + outStr;
		}
		else if(n==3)
		{
			outputMainStr = "0" + outStr;
		}
		else
		{
			outputMainStr = outStr;
		}

		fout<<"Case #"<<i+1<<": "<<outputMainStr<<"\n";

	}
	fin.close();
	fout.close();
	return 0;
}

