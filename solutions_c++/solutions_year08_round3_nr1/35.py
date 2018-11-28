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
#include <list>
 
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

int main()
{
	freopen("input.in", "r", stdin);
	//freopen("C-small.in", "r", stdin);
	//freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);


	int T;cin>>T;
	REP(test, T)
	{
		int p, k, l;
		cin>>p>>k>>l;
		vector<long long> v;
		REP(i, l)
		{
			int x;
			cin>>x;
			v.pb(x);
		}
		SORT(v);reverse(ALL(v));
		int pos = 0;
		long long now = 0;
		long long res = 0;
		bool fl = true;
		while (pos < v.sz)
		{
			long long sum = 0;
			for (int i = pos; i < MIN(v.sz, pos + k); i++)
				sum += v[i];
			pos += k;
			now++;
			if (now > p)
			{fl = false;break;}
			res += sum*now;
		}
		if (fl)
			cout<<"Case #"<<test+1<<": "<<res<<endl;
		else
			cout<<"Case #"<<test+1<<": "<<"Impossible"<<endl;
	}
	return 0;
}