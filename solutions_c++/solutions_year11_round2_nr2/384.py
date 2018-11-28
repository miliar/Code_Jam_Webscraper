/*

 Email : ahmed.aly.tc@gmail.com

 Codeforces username: ahmed_aly

 TopCoder handle: ahmed_aly

 Google Code Jam tools website: http://ahmed-aly.com/CodeJamTools/

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

#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;

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

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int N;
int n, d;

vi nums;

bool val(double mx) {
	int ind = 1;
	double last = nums[0] - mx;
	while (ind < n) {
		double diff = fabs(last - nums[ind]);
		double new_last = last + d;
		double move = fabs(nums[ind] - new_last);
		if (comp(last, nums[ind]) == -1) {
			if (comp(diff, d) >= 0) {
				move = min(move, mx);
				last = nums[ind] - move;
			} else {
				if (comp(move, mx) > 0)
					return 0;
				last = new_last;
			}
		} else {
			if (comp(move, mx) > 0)
				return 0;
			last = new_last;
		}
		ind++;
	}
	return 1;
}

//#define SMALL
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
		int x, y;
		cin >> n >> d;
		nums.clear();
		rep(i,n) {
			cin >> x >> y;
			rep(j,y)
				nums.pb(x);
		}
		n = sz(nums);
		ll st = 0, en = (ll) 1e13;
		while (st + 1 < en) {
			ll md = (st + en) / 2;
			if (val(md / 2.))
				en = md;
			else
				st = md;
		}
		if (val(st / 2.))
			printf("Case #%d: %.9lf\n", nn, st / 2.);
		else
			printf("Case #%d: %.9lf\n", nn, en / 2.);

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
