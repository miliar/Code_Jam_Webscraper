#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define norm(a) sort(all(a)); a.erase(unique(all(a)), a.end());
#define num(a, v) (int)(lower_bound(all(a), v) - a.begin())
#define sqr(a) (a)*(a)

typedef long long int64;
typedef pair<int,int> pii;

const int inf = (int)1E+9;
const double eps = 1e-9;

const string task = "a";
const string inp = task + ".in";
const string oup = task + ".out";

const int nmax = 100100;

long long r,k,n;
long long a[nmax];
long long p[nmax];
long long s[nmax];

void solve(){
	cin >> r >> k >> n;
	forn(i,n)
		cin >> a[i];
	
	forn(i,n){
		s[i] = a[i];
		p[i] = (i+1) % n;
		while (p[i] != i && s[i] + a[p[i]] <= k){
			s[i] += a[p[i]];
			p[i]++;
			if (p[i] >= n) p[i] -= n;
		}
	}
	int now = 0;
	long long res = 0;
	forn(i,r){
		res = res + s[now];
		now = p[now];
	}
	cout << res << endl;
} 

int main(){
	freopen(inp.data(), "rt", stdin);
	freopen(oup.data(),"wt", stdout);

	int tst;
	cin >> tst;
	forn(i,tst){
		printf("Case #%d: ",i+1);
		solve();
	}

	return 0;
}
