#define _CRT_SECURE_NO_DEPRECATE

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<memory.h>
using namespace std;

ifstream inf("C-large.in");
ofstream outf("out.txt");
#define cin inf
#define cout outf

int a[1001];
int main()
{
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		int n;
		cin>>n;
		int all =0;
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			all ^= a[i];
		}
		if(all)
		{
			cout<<"Case #"<<c<<": NO"<<endl;
		}
		else
		{
			sort(a,a+n);
			int sum = 0;
			for(int i=1;i<n;i++)
				sum += a[i];
			cout<<"Case #"<<c<<": "<<sum<<endl;
		}
	}
}