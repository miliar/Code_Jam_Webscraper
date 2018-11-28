#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <cctype>
#include <iterator>
#include <utility>

using namespace std;

int main()
{
	int m,t,ans,i,j,n,a,b;
	vector<int> b1,b2;
	ifstream fin("A-large.in");
	ofstream fout("k.out");
	fin>>t;
	for(m=1;m<=t;m++)
	{
		ans=0;
		fin>>n;
		for(i=0;i<n;i++)
		{
			fin>>a>>b;
			b1.push_back(a);
			b2.push_back(b);
		}
		for(i=0;i<b1.size();i++)
		{
			for(j=0;j<b1.size();j++)
			{
				if(i==j) break;
				if((b1[i]<b1[j])&&(b2[i]>b2[j]))
					ans++;
				else if((b1[i]>b1[j])&&(b2[i]<b2[j]))
					ans++;
			}
		}
		b1.clear();
		b2.clear();
		fout<<"Case #"<<m<<": "<<ans<<"\n";
	}
}
