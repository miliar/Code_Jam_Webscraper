// a1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<math.h>
#include<fstream>

using namespace std;
int main()
{   ofstream acout("1.txt",ios::out);
ifstream acin("1.in",ios::in);
	int dp[1000];
	dp[0]=0;
	char pre='0';
	char cur;
	int opre=1;
	int bpre=1;
	int onum=0,bnum=0;
	int ng;
	int i,j,k;
	int step;
	int num;
	int casenum=1;
	acin>>ng;

	while(ng)
	{   dp[0]=0;
		onum=0;
	   bnum=0;
	   opre=1;
	   bpre=1;
	    pre='O';
		acin>>step;
		for(i=1;i<=step;i++)
		{
			acin>>cur;
			acin>>num;
			if(cur==pre)
			{    pre=cur;
				if(cur=='O') {dp[i]=dp[i-1]+abs(num-opre)+1;onum=i;opre=num;}
				else {dp[i]=dp[i-1]+abs(num-bpre)+1;bnum=i;bpre=num;}
			}
			else
			{  pre=cur;
				if(cur=='O')
				{
					dp[i]=max(abs(num-opre),dp[bnum]-dp[onum])+1+dp[onum];
					onum=i;
					opre=num;
			     }
			else 
			   {
				          dp[i]=max(abs(num-bpre),dp[onum]-dp[bnum])+1+dp[bnum];
                 bnum=i;
				 bpre=num;
				}
		   }
		}   
		acout<<"Case #"<<casenum<<": "<<dp[step]<<endl;
			ng--;
			casenum++;

	}
		return 0;
  
}


