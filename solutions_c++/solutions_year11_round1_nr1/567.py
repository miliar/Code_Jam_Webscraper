#define _CRT_SECURE_NO_DEPRECATE

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<set>
#include<limits>
#include<string.h>
#include<memory.h>
using namespace std;


ifstream inf("A-large.in");
ofstream outf("out.txt");

#define cin inf

#define cout outf

int main()
{
	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		long long n,pd,pg;
		long long d=0;
		long long g=0;
		cin>>n>>pd>>pg;
		
		bool dcan = false;
		if(n >= 100)
			dcan = true;
		else
		{
			for(int i=1;i<=n;i++)
				if(i*pd%100 == 0)
					dcan = true;
		}
		bool gcan = false;
		if(pg < 100 || pd == 100)
			gcan = true;
		if(pg == 0 && pd > 0)
			gcan = false;

		string ret;
		if(dcan && gcan)
			ret = "Possible";
		else
			ret = "Broken";
		cout<<"Case #"<<t<<": "<<ret<<endl;
	}
} 