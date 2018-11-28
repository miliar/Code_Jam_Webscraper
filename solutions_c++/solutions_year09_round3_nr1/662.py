// All Your Base.cpp : 定义控制台应用程序的入口点。
//


#include "stdafx.h"
#include "iostream"
#include "fstream"
#include "string"
#include "cmath"
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream ifile=ifstream("A-small-attempt0.in");
	cin.rdbuf(ifile.rdbuf());
	
	int num,i,j,tmp,base,d;
	string str,B;
	ofstream ofile=ofstream("A-small-attempt0.out");
	cout.rdbuf(ofile.rdbuf());
	int A[64];
	cin>>num;
	for(i=0;i<num;i++)
	{
		cin>>str;
		B="";
		for(j=0;j<str.length();j++)
		{
			d=B.find(str[j]);
			if(d<0)
				B.push_back(str[j]);
			A[j]=str[j];
		}
		base=B.length();
		if(base<2) base=2;
		for(j=0;j<str.length();j++)
		{
			d=B.find(str[j]);
			if(d==0) 
			{
				A[j]=1;
				continue;
			}
			if(d==1) 
			{
				A[j]=0;
				continue;
			}
			A[j]=d;
		}
		tmp=0;
		for(j=0;j<str.length();j++)
			tmp+=A[j]*pow((double)base,(double)str.length()-j-1);


		cout<<"Case #"<<i+1<<": "<<tmp<<endl;
	}

	system("pause");
	return 0;
}

