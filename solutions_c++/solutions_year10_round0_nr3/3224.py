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
	long long i,j,k,t,T,R,N;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	rep(t,T)
	{
		long long y=0;
		in>>R>>k>>N;
		vector<long long> g(N);
		rep(i,N)
			in>>g[i];
		rep(i,R)
		{
			long long l,s=0;
			bool f=1;
			for(j=0; (j<N)&&(f); j++)
			{
				if ((s+g[j])>k)
					f=0;
				else s+=g[j];		
			}
			y+=s;
			j--;
			rep(l,j)
				g.push_back(g[l]);
			g.erase(g.begin(),g.begin()+j);
			
		}
		//cout<<"Case #"<<(t+1)<<": "<<y<<endl;
		out<<"Case #"<<(t+1)<<": "<<y<<endl;
	}
	return 0;
}



