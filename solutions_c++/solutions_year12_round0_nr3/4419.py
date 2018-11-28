// BEGIN CUT HERE

// END CUT HERE
#line 5 "ImportantSequence.cpp"
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define SZ(v) (int)((v).size())

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


int main()
{
	/*int sum[2][3]={0};
	for(int i=0;i<2;i++)
		for(int j=0;j<3;j++)
			cout<<sum[i][j]<<endl;
	system("pause");
	return 0;*/

	ifstream infile;
	ofstream outfile;
	infile.open("in.in");
	outfile.open("out.in");
	int T;
	infile>>T;
	string line;
	getline(infile,line);
	

	
	for(int i=1;i<=T;i++)
	{
		int a,b;
		//getline(infile,line);
		infile>>a>>b;
		map<vector<int>,int> maping;
		for(int j=a;j<=b;j++)
		{
			vector<int> v;
			int k=j,num=0;
			while(k!=0)
			{
				int cur=k%10;
				v.push_back(cur);
				k=k/10;
				num++;
			}
			bool flag=false;
			for(int ii=0;ii<num;ii++)
			{
				map<vector<int>,int>::iterator it= maping.find(v);
				if(it!=maping.end())
				{
					it->second=it->second+1;
					flag=true;
					break;
				}
				int tem=v[0];
				for(int jj=0;jj<num-1;jj++)
					v[jj]=v[jj+1];
				v[num-1]=tem;
			}
			if(!flag)
				maping.insert(make_pair(v,1));
		}
		map<vector<int>,int>::iterator vt=maping.begin();
		int co=0,s=0;
		for(;vt!=maping.end();++vt)
		{
			int ret=vt->second;
			if(ret>1)
				co+=ret*(ret-1)/2;
		}
		//cout<<co<<endl;
		outfile<<"Case #"<<i<<": "<<co<<endl;
	}



	infile.close();
	outfile.close();
	system("pause");
	return 0;
}
