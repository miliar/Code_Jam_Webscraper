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
	ofstream ofile=ofstream("A.txt");
	cin.rdbuf(ifile.rdbuf());
	cout.rdbuf(ofile.rdbuf());
	int num,i,j,k,tmp,base,h,d;
	string str,B;
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
		//for(j=0;j<str.length();j++)//从小到大排序
		//	for(k=j+1;k<str.length();k++)
		//	{
		//		if(A[j]>A[k])
		//		{
		//			tmp=A[j];
		//			A[j]=A[k];
		//			A[k]=tmp;
		//		}
		//	}
		//base=1;
		//for(j=1;j<str.length();j++)//得到进制
		//	if(A[j]!=A[j-1])
		//		base++;
		//h=0;
		//for(j=1,k=0;j<str.length();j++)//转成以0开始的数字
		//	if(A[j]!=A[j-1])
		//	{
		//		for(;h<j;h++)
		//			A[h]=k;
		//		k++;
		//	}
	/*	if(j==str.length())
		{
			for(;h<j;h++)
				A[h]=k;
		}*/
		//for(j=1;j<str.length();j++)//得到不以0开始的最小数字
		//{
		//	if(A[j]!=A[0])
		//	{
		//		tmp=A[0];
		//		A[0]=A[j];
		//		A[j]=tmp;
		//	}
		//}
		tmp=0;
		for(j=0;j<str.length();j++)
			tmp+=A[j]*pow((double)base,(double)str.length()-j-1);

		cout<<"Case #"<<i+1<<": "<<tmp<<endl;
	}

	system("pause");
	return 0;
}

