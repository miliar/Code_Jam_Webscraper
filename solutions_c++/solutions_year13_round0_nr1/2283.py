#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

typedef double dbl;
typedef float flt;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define eps 1e-9
#define inf 1000000000
#define infll 1000000000000000000LL
#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define sz(x) ((int)(x).size())
#define intclz(x) __builtin_clz(x)
#define intctz(x) __builtin_ctz(x)
#define intln(x) (32-intclz(x))
#define intbc(x) __builtin_popcount(x)
#define llclz(x) __builtin_clzll(x)
#define llctz(x) __builtin_ctzll(x)
#define llln(x) (64-llclz(x))
#define llbc(x) __builtin_popcountll(x)
#define atbit(x,i) (((x)>>(i))&1)
#define tof(x) __typeof(x)
#define FORab(i,a,b) for (int i=(a); i<=(b); ++i)
#define RFORab(i,a,b) for (int i=(a); i>=(b); --i)
#define FOR1(i,n) FORab(i,1,(n))
#define RFOR1(i,n) RFORab(i,(n),1)
#define FOR(i,n) FORab(i,0,(n)-1)
#define RFOR(i,n) RFORab(i,(n)-1,0)
#define allstl(i,x,t) for (t::iterator i = (x).begin(); i!=(x).end(); ++i)
#define rallstl(i,x,t) for (t::reverse_iterator i = (x).rbegin(); i!=(x).rend(); ++i)
#define begend(x) (x).begin(),(x).end()
#define ms(a,v) memset(a,v,sizeof(a))
#define msn(a,v,n) memset(a,v,n*sizeof(a[0]))
#define mcp(d,s,n) memcpy(d,s,n*sizeof(s[0]))
#define clamp(x,a,b) min(max(x,a),b)

bool check(string s, char c) {
	int cc = 0, tc = 0;
	FOR(i,4) {
		if (s[i]==c) ++cc;
		else if (s[i]=='T') ++tc;
	}
	if (cc+tc==4 and cc>=3) return true;
	return false;
}

int main()
{
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T;
    cin>>T;
    FOR1(cas,T) {
		cout<<"Case #"<<cas<<": ";
		string g[4];
		FOR(i,4) cin>>g[i];

		FOR(i,4) {
			if (check(g[i], 'X')) {
				cout<<"X won"<<endl;
				goto hell;
			}
			if (check(g[i], 'O')) {
				cout<<"O won"<<endl;
				goto hell;
			}
		}

		FOR(i,4) {
			string s;
			FOR(j,4) s += g[j][i];
			if (check(s, 'X')) {
				cout<<"X won"<<endl;
				goto hell;
			}
			if (check(s, 'O')) {
				cout<<"O won"<<endl;
				goto hell;
			}
		}

		{
			string s;
			FOR(i,4) s += g[i][i];
			if (check(s, 'X')) {
				cout<<"X won"<<endl;
				goto hell;
			}
			if (check(s, 'O')) {
				cout<<"O won"<<endl;
				goto hell;
			}
		}

		{
			string s;
			FOR(i,4) s += g[i][3-i];
			if (check(s, 'X')) {
				cout<<"X won"<<endl;
				goto hell;
			}
			if (check(s, 'O')) {
				cout<<"O won"<<endl;
				goto hell;
			}
		}

		FOR(i,4) {
			FOR(j,4) {
				if (g[i][j]=='.') {
					cout<<"Game has not completed"<<endl;
					goto hell;
				}
			}
		}

		cout<<"Draw"<<endl;

	hell:;
	}
    return 0;
}
