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

int N;
int n;

//#define SMALL
#define LARGE

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
		for(int nn = 1; nn <= N ; ++nn) {
        cout << "Case #" << nn << ": ";
        int X, S, R,  N2;
        ld t;
        cin >> X >> S >> R >> t >> N2;
        vector<pair<int, int> > all;
        int prev = 0;
        for (int i = 0; i < N2; ++i) {
          int b,e,w;
          cin >> b >> e >> w;
          if( b > prev )
            all.push_back(make_pair(S,b-prev));
          all.push_back(make_pair(S+w,e-b));
          prev = e;
        }
        if( prev < X )
          all.push_back(make_pair(S,X-prev));
        sort(all.begin(),all.end());
        ld totT = 0;
        R -= S;
        for (int i = 0; i < all.size(); ++i) {
//          cout << all[i].first << " " << all[i].second << endl;
          if( t > 0 ) {
            ld nS = all[i].first + (ld) R;
            ld reqt = all[i].second / nS;
//            cout << reqt << endl;
            if( reqt <= t  ) {
              t -= reqt;
              totT += reqt;
            } else {
              totT += t;
              double distMoved = nS*t;
              t = 0;
              totT += (all[i].second-distMoved)/all[i].first;
            }
          } else {
            totT += ((ld) all[i].second)/all[i].first;
          }
        }
        printf("%.8lf\n",(double)totT);
#ifdef SMALL
        cerr << nn << " of " << N << " is done." << endl;
#endif
#ifdef LARGE
        cerr << nn << " of " << N << " is done." << endl;
#endif
    }
    return 0;
}
