//#include "LongInt.h"
#include <QtCore/QCoreApplication>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <string>
#include <cassert>
#include <iomanip>
using namespace std;
ifstream fin;
ofstream fout;
void preWork();
void work();
//void test();
int main(int argc, char *argv[])
{
//	test();

	QCoreApplication a(argc, argv);
//	int x[9]= {1,2,3,4,3,2,1};
//	sort(x,x+7);
	char * inputName="D-large.in";
	fin.open(inputName);
//	fin.open ( "A-small-practice.in");
	//fin.open ( "A-large-practice.in");
	//fin.open ( "input.txt");

	fout.open("output.txt");
	preWork();
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

double step[1100];
double step2[20];
int nowN;
int se[20];
bool used[20];
int xacc;
int tot;
double pacc;
void spread(int n)
{
	if (n==nowN)
	{
		tot++;
		for (int i=1; i<=nowN; i++) if (!used[i]) se[n]=i;
		bool v[20];
		memset(v,false,sizeof(v));
		for (int i=1; i<=n; i++)
		{

			if (v[i]) continue;
			int c;
			c=1;
			int now;
			now =se[i];
			v[i]=true;
			while (now!=i)
			{
				c++;
				v[now]=true;
				now= se[now];
			}
			if (c==nowN) xacc++;
			else pacc+=step[c];
		}
		return;
	}
	for (int i=1; i<=nowN; i++)
	{
		if (used[i]) continue;
		used[i]=true;
		se[n]=i;
		spread(n+1);
		used[i]=false;
	}
}
void valid()
{
	step2[0]=0;
	step2[1]=0;
	step2[2]=2;
	for (int i=3; i<=10; i++)
	{
		nowN =i;
		tot=0;
		xacc=0;
		pacc=0;
		memset(used,false,sizeof(used));
		spread(1);
	}
}
void preWork()
{
//	valid();
	step[0]=0;
	step[1]=0;
	step[2]=2;
	for (int i=3; i<1010; i++)
	{
		double a;
		a=0;
		for (int j=1; j<i-1; j++)
		{
			a+=(step[j] + step[i-j])/(i-1);
		}
		a+= (step[i-1]+2)/(i-1);
		step[i]=a;		
	}
}

void work()
{
	int n;
	int a[1100];
	bool v[1100];
	fin>>n;
	for (int i=1; i<=n; i++)
	{
		fin>>a[i];
	}
	memset(v,false,sizeof(v));
	double r;
	r=0;
	for (int i=1; i<=n; i++)
	{
		if (v[i]) continue;
		int c;
		c=1;
		int now;
		now =a[i];
		v[i]=true;
		while (now!=i)
		{
			c++;
			v[now]=true;
			now= a[now];
		}
		//r+=step[c];
		if (c>1) r+= c;
	}
	fout<<setprecision(10)<<r;

}

