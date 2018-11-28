// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE

#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <list>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;

int main()
{
	ifstream inf;
	ofstream of;
	inf.open("d:\\input.in",ios::in);
	of.open("d:\\output.txt");

	int n;
	string ssss;
	inf>>ssss;
	sscanf(ssss.c_str(),"%d",&n);

	for(int i=0;i<n;++i)
	{
		string s;
		int q,m;
		int res;
		inf>>s;
		
		sscanf(s.c_str(),"%d",&q);
		vector<string> qq;
		vector<string> mm;
		char c[2];
		inf.read(c,1);
		for(int j=0;j<q;++j){
			char buf[100000];
			inf.getline(buf,100000,'\n');
			s = string(buf);
			qq.push_back(s);
		}
		inf>>s;
		sscanf(s.c_str(),"%d",&m);
		map<string,int> maps;
		inf.read(c,1);
		for(int j=0;j<m;++j){
			char buf[100000];
			inf.getline(buf,100000,'\n');
			mm.push_back(s= string(buf));
			for(int k=0;k<qq.size();++k){
				if(s==qq[k]){
					maps[s]=k;
					break;
				}
			
			}			
		}
		vector<int> mins(q,0);
		for(int j=mm.size()-1;j>=0;--j){
			vector<int> mins2(q,100000000);
			int mi=100000000;
			for(int k=0;k<q;++k)
			{
				mi=min(mi,mins[k]);
				if (k!=maps[mm[j]])
				{
					mins2[k]=min(mins2[k],mins[k]);
				}
			}
			for(int k=0;k<q;++k)
				if (k!=maps[mm[j]])
					mins2[k]=min(mins2[k],mi+1);
			mins = mins2;
		/*	for(int u=0;u<mins.size();++u)
				cout<<mins[u]<<" ";
			cout<<endl;*/
		}
		res = mins[0];
		for(int j=1;j<mins.size();++j)
			res = min(res,mins[j]);
		of << "Case #" << (i+1)<<": ";
		of << res;
		of << '\n';
	}
	inf.close();
	of.close();
	return 0;
}
