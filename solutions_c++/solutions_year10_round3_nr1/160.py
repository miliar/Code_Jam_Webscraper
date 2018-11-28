// Rope Intranet.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("outdata.txt");

int t;
int n;
int a[1001];
int b[1001];
int ans;

bool judge(int i,int j)
{
	if((a[i]-a[j])*(b[i]-b[j])>0)
		return false;
	else
		return true;
}


int _tmain(int argc, _TCHAR* argv[])
{
	fin>>t;
	int tn=1;
	while(tn<=t)
	{
		fin>>n;
		ans=0;

		for(int i=1;i<=n;i++)
		{
			fin>>a[i]>>b[i];
			for(int j=1;j<i;j++)
				if(judge(i,j))
					ans++;
		}

		fout<<"Case #"<<tn<<": "<<ans<<endl;
		tn++;
	}
	return 0;
}

