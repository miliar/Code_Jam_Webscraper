//#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
#include <fstream>
#include <string>
using namespace std;
ifstream fin;
ofstream fout;

void preWork();
void work();

int main(int argc, char *argv[])
{
	//preWork();
	QCoreApplication a(argc, argv);

//	char * inputName="A-large.in";
//	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	fin.open ( "input.txt");

	fout.open("output.txt");
	int n;
	fin >>n;
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


void work()
{
	int n,m;
	fin>> n>>m;
	char grid[ 60][60];
	bool no;
	no=false;
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
		{
			char c;
			fin>>c;
			grid[i][j]= c;
		}
	}
	for (int i=0; i<n; i++)
	{
		if (i<=0) continue;
		for (int j=1; j<m; j++)
		{
			if (grid[i][j] =='#' && grid[i][j-1] =='#' && grid[i-1][j] =='#' && grid[i-1][j-1] =='#' )
			{
				grid[i][j] ='/';
				grid[i][j-1] ='\\';
				grid[i-1][j] ='\\';
				grid[i-1][j-1] ='/';
				j++;
			}
		}
		for (int j=0; j<m; j++)
		{
			if (grid[i-1][j]=='#')
			{
				no=true;
				break;
			}
		}
		if (no) break;
	}
	for (int j=0; j<m; j++)
	{
		if (grid[n-1][j]=='#')
		{
			no=true;
			break;
		}
	}

	if (no)
	{
		fout<<endl<<"Impossible";
	}
	else
	{
		for (int i=0; i<n; i++)
		{
			fout<<endl;
			for (int j=0; j<m; j++)
			{
				fout<<grid[i][j];
			}
		}
	}
}

