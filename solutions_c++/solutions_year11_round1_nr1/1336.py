
#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#include <time.h>

#define sz(a) a.size()
#define vi vector<int>
#define vs vector<string>
#define vii vector< pair<int,int> >
#define all(a) a.begin(),a.end()
#define pb push_back


int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("free1.out");

	long long t,n,pd,pg;

	in>>t;

	for(int i=1;i<=t;i++)
	{
		in>>n>>pd>>pg;

		out<<"Case #"<<i<<": ";
		bool flag = true;
		for(int j=1;j<=n;j++)
		{
			long double v= (pd/100.0)*j;
			long long v1 = (pd*j/100);
			if(abs(v-v1)<1e-6)
			{
				flag = false;
			}
		}
		if(pg==0&&pd>0 || pd<100 && pg==100 || flag)
		{
			out<<"Broken"<<endl;
			continue;
		}
		else
		{
			out<<"Possible"<<endl;
		}
	}
	return 0;
}