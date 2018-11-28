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

#define SZ 1001

Int res;
int r1,k;
int n;
int g[SZ];
int start[SZ];
int tres[SZ];

void read()
{
	cin>>r1>>k>>n;
	REP(i,n)
		cin>>g[i];
}

Int sol()
{
	int r = r1;
	FILL(start,-1);

	Int t = 0;
	REP(i,n)
		t += g[i];

	if(t<=k)//everybody everytime
		return t*r;

	bool was = true;
	int i = 0, cur = 0,cs;
	res = 0;
	while(cur<r)
	{
		if(start[i] != -1 && !was)//cycle
		{
			was = false;
			cs = start[i];
			cur -= cs;
			r -= cs;
			res -= tres[i];
			res *= (r/cur);
			res += tres[i];
			cur = r - (r%cur);
		}
		t = 0;
		while((t+g[i])<=k)
		{
			t += g[i];
			++i;
			if(i == n)
				i = 0;
		}
		res += t;
		cur++;
	}
	return res;
}

int main()
{
	int T,t1,t2;
	cin>>T;
	REP(i,T)
	{
		read();
		cout<<"Case #"<<i+1<<": "<<sol()<<endl;
	}
	return 0;
}