// Picking up chicks.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;


int c;
int t;
int k;
long long b;
int n;
long long x[51];
int v[51];
bool reach[51];

int time;
int reachnum;
int swapnum;



int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("B-large.in");
	ofstream fout("outdata.txt");

	
	fin>>c;
	int cn=1;
	while(cn<=c)
	{
		fin>>n>>k>>b>>t;
		memset(reach,0,sizeof(reach));

		for(int i=1;i<=n;i++)
			fin>>x[i];
		for(int i=1;i<=n;i++)
			fin>>v[i];
		
		reachnum=0;
		for(int i=1;i<=n;i++)
		{
			time=(b-x[i])/v[i];
			if((b-x[i])%v[i]>0)
				time++;
			if(time<=t)
			{
				reach[i]=1;
				reachnum++;
			}
			else
				reach[i]=0;
		}

		if(reachnum<k)
		{
			fout<<"Case #"<<cn<<": "<<"IMPOSSIBLE"<<endl;
			cn++;
			continue;
		}
		
		int zero=0;
		int reached=0;
		swapnum=0;
		for(int i=n;i>=1;i--)
		{
			if(reach[i]==1)
			{
				swapnum+=zero;
				reached++;
			}
			else
				zero++;
			if(reached==k)
				break;
		}

		fout<<"Case #"<<cn<<": "<<swapnum<<endl;
		cn++;
	}
	return 0;
}

