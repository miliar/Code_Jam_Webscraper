// GCJ2010_1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	int ca = 0;
	cin>>t;
	while(t--)
	{
		ca++;
		int n;
		int k;
		cin>>n;
		cin>>k;
		k = k+1;
		int res = k%(int)(pow(2.0,double(n)));
		if(res == 0){
			cout<<"Case #"<<ca<<": ON"<<endl;
		}
		else{
			cout<<"Case #"<<ca<<": OFF"<<endl;
		}
	}
	return 0;
}

