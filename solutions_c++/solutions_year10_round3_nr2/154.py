// google B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	ifstream fin("B-large.in",ios::binary|ios::in);
	ofstream fout("out.txt",ios::binary|ios::out);

	int tn,cc;
	long l,p,c,t,ans;

	fin>>tn;
	for (cc=1;cc<=tn;cc++)
	{
		fin>>l>>p>>c;
		t=ceil(log(double(double(p)/double(l)))/log(double(c)));
		ans=ceil(log(double(t))/log(double(2)));
		fout<<"Case #"<<cc<<": ";
		fout<<ans<<endl;
	}
	return 0;
}