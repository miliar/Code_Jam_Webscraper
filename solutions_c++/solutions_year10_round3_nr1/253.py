#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<cstdio>
#include<vector>
#include<list>
#include<sstream>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<cmath>
#include<functional>
#include<memory>
#include<stack>

using namespace std;


#define FOR(i,a,b) for(int i = a; i<b;++i)
#define RFOR(i,a,b) for(int i = (b-1); i>=a; --i)
#define REP(i,a) FOR(i,0,a)
#define RREP(i,a) RFOR(i,0,a)


#define ALL(a) a.begin(),a.end()
#define FILL(a,val) memset(a,val,sizeof(a))
#define pb(a) push_back(a)
#define sz(a) a.size()

#define mp make_pair

typedef long long Int;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<VI > VII;

const int INF = (1<<30);

vector<PII> x;

void sol(int test)
{
	int n;
	cin>>n;
	x.resize(n);
	REP(i,n)
		cin>>x[i].first>>x[i].second;
	sort(x.begin(), x.end());
	int r = 0;
	REP(i,n)
		REP(j,i)
		if(x[j].second>x[i].second)
			++r;
	cout<<"Case #"<<test<<": "<<r<<endl;
}

int main()
{
	int T;
	cin>>T;
	REP(i,T)
		sol(i+1);
	return 0;
}