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


#define SZ 60


Int x[SZ],v[SZ];
int n,k;
Int b,t;
void sol(int test)
{
	cin>>n>>k>>b>>t;
	REP(i,n)
		cin>>x[i];
	REP(i,n)
		cin>>v[i];
	int r = 0,tmp=0;
	for(int i = n-1; i>=0; --i)
		if((x[i] + v[i]*t)<b)
			++tmp;
		else
		{
			r += tmp;
			--k;
			if(k == 0)
				break;
		}
	cout<<"Case #"<<test<<": ";
	if(k == 0)
		cout<<r;
	else
		cout<<"IMPOSSIBLE";
	cout<<endl;
}

int main()
{
	int T;
	cin>>T;
	REP(i,T)
		sol(i+1);
	return 0;
}