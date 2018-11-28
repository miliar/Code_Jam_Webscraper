//#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
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
	char * inputName="A-large.in";
	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
//	fin.open ( "input.txt");

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

void approach(int &now, int target, int step)
{
	if ( abs(now-target)<= step )
	{
		now= target;
		return;
	}
	else
	{
		if (now<target) now+=step;
		else now-=step;
	}
}
void work()
{
	int n;
	fin>>n;
	bool O[200];
	int position[200];
	int nextPositionB[200];
	int nextPositionO[200];
	int lastO, lastB;
	lastO=150;
	lastB=150;
	for (int i=0; i<n; i++)
	{
		char c;
		fin>> c;
		fin>> position[i];

		if (c=='O')
		{
			O[i]=true;

		}
		else
		{
			O[i]=false;
		}
	}
	for (int i=n-1; i>=0; i--)
	{
		if (O[i])
		{
			lastO=position[i];
		}
		else
		{
			lastB= position[i];
		}
		nextPositionB[i] = lastB;
		nextPositionO[i] = lastO;
	}
	int positionO=1;
	int positionB=1;
	int step;
	step=0;
	for (int i=0; i<n; i++)
	{
		if (O[i])
		{
			int a;
			a= abs(position[i]-positionO)+1;
			step+=a;
			positionO= position[i];
			approach(positionB,nextPositionB[i],a);
		}
		else
		{
			int a;
			a= abs(position[i]-positionB)+1;
			step+=a;
			positionB= position[i];
			approach(positionO,nextPositionO[i],a);

		}
	}
	fout<<step;
}
/*
void test()
{
	LongInt b,c,e,f,g;
	f=9529;
	g=43690;
	f+g;
	LongInt a;
	a= LongInt("99999999999999999999999999999999") + LongInt ("99999999999999999999999999999999");
	cout<<a<<endl;
	a= LongInt("99999999999999999999999999999999") * LongInt ("99999999999999999999999999999999");
	cout<<a<<endl;

	c=-1;
	b= 1;
	e=0;
	cout<<(c+b)<<endl;
	cout<<(c*b)<<endl;
	cout<<(e*b)<<endl;
	cout<<(c*e)<<endl;

	a=2;
	for (int i=0; i<15; i++)
	{
		a= a*a;
	}
	cout<<a<<endl;

}

*/