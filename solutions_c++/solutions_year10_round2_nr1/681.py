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

int res;
struct dir
{
	map<string,dir> x;
	void insert(char *s)
	{
		if(*s == '\0')
			return;
		++s;
		string name;
		while(*s != '\0' && *s != '/')
		{
			name += *s;
			++s;
		}
		if(x.find(name) == x.end())
			++res;
		x[name].insert(s);
	}
	void clear()
	{
		x.clear();
	}
};

dir root;
	int n,m;
	char buf[200];

void sol(int test)
{
	root.clear();
	gets(buf);
	sscanf(buf, "%d%d", &n, &m);
	REP(i, n)
	{
		gets(buf);
		root.insert(buf);
	}
	res = 0;
	REP(i, m)
	{
		gets(buf);
		root.insert(buf);
	}
	cout<<"Case #"<<test<<": "<<res<<endl;
}

int main()
{
	int T;
	gets(buf);
	sscanf(buf, "%d", &T);
	REP(i,T)
		sol(i+1);	
	return 0;
}