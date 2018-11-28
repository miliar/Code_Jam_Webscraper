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

int N, n, ind[1009];
bool vis[1009];

#define SMALL
#define LARGE

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("D-small-attempt2.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("D-large.in", "rt", stdin);
	freopen("D-large.out", "wt", stdout);
#endif
	cin >> N;
	rep2(nn,1,N+1) {
		cin >> n;
		double ret = 0;
		rep2(i,1,n+1)
			cin >> ind[i];
		mem(vis,0);
		rep2(i,1,n+1) {
			if (ind[i] == i || vis[i])
				continue;
			int temp = i;
			while (!vis[temp]) {
				vis[temp] = 1;
				temp = ind[temp];
				ret++;
			}
		}
		printf("Case #%d: %.6lf\n", nn, ret);
#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
