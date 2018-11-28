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
	char * inputName="C-large.in";
	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	//fin.open ( "input.txt");

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
	unsigned int n;
	unsigned int m;
	unsigned int x;
	unsigned int tot;
	x=0;
	m=10000000;
	tot=0;
	fin>>n;
	for (int i=0; i<n; i++)
	{
		unsigned int z;
		fin>>z;
		if (z<m) m=z;
		x^= z;
		tot+=z;
	}
	if (x!=0) 
	{
		fout<<"NO";
		return;
	}
	else
	{
		fout<<tot-m;
	}
}
