// code jam B.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<stdio.h>
#include<algorithm>
#include<fstream>
using namespace std;
long long arr[1003],arr1[13],c;
long long gcd(long long a,long long b)
{
	while (true)
	{
		if (!(a%b)) return b;
		a%=b;
		if (!(b%a)) return a;
		b%=a;
	}
}

int main()
{
	//freopen("b.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	ifstream fin("b.txt");
	ofstream fout("out.txt");
	long long test,cas,n,i,p,j;
	fin>>test;
	for (cas=1;cas<=test;cas++)
	{
		fin>>n;
		for (i=0;i<n;i++) fin>>arr[i];
		sort(arr,arr+n);
		p=arr[n-1];
		c=0;
		for (i=0;i<n;i++)
		{
			for (j=i+1;j<n;j++) arr1[c++]=arr[j]-arr[i];
			//printf("%d\n",arr[i]);
		}
		for (i=1;i<c;i++)
		{
			if (arr1[i]) arr1[0]=gcd(arr1[0],arr1[i]);
			else arr1[0]=gcd(arr1[i],arr1[0]);
		}
		//printf("%d\n",arr[0]);
		fout<<"Case #"<<cas<<": "<<(arr1[0]-(p%arr1[0]))%arr1[0]<<endl;
		//printf("Case #%lld: %lld\n",cas,(arr1[0]-(p%arr1[0]))%arr1[0]);
	}
	return 0;
}

