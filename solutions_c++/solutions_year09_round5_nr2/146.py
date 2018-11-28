#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define MOD 10009
#define MAXN 102
#define MAXL 30

struct state {
	int v[5];
};

bool operator<(const state& s1, const state& s2) {
	forn(i,5) if (s1.v[i] < s2.v[i]) return true;
	return false;
}

bool operator==(const state& s1, const state& s2) {
	forn(i,5) if (s1.v[i] != s2.v[i]) return false;
	return true;
}



int n, cnt[MAXN][MAXL], term[4];

map<vi,int> memo;
int go(vi v) {
	if (memo.count(v)) return memo[v];
	if (v[4] == 0) {
		int res = 1; forn(i,4) if (term[i] != 29){ res *= v[i]; res %= MOD; };
		return memo[v] = res;
	}
	int res = 0;
	v[4]--;
	forn(i,n) {
		forn(j,4) v[j] += cnt[i][term[j]];
		res += go(v); res %= MOD;
		forn(j,4) v[j] -= cnt[i][term[j]];
	}
	v[4]++;
	return memo[v] = res;
}

void init() {
	forn(i,n) forn(j,MAXL) cnt[i][j] = 0;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int ncas; cin >> ncas;
	forsn(cas,1,ncas+1) {
		init();
		string s; int k; cin >> s >> k; s += '+';
		cin >> n;
		forn(i,n) {
			string s; cin >> s;
			forn(j,si(s)) cnt[i][s[j]-'a']++;
		}

		int res[11]; forn(i,11) res[i] = 0;
		int ind = 0;
		while (ind < si(s)) {
			forn(i,4) {
				if (s[ind] == '+') term[i] = 29;
				else {
					term[i] = s[ind]-'a';
					ind++;
				}
			}
			ind++;

			memo.clear();
			vi v(5,0);
			forn(i,k) {
				v[4] = i+1;
				res[i] += go(v);
				res[i] %= MOD;
			}
		}

		cout << "Case #" << cas << ": ";
		forn(i,k) {
			if (i) cout << ' ';
			cout << res[i];
		}
		cout << endl;
	}
}
