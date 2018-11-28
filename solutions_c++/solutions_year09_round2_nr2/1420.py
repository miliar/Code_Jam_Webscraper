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
#include <set>

#define rep(i,n) for(i=0; i<n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz(c) (c).size()

using namespace std;

string sub="welcome to code jam";

int C=0;

int main()
{
	int i,j,T;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in>>T;

	rep(i,T)
	{
		long long buf,n;
		in>>n;
		buf=n;
		vector<int> v;
		while (n>0)
		{	
			v.push_back(n%10);
			n/=10;
		}
		n=buf;
		long long res=0;
		sort(v.begin(),v.end());
		bool f=1;
		while ((f)&&(res<=n))
		{
			f=next_permutation(v.begin(),v.end());
			res=0;
			rep(j,sz(v))
				res=(res*10)+v[j];		

		}
		if (!f)
		{
			v.push_back(0);
			sort(v.begin(),v.end());
			f=1;
			res=0;
			while ((f)&&(res<=n))
			{
				f=next_permutation(v.begin(),v.end());
				res=0;
				rep(j,sz(v))
					res=(res*10)+v[j];	
			}
		}
		out<<"Case #"<<(i+1)<<": "<<res<<endl;
	}
	return 0;
}

