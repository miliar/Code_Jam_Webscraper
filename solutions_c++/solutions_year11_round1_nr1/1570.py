// googel code jam round 1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
   int pg,pd;

	int ng;
   
   int casenum=1;
   int remain;
   int beichushu;
   int chushu;
   ifstream acin("Asmall.in",ios::in);
   ofstream acout("Asamll.out",ios::out);
	acin>>ng;
	int n;
	bool result=false;
   int i,j,k;
	while(ng)
	{   result=false;
		acin>>n>>pd>>pg;
	if(pg==0||pg==100)
	{
		if(pg==pd) result=true;
		else result=false;
		goto end;
	}
	 beichushu=100;
	   chushu=pd;
	
  while(true)
  {
	  remain=beichushu%chushu;
	  if(remain==0) break;
	  beichushu=chushu;
	  chushu=remain;

  }
  

	if((100/chushu)<=n) result=true;
end:
	acout<<"Case #"<<casenum<<": ";
	if(result) acout<<"Possible"<<endl;
	else acout<<"Broken"<<endl;
	ng--;
	casenum++;
	}
	return 0;
}
