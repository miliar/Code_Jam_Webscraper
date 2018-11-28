// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<iostream>
#include<fstream>
using namespace std;
int main()
{ ifstream acin("c.in",ios::in);
  ofstream acout("c.out",ios::out);
	int ng;
	int casenum=1;
	int t;
	int min=10000000;
	int val;
	int num;
	acin>>ng;
	while(ng)
	{  int k;
	min=10000000;
	  num=0;
	  val=0;
		acin>>t;
		while(t)
		{
			acin>>k;
			num=num^k;
			
			val+=k;
			if(k<min) min=k;
			t--;
		} 
		acout<<"Case #"<<casenum<<": ";
		if(num!=0) acout<<"NO"<<endl;
		else acout<<val-min<<endl;
		casenum++;
		ng--;
	}
	return 0;

}
