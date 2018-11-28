#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cfloat>
#include <climits>
#include <numeric>
#include <ctime>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> pii;
typedef vector<ll> vll;
typedef vector<ll> vi;
typedef vector<string> vs;

#define sz(c) ll((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORS(i,a,b,s) for (ll i = (a); i < (b); i=i+(s))
#define FORD(i,a,b) for (ll i = ll(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

struct ci {
	int r;
	int x,y;
	int in;

	bool operator< (const ci& o) const {
		return (r>o.r);
	}
};

ci c[1000];

int main() {
	ll tc;
	cin >> tc;
	FOR(ctc,1,tc+1) {
		cout << "Case #" << ctc << ": ";

		int n,w,l;
		cin >> n >> w >> l;
		FOR(i,0,n) {
			cin >> c[i].r;
			c[i].in=i;
		}
		sort(c,c+n);
		int cx = -c[0].r;
		int cy = -c[0].r;
		int mr = 0;
		FOR(i,0,n) {
			if(cx+c[i].r <= w)
			{
				c[i].y = max(cy+c[i].r,0);
				c[i].x = cx+c[i].r;
				cx+=2*c[i].r;
				mr = max(mr,c[i].r);
			} else {
				cx = -c[i].r;
				cy += 2*mr;
				mr = 0;
				i--;
			}
		}
		FOR(i,0,n) {
			FOR(j,0,n) {
				if(c[j].in == i) {
					if(i)
						cout << " ";
					cout << c[j].x << " " << c[j].y;
				}
			}
		}
		cout << endl;
	}
	return 0;
}
