// SaveUniverse.cpp : 定义控制台应用程序的入口点。
//
#include <stdio.h>
#include <tchar.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <hash_set>

using namespace std;
using namespace stdext;
long int getNum(ifstream& im)
{
	string strNum;
	if(!im.eof())
	{
		getline(im, strNum);
		return atoi(strNum.c_str());
	}
	else
		return 0;
}
int main(int argc, char* argv[])
{
	if(argc!=3)
	{
		printf("Please Input: [Input File Name] [Output File Name]\n");
		return 0;
	}
	long int numCase = 0;
	long int numSE = 0;
	long int numQry = 0;
	string strSE;
	string strQry;
	vector<string> vecSE;
	vector<string> vecQry;
	ifstream im(argv[1]);
	ofstream om(argv[2]);

	numCase = getNum(im);
	long int realNum = numCase;
	while(numCase>0)
	{
		int timeSwitch = 0;
		hash_set<string> setTobe;
		numCase--;
		vecSE.clear();
		vecQry.clear();
		
		numSE = 0;
		numQry = 0;

		numSE =getNum(im);
		while(numSE>0)
		{
			numSE--;
			getline(im,strSE);
			vecSE.push_back(strSE);
		}

		numQry = getNum(im);
		while(numQry>0)
		{

			
			getline(im,strQry);
			
			if(setTobe.find(strQry) == setTobe.end())
			{
				setTobe.insert(strQry);
			}
			if(setTobe.size()==vecSE.size())
			{
				timeSwitch++;
				setTobe.clear();
				setTobe.insert(strQry);
			}

			numQry--;
		}
		om<<"Case #"<<realNum-numCase<<": "<<timeSwitch<<endl;
	}
	return 0;
}

