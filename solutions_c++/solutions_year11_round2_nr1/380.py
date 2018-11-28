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

int N, n;

char mat[109][109];

vii op;

double OWP[109];
double OOWP[109];

#define SMALL
#define LARGE

double getWP(int ind, int ign) {
	double sum = 0;
	double cnt = 0;
	rep(i,n) {
		if (!isdigit(mat[ind][i]) || i == ign)
			continue;
		cnt++;
		if (mat[ind][i] == '1')
			sum++;
	}
	if (cnt == 0)
		return 0;
	return sum / cnt;
}

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif

	cin >> N;
	rep2(nn,1,N+1) {
		printf("Case #%d:\n", nn);
		cin >> n;
		op.clear();
		op.resize(n);
		rep(i,n) {
			cin >> mat[i];
			rep(j,n)
				if (isdigit(mat[i][j]))
					op[i].pb(j);
		}
		rep(i,n) {
			double sum = 0;
			rep(j,sz(op[i]))
				sum += getWP(op[i][j], i);
			if (sz(op[i]))
				OWP[i] = sum / sz(op[i]);
			else
				OWP[i] = 0;
		}
		rep(i,n) {
			double sum = 0;
			rep(j,sz(op[i]))
				sum += OWP[op[i][j]];
			if (sz(op[i]))
				OOWP[i] = sum / sz(op[i]);
			else
				OOWP[i] = 0;
		}
		rep(i,n)
			printf("%.9lf\n", 0.25 * getWP(i, -1) + 0.50 * OWP[i] + 0.25
					* OOWP[i]);

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
