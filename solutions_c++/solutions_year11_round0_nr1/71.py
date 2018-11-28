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

int N, n;

#define SMALL
#define LARGE

int o[109], b[109];
int on, bn;
int nums[109];
char col[109];

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
		cout << "Case #" << nn << ": ";
		cin >> n;
		on = bn = 0;
		rep(i,n) {
			cin >> col[i] >> nums[i];
			if (col[i] == 'O')
				o[on++] = nums[i];
			else
				b[bn++] = nums[i];
		}
		int nextO = 0, nextB = 0;
		int curO = 1, curB = 1;
		int cur = 0;
		int ret = 0;
		while (cur < n) {
			ret++;
			bool oM=0;
			if (nextO < on && curO != o[nextO]) {
				if (o[nextO] < curO)
					curO--;
				else
					curO++;
				oM=1;
			}
			bool bM=0;
			if (nextB < bn && curB != b[nextB]) {
				if (b[nextB] < curB)
					curB--;
				else
					curB++;
				bM=1;
			}
			if (col[cur] == 'O' && curO == nums[cur] && !oM) {
				cur++;
				nextO++;
			}
			else if (col[cur] == 'B' && curB == nums[cur] && !bM) {
				cur++;
				nextB++;
			}
		}
		cout<<ret<<endl;

#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
