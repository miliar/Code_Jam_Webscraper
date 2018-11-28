#include <string>
#include <vector>
#include <cmath>

#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include<fstream> 
using namespace std;
int main()
{
	ofstream ofs; 
	ifstream ifs;
	ifs.open("d:\\Wraith\\A.in");
	ofs.open("d:\\Wraith\\a.out");
	int num;
	//cin>>num;
	ifs>>num;
	for(int i=1;i<=num;i++)
	{
		string a;
		ifs>>a;
		//cin>>a;
		ofs<<"Case #"<<i<<": ";
		//cout<<"Case #"<<i<<": ";
		long long asw=0.0;
		int base=1;
		string ta=a;
		sort(ta.begin(),ta.end());
		for(int j=1;j<ta.size();j++)
		{
			if(ta[j]!=ta[j-1])base++;
		}
		if(base<2)base=2;
		char key[37];
		int l=0;
		long long ss=a.size()-1.0;
		long long rs=pow(base,(double)ss);
		for(int k=0;k<a.size();k++)
		{
			long long vv=0.0;
			int p=0;
			while((key[p]!=a[k])&&(p<l))
			{
				p++;
			}
			if(p==l){vv=l;key[l]=a[k];l++;}else vv=p;
			if(vv==0)vv=1;else if(vv==1)vv=0;
			asw+=(vv*rs);
			rs/=base;
		}
		ofs<<asw<<endl;
		//cout<<asw<<endl;
	}
	return 0;
}