#define _CRT_SECURE_NO_DEPRECATE

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<string.h>
#include<memory.h>
using namespace std;

ifstream inf("A-large.in");
ofstream outf("out.txt");
#define cin inf
#define cout outf
int solve(char* cl,int* id,int n)
{
	int lastb = 1;
	int lastbt = 0;
	int lasto = 1;
	int lastot = 0;
	for(int i=0;i<n;i++)
	{
		if(cl[i] == 'B')
		{
			int nbt = 1+abs(id[i] - lastb) + lastbt;
			if(nbt <= lastot)
				nbt = lastot+1;
			lastb = id[i];
			lastbt = nbt;
		}
		if(cl[i] == 'O')
		{
			int not = 1+abs(id[i] - lasto) + lastot;
			if(not <= lastbt)
				not = lastbt+1;
			lastot = not;
			lasto = id[i];
		}
	}
	return max(lastot,lastbt);
}
int main()
{
	int t,n;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		cin>>n;
		char cl[101];
		int id[101];
		for(int i=0;i<n;i++)
			cin>>cl[i]>>id[i];
		
		int ret = solve(cl,id,n);
		cout<<"Case #"<<c<<": "<<ret<<endl;
	}
}
