// GCJ2010.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;
#include <math.h>

int main(int argc, char* argv[])
{
	int noOfTestCases;
	cin>>noOfTestCases;

	for(int i=0;i<noOfTestCases;i++)
	{
		int N;
		unsigned long K;

		cin>>N;
		cin>>K;

		if(K==0)
		{
            cout<<"Case #"<<i+1<<":"<<" "<<"OFF"<<'\n';
		}
		else
		{
			unsigned long t = pow(2, N);

			if((K%t + 1)==t)
			{
				cout<<"Case #"<<i+1<<":"<<" "<<"ON"<<'\n';
			}
			else
			{
				cout<<"Case #"<<i+1<<":"<<" "<<"OFF"<<'\n';
			}
		}
	}
	return 0;
}
