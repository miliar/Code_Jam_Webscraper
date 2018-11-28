#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio> 
#include <deque>  
#include <queue>
#include <stack> 
#include <iomanip>
#include <cctype>

#define rep(i,n) for(i=0;i<n;i++)

using namespace std;

int main()
{
	int i,j,k,L,D,N;
	ifstream in("input.txt");
	ofstream out("output.txt");
	string s;
	vector<string> vd;
	in>>L>>D>>N;
	rep(i,D)
	{
		in>>s;
		vd.push_back(s);
	}
	rep(i,N)
	{
		int c=0;
		vector<string> vs;
		in>>s;
		j=0;
		while (j<s.size())
		{
			string st;
			if (isalpha(s[j]))
				st.push_back(s[j]);
			else
			{
				j++;
				while ((j<s.size())&&(s[j]!=')'))
				{
					st.push_back(s[j]);
					j++;
				}
			}
			vs.push_back(st);
			j++;
		}
		rep(j,vd.size())
		{
			bool f=1; k=0;
			while ((k<vd[j].size())&&(f))
			{
				if (find(vs[k].begin(),vs[k].end(),vd[j][k])==vs[k].end())
					f=0;
				k++;
			}
			if (f) c++;
		}
		out<<"Case #"<<(i+1)<<": "<<c<<endl;
		cout<<"Case #"<<(i+1)<<": "<<c<<endl;
	}
	return 0;
}

