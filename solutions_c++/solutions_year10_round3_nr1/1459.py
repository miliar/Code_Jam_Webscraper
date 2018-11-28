/*

  ID: AhmedAbdElSamie100
  PROG: A
  lANG: C++
  
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;


int main()
{
	vector<pair <int , int> > work;
	
	string temp="",temp1="";
	int testc=0,size=0,t1=0,t2=0,con=0;
	pair<int,int> tempp;

	tempp.first=0;
	tempp.second=0;
    
	ofstream fout ("A-small-attempt0.out");
    ifstream fin ("A-small-attempt0.in");
	
	fin>>testc;
	
	for(int i=0;i<testc;i++)
	{
		fin>>size;

		for(int j=0;j<size;j++)
		{
			fin>>t1>>t2;
			work.push_back(make_pair(t1,t2));
		}

		sort(work.begin(),work.end());

		for(int k=0;k<work.size();k++)
		{
			if(work[k].first>tempp.first && work[k].second>tempp.second)
			{
				tempp.first=work[k].first;
				tempp.second=work[k].second;
				continue;
			}
			if(work[k].first>tempp.first && work[k].second<tempp.second)
				con++;

			//cout<<work[k].first<<endl;
		}

		fout<<"Case #"<<i+1<<": "<<con<<endl;

		work.clear();

		con=0;
		tempp.first=0;
		tempp.second=0;

	}

return 0;
}

/*
															  */