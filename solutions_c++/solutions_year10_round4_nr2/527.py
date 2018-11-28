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
typedef pair<ll, ll> pll;

ll gcd(ll a, ll b){return a == 0 ? b : gcd(b%a, a);}


string filename = "B-large";
//string filename = "test";

ll cost[10000];
int lim[2000];

int n, p;

ll go(int s, int games){
	int index = s - ((1<<(p)) - 1);
	if (index >= 0){
		if (games >= lim[index])
			return 0;
		else
			return -1;
	}else{
		int res0l = go(2*s + 1, games);
		int res0r = go(2*s + 2, games);
		int res0, res1;

		if (res0l == -1 || res0r == -1){
			res0 = -1;
		}else{
			res0 = res0l + res0r;
		}

		

		int res1l = go(2*s + 1, games + 1);
		int res1r = go(2*s + 2, games + 1);

		if (res1l == -1 || res1r == -1){
			res1 = -1;
		}else{
			res1 = res1l + res1r + cost[s];
		}

		if (res0 == -1)
			return res1;
		else if (res1 == -1)
			return res0;
		return MIN(res0, res1);
	}
}

int main(){
	string str_fin = filename + ".in";
	string str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);
	
	int T;
	cin>>T;
	REP(test, T){
		cin>>p;
		memset(cost, 0, sizeof(cost));
		memset(lim, 0, sizeof(lim));
		n = 1<<p;
		REP(i, n){
			cin>>lim[i];
			lim[i] = p - lim[i];
		}
		REP(i, p){
			int shift = (1<<(p-i-1)) - 1;
			int t = 1<<(p - i - 1);
			REP(j, t){
				int x;
				cin>>x;
				cost[shift + j] = x;
			}
		}

		ll res = 0;

		res = go(0, 0);

		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}


	return 0;
}