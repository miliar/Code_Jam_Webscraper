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
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.txt","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		int n,m,a;
		cin>>n>>m>>a;
		cout<<"Case #"<<t+1<<": ";
		rep2(x1,0,n)
			rep2(y1,0,m)
				rep2(x2,0,n)
					rep2(y2,0,m)
					{
						if(a==abs(x1*y2-x2*y1))
						{
							cout<<"0 0 "<<x1<<" "<<y1<<" "<<x2<<" "<<y2;
							goto done;
						}
					}


			cout<<"IMPOSSIBLE";

			done:cout<<endl;
	}
	return 0;
}
