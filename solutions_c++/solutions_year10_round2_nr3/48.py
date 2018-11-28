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

string filename = "C-large";

ll mod = 100003;
ll mem[501][501];
ll c[502][502];

ll go(int n, int cnt){
	if (cnt == 0){
		if (n == 1)
			return 1;
		else
			return 0;
	}
	if (cnt >= n)
		return 0;
	if (cnt == 1)
		return 1;
	if (mem[n][cnt] != -1)
		return mem[n][cnt];
	ll& ret = mem[n][cnt];
	ret = 0;
	REP(i, cnt){
		int all = n - cnt - 1;
		int need = cnt - i - 1;
		if (need >= 0 && all >= 0){
			ll r1 = go(cnt, i); 
			r1 *= c[all][need];
			r1 %= mod;
			ret += r1;
			ret %= mod;
		}
	}
	return ret;
}

int main(){	
	string str_fin = filename + ".in", str_fout = filename + ".out";
	freopen(str_fin.c_str(), "r", stdin);		
	freopen(str_fout.c_str(), "w", stdout);

	REP(i, 501){
		c[i][0] = c[i][i] = 1;
		FOR(j, 1, i){
			c[i][j] = (c[i-1][j-1] + c[i-1][j])%mod;
		}
	}
	memset(mem, -1, sizeof(mem));

	int T;
	cin>>T;
	REP(test, T){
		ll n, res = 0;
		cin>>n;
		FOR(i, 1, n){
			res += go(n, i);
			res %= mod;
		}
		cout<<"Case #"<<test+1<<": "<<res<<endl;
	}


	return 0;
}