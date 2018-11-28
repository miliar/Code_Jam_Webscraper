//#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <cassert>
#include <cmath>
using namespace std;
ifstream fin; 
ofstream fout;

void preWork();
void work();
void work1();
int main(int argc, char *argv[])
{
	preWork();
	QCoreApplication a(argc, argv);

//	char * inputName="A-large.in";
//	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	fin.open ( "NO1_input.txt");

	fout.open("output.txt");
	int n;
	fin >>n;
	//char zzzz[100];
	//fin.getline(zzzz,100);
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



void preWork()
{
	
}

struct P
{
	int d, l;
};
void work()
{
	int n;
	int d;
	fin >>n;
	P z[20000];
	int r[20000];
	for (int i=0; i<n; i++)
	{
		fin >> z[i].d>>z[i].l;
	}
	fin>>d;
	memset(r,0,sizeof(r));
	r[0] = z[0].d;
	for (int i=0; i<n; i++)
	{
		if (r[i]> z[i].l) r[i] = z[i].l;
		int x = r[i]+z[i].d;
		if (x >= d ) 
		{
			fout<<"YES";
			return;
		}
		int j = i+1;
		while (j<n && x >= z[j].d)
		{
			if (r[j]==0)
			{
				r[j] = z[j].d-z[i].d;
			}
			j++;
		}
	}
	fout<<"NO";
}
