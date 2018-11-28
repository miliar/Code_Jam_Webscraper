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
#include <cstring>
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
#define D(a) cerr << #a << "=" << a << endl;
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

const int MAXC = 256 + 10;
const int MAXN = 100 + 10;

int D,I,M,N,a[MAXN];

int memo[MAXC][MAXN];
int go(int last, int pos) {
	if (pos == N) return 0;
	int& res = memo[last][pos];
	if (res != -1) return res;

	res = go(last,pos+1) + D;
	forn(c,256) if (last == 256 || abs(last - c) <= M) {
		res = min(res,go(c,pos+1) + abs(c-a[pos]));
		res = min(res,go(c,pos) + I);
	}
	return res;
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int ncas; cin >> ncas;
    forn(cas,ncas) {
    	cout << "Case #" << cas+1 << ": ";

    	cin >> D >> I >> M >> N;
    	forn(i,N) cin >> a[i];
    	memset(memo,-1,sizeof memo);
    	cout << go(256,0) << endl;
	}
    return 0;
}
