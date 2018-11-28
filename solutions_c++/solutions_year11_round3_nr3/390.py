#define _CRT_SECURE_NO_DEPRECATE


#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<set>
#include<list>
#include<limits>
#include<string.h>
#include<memory.h>
using namespace std;

#define SZ(x) ((int)x.size())

ifstream inf("C-small-attempt0.in");
ofstream outf("out.txt");

#define cin inf

#define cout outf

int a[101];
int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n,l,h;
		cin>>n>>l>>h;
		for(int i=0;i<n;i++)
			cin>>a[i];
		bool can;
		for(int i=l;i<=h;i++)
		{
			can = true;
			for(int j=0;j<n;j++)
			{
				if(a[j]%i==0 || i%a[j] == 0)
					continue;
				can = false;
				break;
			}
			if(can)
			{
				cout<<"Case #"<<t<<": "<<i<<endl;
				break;
			}
		}
		if(!can)
			cout<<"Case #"<<t<<": NO"<<endl;
	}
} 