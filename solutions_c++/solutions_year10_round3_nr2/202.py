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


map<PII, int> res;

Int c;

int getRes(int a, int b)
{
	if((a*c)>=b)
		return 0;
	if(res.find(mp(a,b)) != res.end())
		return res[mp(a,b)];

	int r = INF;
	for(Int i = c; i*a<b; i *= c)
	{
		r = min(r,
			max( getRes(i*a,b), getRes(a,i*a))
			);
	}
	res[mp(a,b)] = r+1;
	return (r+1);
}

void sol(int test)
{
	int l,p;
	cin>>l>>p>>c;
	res.clear();
	cout<<"Case #"<<test<<": "<<getRes(l,p)<<endl;
}


int main()
{
	int T;
	cin>>T;
	REP(i,T)
		sol(i+1);
	return 0;
}