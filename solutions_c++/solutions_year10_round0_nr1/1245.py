//// a.cpp : 定义控制台应用程序的入口点。
////
//
//#include "stdafx.h"

#include <algorithm>

#include <iostream>
#include <math.h>
using namespace std;


int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N,K;
	int n;
	cin>>T;
	for (int i=0; i<T; i++)
	{
		cin>>N>>K;
		if (K<=0)
		{
			cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
			continue;
		}
		n=(int)(powf(2,N)+0.5);
		K=K%n;
		if (K!=(n-1))
		{
			cout<<"Case #"<<i+1<<": "<<"OFF"<<endl;
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<"ON"<<endl;
		}
	}
	return 0;
}

