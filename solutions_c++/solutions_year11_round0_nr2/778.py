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


int t,c,d,n;
string s;
int g[32][32];
bool op[32][32];
vector<int> v;

void init() {
	memset(g,-1,sizeof(g));	
	memset(op,false,sizeof(op));
	v.clear();
}

int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	cin >> t;
	forn(caso,t) {
		init();
		cin >> c;
		forn(i,c) {
			string tmp; cin >> tmp;
			int a = tmp[0]-'A', b = tmp[1]-'A',	c = tmp[2]-'A';
			g[a][b] = g[b][a] = c;	
		}
		
		cin >> d;
		forn(i,d) {
			string tmp; cin >> tmp;	
			int a = tmp[0]-'A', b = tmp[1]-'A';
			op[a][b] = op[b][a] = true;
		}
		
		cin >> n >> s;	
		
	//	cout << c <<  " " << d << " " << n << endl;
		forn(i,n) {
			int now = s[i]-'A';
			if (si(v) == 0) v.pb(now);
			else if (si(v)>0 && g[v.back()][now] != -1) {
				int u = v.back();
				v.pop_back(); v.pb(g[u][now]);
			} else {
				bool explota = false;
				forn(j,si(v)) if (op[v[j]][now]) {
					v.clear();
					explota = true;
					break;	
				}
				if (!explota) v.pb(now);
			}	
		}
		cout << "Case #" << caso+1 << ": [";
		if (si(v)>0) cout << (char)(v[0]+'A');
		forsn(i,1,si(v)) cout << ", " << (char)(v[i]+'A'); 
		cout << "]" << endl;
	}
	
	return 0;
}
