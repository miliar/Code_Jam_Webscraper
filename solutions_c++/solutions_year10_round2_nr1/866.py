#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define rep(i,n) for(i=0; i<n; i++)

using namespace std;

int main()
{
	int i,j,k,T,N,K,M,t;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	rep(t,T)
	{
		in>>N>>M;
		int c=0;
		vector<string> ve(N), vn(M);
		rep(i,N) 
			in>>ve[i];
		rep(i,M) 
			in>>vn[i];
		rep(i,M)
		{
			string s="/";
			j=1;
			while (j<vn[i].size())
			{
				while ((j<vn[i].size())&&(vn[i][j]!='/'))
					s+=vn[i][j++];
				if (find(ve.begin(),ve.end(),s)==ve.end())
				{
					ve.push_back(s);
					c++;
				}
				s+=vn[i][j++];
			}
		}
		out<<"Case #"<<(t+1)<<": "<<c<<endl;
	}
	return 0;
}

