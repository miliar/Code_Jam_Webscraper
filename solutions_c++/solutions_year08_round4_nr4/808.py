#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
vector<int> change;

vector<pair<int,int> > nodes;

int eval(int i)
{
	if(nodes[i].first)
	{
		int x1=eval(i*2+1);
		int x2=eval(i*2+2);
		return nodes[i].second?x1&x2:x1|x2;
	}
	return nodes[i].second;
}

int main() {
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("d-small.txt","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{

		cout<<"Case #"<<t+1<<": ";
		int m=10000;
		int k;
		string s;
		cin>>k>>s;
		vector<int> v;
		rep(i,k)
			v.push_back(i);
		do
		{
			string r="";
			for(int i=0;i<s.size();i+=k)
			{
				rep(j,k)
				{
					r+=s[i+v[j]];
				}
			}
			int c=0;
			char cur=0;
			foreach(x,r)
			{
				if(*x==cur)
					continue;
				c++;
				cur=*x;
			}
			m=min(m,c);
		}
		while(next_permutation(all(v)));
			done:cout<<m<<endl;
	}
	return 0;
}
