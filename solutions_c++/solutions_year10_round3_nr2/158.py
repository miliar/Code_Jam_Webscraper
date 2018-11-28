// google B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	ifstream fin("B-large.in");
	ofstream fout("outdata.txt");

	int tn,cc;
	long l,p,c,t,re;

	fin>>tn;
	for (cc=1;cc<=tn;cc++)
	{
		fin>>l>>p>>c;
		t=ceil(log(double(double(p)/double(l)))/log(double(c)));
		re=ceil(log(double(t))/log(double(2)));
		fout<<"Case #"<<cc<<": ";
		fout<<re<<endl;
	}
	return 0;
}
