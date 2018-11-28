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
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.txt","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		int n,v;
		cin>>n>>v;
		nodes.clear();
		vector<pair<int,int> > chang;
		rep(i,(n-1)/2)
		{
			int  g,c;
			cin>>g>>c;
			if(c)
				chang.push_back(make_pair(i,g));
			nodes.push_back(make_pair(1,g));
		}
		rep(i,(n+1)/2)
		{
			int x;
			cin>>x;
			nodes.push_back(make_pair(0,x));
		}
		int m=31;
		rep(i,1<<chang.size())
		{
			int x=0;
			rep(j,chang.size())
			{
				int b=(i>>j)&1;

				nodes[chang[j].first].second=chang[j].second^b;
				x+=b;
			}
			if(eval(0)==v)
				m=min(m,x);
		}
		cout<<"Case #"<<t+1<<": ";
		if(m==31)
			cout<<"IMPOSSIBLE";
		else
			cout<<m;
		cout<<endl;
	}
	return 0;
}
