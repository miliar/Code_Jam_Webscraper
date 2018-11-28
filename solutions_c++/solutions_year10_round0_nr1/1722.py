// Jam_A.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
using namespace std;



int main()
{
	freopen("large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long pw[30];
	pw[0]=1;
	for(int a=1; a<30; a++)
	{
		pw[a]=pw[a-1]*2;
	}
	long long t;
	cin>>t;
	for(int a=1; a<=t; a++)
	{
		cout<<"Case #"<<a<<": ";
		long long n,m;
		cin>>n>>m;
		long long p=pw[n];
		if(m<p-1)
		{
			cout<<"OFF\n";
			continue;
		}
		m++;
		if(m%p==0)
		{
			cout<<"ON";
		}
		else
		{
			cout<<"OFF";
		}
		cout<<endl;
		

	}

	return 0;
}

