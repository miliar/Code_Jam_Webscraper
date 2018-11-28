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

Int a[40];


int main()
{
	Int t,n,k;
	REP(i,40)
		a[i] = (1LL<<i)-1;
	cin>>t;
	REP(i,t)
	{
		cin>>n>>k;
		printf("Case #%d: %s\n", i+1,((k&a[n]) == a[n])? "ON":"OFF");
	}
	return 0;
}