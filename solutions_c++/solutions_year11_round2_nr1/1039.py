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
	int n;
	fin>> n;
	int game[300][300];
	int t0[300];
	int w0[300];
	double WP[300];
	double OWP[300];
	double OOWP[300];
	for (int i=0; i<n; i++)
	{
		int t;
		int w;
		w=0;
		t=0;
		for (int j=0; j<n; j++)
		{
			char c;
			fin>>c;
			switch (c)
			{
			case '1':
				game[i][j]=1;
				t++;
				w++;
				break;
			case '0':
				game[i][j]=-1;
				t++;
				break;
			case '.':
				game[i][j] =0;
				break;
			}
		}
		WP[i]=  w/double(t);
		t0[i]= t;
		w0[i]=w;
	}
	for (int i=0; i<n; i++)
	{
		double a;
		a=0;
		for (int j=0; j<n; j++)
		{
			if (game[i][j]==0) continue;
			int w1,t1;
			w1= w0[j];
			t1= t0[j];
			t1--;
			if (game[i][j]==-1)
			{
				w1--;
			}
			a+=   w1/ double(t1);
		}
		a/= t0[i];
		OWP[i]= a;
	}
	for (int i=0; i<n; i++)
	{
		double a;
		a=0;
		for (int j=0; j<n; j++)
		{
			if (game[i][j]==0) continue;
			a+= OWP[j];
		}
		a/= t0[i];
		OOWP[i]= a;
	}

	for (int i=0; i<n; i++)
	{
		fout<<endl;
		fout<<setprecision(12)<<0.25* WP[i] + 0.5 * OWP[i]+ 0.25* OOWP[i];
	}
}

