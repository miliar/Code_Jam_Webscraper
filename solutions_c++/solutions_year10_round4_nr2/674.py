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

const Int INF = (1LL<<30);

int m[2000];
int price[11][2000];

Int res[11][1500][11];

Int sol(int level, int match, int missed)
{
	if(level == -1)//single team
		if(missed>m[match])
			return INF;
		else
			return 0;
	if(res[level][match][missed] != -1)
		return res[level][match][missed];
	
	res[level][match][missed] = 
		min(
			sol(level-1, 2*match, missed) + sol(level-1, 2*match + 1, missed) + price[level][match],
			sol(level-1, 2*match, missed+1) + sol(level-1, 2*match + 1, missed+1) );
	return res[level][match][missed];
}

void solT(int tn)
{
	int p;
	cin>>p;
	REP(i,(1<<p))
		cin>>m[i];
	REP(i,p)
		REP(j,(1<<(p-1-i)))
			cin>>price[i][j];
	FILL(res,-1);
	cout<<"Case #"<<tn<<": "<<sol(p-1,0,0)<<endl;
}

int main()
{
	int N;
	cin>>N;
	REP(i,N)
		solT(i+1);
	return 0;
}