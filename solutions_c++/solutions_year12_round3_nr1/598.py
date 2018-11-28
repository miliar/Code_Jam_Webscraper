
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>
#include<ctime>

using namespace std;

const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long

int n;
vector<vector<int> > v;
vector<int> used;
bool ok;

void dfs(int k)
{
	if (used[k])
	{
		ok = true;
		return;
	}

	used[k]=1;

	REP(i,v[k].size())
	{
		dfs(v[k][i]);
	}
}

bool solve()
{
	
	cin>>n;
	v.clear();
	v.resize(n);

	REP(i,n)
	{
		int m; cin>>m;
		REP(j,m)
		{
			int a; cin>>a; --a;
			v[i].push_back(a);
		}
	}

	ok=false;

	REP(i,n)
	{
		used.clear();
		used.resize(n);
		dfs(i);
		if (ok) return true;
	}
	
	return false;
}

int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output_a_hard.txt","w",stdout);
#endif

	int T;
	cin>>T;

	REP(t,T)
	{

		if (solve())
		{
			printf("Case #%d: Yes\n",t+1);
		}
		else
		{
			printf("Case #%d: No\n",t+1);
		}
	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}