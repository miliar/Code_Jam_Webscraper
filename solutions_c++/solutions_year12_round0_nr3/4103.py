#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <set>
using namespace std;
int main()
{
	ifstream in("ci.txt");
	ofstream out("co.txt");
	int A,B;
	int T;
	set<int> visitSet;
	in>>T;
	int i=0;
	int j;
	stringstream ss;
	int sumPair;
	for(;i<T;i++)
	{
		in>>A>>B;
		int cur = A;
		sumPair=0;
		while(cur<=B)
		{
			visitSet.insert(cur);
			ss<<cur;
			string soustr;
			ss>>soustr;
			ss.clear();
			int n = soustr.size();
			int count=1;
			for(j=1;j<n;j++)
			{
				int leastLen = n-j;
				string frontsub = soustr.substr(0,j);
				string leastsub = soustr.substr(j,leastLen);
		//		reverse(frontsub.begin(),frontsub.end());
				string ostr = leastsub+frontsub;
				if(ostr[0]=='0')
				{
					continue;
				}
				int newValue =atoi(ostr.c_str());
				if((visitSet.find(newValue))!=visitSet.end() || newValue<A ||newValue>B )
				{
					continue;
				}
				else
				{
					count++;
					visitSet.insert(newValue);
				}

			}
			int pairNum=0;
			if(count>1)
				pairNum = ((count-1)*count)/2;
			sumPair+=pairNum;
			cur++;
		}
		out<<"Case #"<<i+1<<": "<<sumPair<<endl;
		visitSet.clear();
	}
	return 0;
}

