/*
 E-Mail : acm.magdi@gmail.com
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

using namespace std;


#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define pb push_back
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

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int R, C;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= R || j >= C)
		return false;
	return true;
}

const int SIZE = 1010;
int N;

//#define SMALL
#define LARGE

int main() {
	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);
#endif
#ifdef LARGE
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
#endif
	int n;
	cin >> N;
	for (int nn = 1; nn <= N; ++nn) {
		scanf("%d", &n);
		char x;
		int y;

		vector<pair<int, int> > seq(0);
		vector<int> o, b;
		for (int i = 0; i < n; ++i) {
			scanf(" %c%d", &x, &y);
			seq.pb(mp(y, x == 'O'));
			if (x == 'O') {
				o.pb(y);
			} else
				b.pb(y);
		}
		int t = 0, Oind = 1, Bind = 1, ib = 0 ,io = 0;
		for (int i = 0; i < seq.size(); ++i) {
			if (seq[i].second == 0)//blue{
			{
				int bmov = abs(Bind - seq[i].first) + 1;
				t += bmov;
				Bind = b[ib] ;
				int od = 0 ;
				if(io < o.size()){
					od = min(abs(o[io] - Oind), bmov);
				if (Oind >= o[io]) {
					Oind -= od;
				} else {
					Oind += od;
				}
				}
				ib++;
			} else {
				int omov = abs(Oind - seq[i].first) + 1;
				Oind = o[io];
				t += omov;
			  //int od = min(abs(o[io] - Oind), bmov);
				int bdis = 0 ;
				if(ib < b.size()){
					bdis = min(abs(b[ib] - Bind), omov);
					if (Bind >= b[ib]) {
						Bind -= bdis;
					} else {
						Bind += bdis;
					}
				}
				io++;
			}
		}
		printf("Case #%d: %d\n" , nn , t);
#ifdef SMALL
		cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
		cerr << nn << " of " << N << " is done." << endl;
#endif
	}
	return 0;
}
