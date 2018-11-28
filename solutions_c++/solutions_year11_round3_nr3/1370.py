// roundc3.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;
int main()
{   ifstream acin("1.in",ios::in);
    ofstream acout("1.out",ios::out);
	int play[1000];
	int ng;
	int casenum=1;
	int low;
	int high;
	int i,j,k;
	int count;
	bool result=true;
	acin>>ng;
	while(ng)
	{
		acin>>count>>low>>high;
		for(i=0;i<count;i++)
			acin>>play[i];
		for(i=low;i<=high;i++)
		{ result=true;
			for(j=0;j<count;j++)
			{
				if(i%play[j]!=0&&play[j]%i!=0)
				{
					result=false;
					break;
				}
			}
			if(result==true) break;
		} 
		acout<<"Case #"<<casenum<<": ";
		if(result) acout<<i<<endl;
		else acout<<"NO"<<endl;
		ng--;
		casenum++;
	}
	return 0;
}

