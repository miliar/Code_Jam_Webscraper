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

#define MAXL 24
#define MOD 10000
const string msg = "welcome to code jam";

int pref[MAXL];

void init() {
	forn(i,MAXL) pref[i] = 0;
	pref[0] = 1;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cout << setfill('0');

	int ncas; scanf("%d\n",&ncas);
	forsn(cas,1,ncas+1) {
		init();
		string s; getline(cin,s);
		forn(i,si(s)) {
			char c = s[i];
			dforsn(j,0,si(msg)) if (c == msg[j]) {
				pref[j+1] += pref[j];
				pref[j+1] %= MOD;
			}
		}
		cout << "Case #" << cas << ": " << setw(4) << pref[si(msg)] <<endl;
	}
}
