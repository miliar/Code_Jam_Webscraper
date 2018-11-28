/*

 Email : ahmed.aly.tc@gmail.com

 Codeforces username: ahmed_aly

 TopCoder handle: ahmed_aly
 
 Google Code Jam tools website: http://ahmed-aly.selfip.com/CodeJamTools/

 */

#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

int N;

bool ops[26][26];
char com[26][26];

int n;

string s;

#define SMALL
#define LARGE

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
#endif

	cin >> N;
	rep2(nn,1,N+1) {
		cout << "Case #" << nn << ": ";
		rep(i,26)
			rep(j,26) {
				ops[i][j] = 0;
				com[i][j] = ' ';
			}
		cin >> n;
		rep(i,n) {
			cin >> s;
			com[s[0] - 'A'][s[1] - 'A'] = s[2];
			com[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		cin >> n;
		rep(i,n) {
			cin >> s;
			ops[s[0] - 'A'][s[1] - 'A'] = 1;
			ops[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		cin >> n >> s;
		vector<char> ret;
		rep(i,n) {
			if (sz(ret)) {
				char cc = com[ret.back() - 'A'][s[i] - 'A'];
				if (cc != ' ') {
					ret.pop_back();
					ret.pb(cc);
					continue;
				}
			}
			rep(j,sz(ret))
				if (ops[ret[j] - 'A'][s[i] - 'A']) {
					ret.clear();
					goto END;
				}
			ret.pb(s[i]);
			END: ;
		}
		cout << "[";
		rep(i,sz(ret)) {
			if (i)
				cout << ", ";
			cout << ret[i];
		}
		cout << "]" << endl;

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
