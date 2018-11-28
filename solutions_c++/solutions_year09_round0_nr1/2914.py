// GContest.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("A-large.in",ios::in);
	//ifstream fin("Download A-small.in",ios::in);
	ofstream fout("Output.out",ios::out);
	if (!fin.is_open()) cout<<"Fail to Read"<<endl;
	if (!fout.is_open()) cout<<"Fail to Write"<<endl;

	int L=0, D=0, N=0, Num=0, iL=0, maxL=15;
	char  cGet='\n';

	fin>>L>>D>>N;	
	string *sWordsHead=new string[D+1];
	string *sWords=sWordsHead;
	for (int iD=0;iD<D;++iD){
		fin.get();
		sWords->clear();
		for (iL=0; iL<L; iL++)
		{			
			*sWords+=fin.get();
		}
		*sWords+='\n';
		//cout<<*sWords<<endl;
		sWords++;
	}

	string *sTestHead=new string[L+1];
	string *sTest=sTestHead;
	for (int iN=0; iN<N;iN++){//for each test case
		Num=0;// initialize number of possible words found		
		sTest=sTestHead;//move to head;
		fin.get();
		// read L possibler character sets per test
		for (iL=0; iL<L; iL++){
			//sTest->clear();
			cGet=fin.get();
			if (cGet=='(')
			{
				getline(fin,*sTest,')');
			}
			else
			{
				*sTest=cGet;
			}
			//cout<<*sTest<<endl;
			sTest++;			
		}

		sWords=sWordsHead;
		for (int iD=0; iD<D; ++iD)// search for possible words
		{
			sTest=sTestHead;
			int flag=1, iL=0;
			//for each possible sub strings
			for (iL=0; iL<L; ++iL){
				std::string::size_type idx = sTest->find(sWords->at(iL));
				sTest++;
				if (std::string::npos == idx )
				{
					flag=0;break;
				}
			}
			sWords++;
			// if there is a case mismatched
			if (flag==1) Num++;
		}
		fout<<"Case #"<<iN+1<<": "<<Num<<endl;
	}

	fin.close();
	fout.close();
	return 0;
}

