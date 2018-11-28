//#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
#include <cassert>
using namespace std;
ifstream fin;
ofstream fout;

void work();
//void test();
int main(int argc, char *argv[])
{
//	test();

	QCoreApplication a(argc, argv);
//	int x[9]= {1,2,3,4,3,2,1};
//	sort(x,x+7);
	char * inputName="B-large.in";
	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
//	fin.open ( "input.txt");

	fout.open("output.txt");
	int n;
	fin >>n;
	assert(fin);
	for (int i=0; i<n; i++)
	{
		fout<<"Case #"<<i+1<<": ";
		work();
		fout<<endl;
	}


	fin.close();

	fout.close();



//	return a.exec();
}

void work()
{
	int n;
	bool combine[200][200];
	char result[200][200];
	bool oppose[200][200];
	memset(combine,false,sizeof(combine));
	memset(oppose,false,sizeof(oppose));
	fin>>n;
	for (int i=0; i<n; i++)
	{
		char c1,c2,c3;
		fin>>c1>>c2>>c3;
		combine[c1][c2]=true;
		result[c1][c2]=c3;
		combine[c2][c1]=true;
		result[c2][c1]=c3;
	}
	fin>>n;
	for (int i=0; i<n; i++)
	{
		char c1,c2;
		fin>>c1>>c2;
		oppose[c1][c2]=true;
		oppose[c2][c1]=true;
	}
	fin>>n;
	int acc[200];
	memset(acc,0,sizeof(acc));
	string s;
	const char baseE[8]= {'Q','W','E','R','A','S','D','F'};
	for (int i=0; i<n; i++)
	{
		char c;
		fin>>c;
		if (s.size()==0)
		{
			s+=c;
			acc[c]++;
			continue;
		}
		char lastc;
		lastc= s[s.size()-1];
		if (combine[c][lastc])
		{
			s[s.size()-1]= result[c][lastc];
			acc[lastc]--;
			continue;
		}
		s+=c;
		acc[c]++;
		for (int j=0; j<8; j++)
		{
			char x= baseE[j];
			if (acc[x]>0 && oppose[c][x])
			{
				s="";
				memset(acc,0,sizeof(acc));
				break;
			}
		}
	}

	fout<<'[';
	if (s.size()>0) fout<<s[0];
	for (int i=1; i<s.size(); i++)
	{
		fout<<", "<<s[i];
	}
	fout<<']';
}
