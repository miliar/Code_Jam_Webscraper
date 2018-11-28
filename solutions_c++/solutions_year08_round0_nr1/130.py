#include <algorithm> 
#include <string> 
#include <set> 
#include <map> 
#include <vector> 
#include <queue> 
#include <iostream> 
#include <iterator> 
#include <sstream> 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 
#include <numeric>
 
using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define INF 2147483647
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define X first
#define Y second
#define CLR(a,v) memset((a),(v),sizeof(a)) 

typedef pair<int,int> II;
typedef vector<int> VI;
typedef vector<VI > VVI;
typedef vector<II > VII;
template<typename T>
void outV(const vector<T>& v){cout<<endl;REP(i,v.sz)cout<<v[i]<<" ";cout<<endl;}
template<typename T>
void outVV(const vector<vector<T> >& v){cout<<endl;REP(i,v.sz){REP(j, v[i].sz)cout<<v[i][j]<<" ";cout<<endl;}cout<<endl;}
void outVII(const VII& v){cout<<endl;REP(i,v.sz)cout<<"("<<v[i].first<<", "<<v[i].second<<") ";cout<<endl;}
int gcd(int a,int b){return a==0 ? b : gcd(b%a, a);}


int s, q;
vector<string> engines;
vector<string> queries;

int mem[110][1100];

int go(int eng, int pos)
{
	if (mem[eng][pos] != -1)
		return mem[eng][pos];
	int ret = 100000;

	if (pos == queries.sz)
		return 0;

	if (queries[pos] == engines[eng])
		return ret;

	REP(i, engines.sz)
	{
		int now = go(i, pos+1);
		if (i != eng)
			now++;
		ret = MIN(ret, now);
	}

	mem[eng][pos] = ret;
	return ret;
}


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	cin>>N;
	REP(test, N)
	{
		memset(mem, -1, sizeof(mem));
		engines.clear();
		queries.clear();
		cin>>s;
		cin.get();
		REP(i, s)
		{
			string str;
			getline(cin, str);
			engines.pb(str);
		}

		cin>>q;
		cin.get();
		REP(i, q)
		{
			string str;
			getline(cin, str);
			queries.pb(str);
		}

		int res = 100000;

		REP(i, engines.sz)
		{
			int now = go(i, 0);
			res = MIN(res, now);
		}

		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}
	return 0;
}