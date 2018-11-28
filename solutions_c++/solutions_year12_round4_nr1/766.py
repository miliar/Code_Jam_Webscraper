/*
 E-Mail : amr.9102@gmail.com
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

#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
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
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-10;

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

int N;
int n;

#define MX 10010
vector<pair<int,int> > vine;
int d[MX], l[MX];
vector<int> b;
int mxD;

//#define SMALL
#define LARGE

int main() {
  freopen("a.txt", "rt", stdin	);
#ifdef SMALL
  freopen("A-small-attempt0.in", "rt", stdin);
  freopen("A-small.out", "wt", stdout);
#endif
#ifdef LARGE
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
#endif

  cin >> N;
  for (int nn = 1; nn <= N; ++nn) {
    printf("Case #%d: ",nn);
    cin >> n;
    mxD = 0;
    vine.clear();
    b.clear();
    for(int i =0 ; i < n; ++i) {
    	pair<int,int> p;
    	cin >> p.first >> p.second;
    	if(i && p.first <= vine[0].first)
    		continue;
    	vine.push_back(p);
    	b.push_back(-1);
    }
    sort(vine.begin(),vine.end());

    for (int i = 0; i < vine.size(); ++i) {
		d[i] = vine[i].first;
		l[i] = vine[i].second;
	}
    b[0] = d[0];
    for(int i = 0 ; i < vine.size() ; ++i) {
    	//cout << d[i] << " " << l[i] << " " << b[i] << endl;
    	if(b[i] == -1)
    		break;
    	mxD = max(mxD, d[i]+b[i]);
    	for(int j = i+1; j < vine.size() && d[i]+b[i] >= d[j] ; ++j) {
    		b[j] = max(b[j],min(d[j]-d[i], l[j]));
    	}
    }
    int D;
    cin >> D;
    if(mxD >= D)
    	printf("YES");
    else
    	printf("NO");
    printf("\n");
#ifdef SMALL
    cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
    cerr << nn << " of " << N << " is done." << endl;
#endif
  }
  return 0;
}
