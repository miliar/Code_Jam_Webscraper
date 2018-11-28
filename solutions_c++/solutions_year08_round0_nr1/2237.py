// SavingUniverse.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <map>
using namespace std;

void test_i(ofstream &outFile,
			const int tm,//第tm个用例
			const vector<string> &vEngine,
			const int &S,
			const vector<string> &vQuery,
			const int &Q
		  )
{
	outFile<<"Case #"<<tm<<": ";
/////////////////////////////
	map<string,int> src;

	int times=0;
	int i=0;//起点
loop:
	int flaged=0;
	for(int j=0;j<S;j++)
		src[vEngine[j]]=-1;
	for(;i<Q;i++)
	{
		if(-1==src[vQuery[i]])
		{
			src[vQuery[i]]=i;
			flaged++;
			if(S==flaged)
				break;
		}
	}
	if(S==flaged)
	{
		int maxIndex=-1;
		for(int k=0;k<S;k++)
		{
			if(src[vEngine[k]]>maxIndex)
				maxIndex=src[vEngine[k]];
		}
		times++;
		i=maxIndex;
		goto loop;
	}
	outFile<<times;
/////////////////////////////
	outFile<<endl;
}


int _tmain(int argc, _TCHAR* argv[])
{
	locale loc = locale::global(locale(""));
	ifstream inFile("C:\\Documents and Settings\\Administrator\\桌面\\GOOGLE_JAM\\A-large.in");
	if(!inFile)
	{
		cerr<<"ifstream error!"<<endl;
		return 1;
	}
	ofstream outFile("C:\\Documents and Settings\\Administrator\\桌面\\GOOGLE_JAM\\A-large.out");
	if(!outFile)
	{
		cerr<<"ofstream error!"<<endl;
		return 1;
	}
	locale::global(loc);

	int N;
	inFile>>N;
	int S,//the number of search engines
		Q;//the number of incoming queries


	int i=1;
	for(;i<=N;i++)
	{
		vector<string> vEngine,vQuery;
		char cb[1];
		inFile>>S;		
		inFile.read(cb,1);
		for(int j=0;j<S;j++)
		{
/*可行
			char ch,temp[100]={0};int t=0;
			while(1)
			{
				if(inFile.eof()) break;
				
				char cc[1];
				inFile.read(cc,1);
				ch=*cc;
//				inFile>>ch;
				if(ch!='\n')
				{
					if(ch!='\r')
						temp[t++]=ch;
				}
				else
					break;
			}
//			inFile.getline(temp,100,'\n');
	//		getline(inFile,temp,100);
	//		inFile.read(temp,100);
			string str(temp);
//			getline(inFile,str);
			vEngine.push_back(str);*/

			string str;
			getline(inFile,str);
			vEngine.push_back(str);
		}
		inFile>>Q;
		inFile.read(cb,1);
		for(int k=0;k<Q;k++)
		{
			string str;
			getline(inFile,str);
			vQuery.push_back(str);
/*
			char temp[100]={0};
			inFile.get(temp,100,'\n');
			string str(temp);
			vQuery.push_back(str);*/
		}
		::test_i(outFile,i,vEngine,S,vQuery,Q);
	}	
	return 0;
}


