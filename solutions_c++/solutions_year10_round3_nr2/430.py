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
#include <memory.h> 
#include <iomanip>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n) 
#define pb push_back 
#define sz size() 

#define ALL(c) (c).begin(), (c).end() 
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT((c)), (c).erase(unique(ALL((c))), (c).end())
#define INF 1000000000
#define MAX(a,b) (((a) > (b)) ? (a) : (b))	
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
#define MP(a,b)	 make_pair((a), (b))
#define SQR(a) ((a)*(a))
#define X first
#define Y second

typedef pair<int,int> ii;
typedef vector<int > vi;
typedef vector<vi > vvi;
typedef vector<ii  > vii;
typedef vector<vii  > vvii;
typedef long long ll;
typedef unsigned long long ull;

string filename = "B-large (1)";

ll go(ll l, ll p, ll c){
	if (l*c >= p){
		return 0;
	}
	int cnt = 0;
	ll t = l;
	while (t < p){
		cnt++;
		t *= c;
	}
	ll res = 0;
	ll m = l;
	REP(i, cnt/2)
		m *= c;
	ll r1 = go(m, p, c);
	ll r2 = go(l, m, c);
	res = MAX(r1, r2) + 1;
	m = l;
	REP(i, (cnt+1)/2)
		m *= c;
	r1 = go(m, p, c);
	r2 = go(l, m, c);
	ll res2 = MAX(r1, r2) + 1;
	res = MIN(res, res2);
	return res;
}

int main(){	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	int T;
	cin>>T;
	REP(test, T){
		ll l, p, c;
		cin>>l>>p>>c;
		ll res = go(l, p, c);
		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}


	return 0;
}