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

inline bool inter(const double s1, const double e1, const double s2, const double e2) {
	if(comp(s1,s2) == 0 && comp(e1,e2) == 0)
		return 1;
	if( comp(s1,s2) >0 && comp(s1,e2) < 0)
		return 1;
	if( comp(s2,s1) >0 && comp(s2,e1) < 0)
		return 1;
	return 0;
}


int N;
int n;

#define SMALL
//#define LARGE

int main() {
  freopen("a.txt", "rt", stdin	);
#ifdef SMALL
  freopen("B-small-attempt0.in", "rt", stdin);
  freopen("B-small.out", "wt", stdout);
#endif
#ifdef LARGE
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
#endif

  cin >> N;
  for (int nn = 1; nn <= N; ++nn) {
    printf("Case #%d: ",nn);
    cin >> n;
    double w, l;
    cin >> w >> l;
    vector<double> rr(n), r(n);
    vector<int> ind(n);
    for (int i = 0; i < n; ++i) {
		cin >>  rr[i];
		ind[i] = i;
	}

    //sort(r.begin(),r.end());
    bool done = 0;
    do {
    	for (int tt = 0; tt < n; ++tt) {
			r[tt] = rr[ind[tt]];
		}
    	vector<double> wi, li;
    	wi.push_back(-r[0]);
    	li.push_back(-r[0]);
    	int i;
    	for (i = 1; i < (int) r.size(); ++i) {
    		pair<double, double> cur;
			for(int cw = -1; cw < (int) wi.size(); cw++) {
				if(cw == -1) {
					cur.first = -r[i];
				} else {
					cur.first = wi[cw]+2*r[cw];
				}
				if(cur.first + r[i] - eps > w)
					continue;
				for(int ch = -1; ch < (int) li.size(); ch++) {
					if(ch == -1) {
						cur.second = -r[i];
					} else {
						cur.second = li[ch]+2*r[ch];
					}
					if(cur.second + r[i] - eps > l)
						continue;
					int k;
					for (k = 0; k < i; ++k) {
//						cout << wi[k] << " " << li[k] << " " << r[k] << " vs " << cur.first << " " << cur.second << " " << r[i] << endl;
						double s1 = max(wi[k],cur.first);
						double e1 = min(wi[k]+2*r[k],cur.first+2*r[i]);
						double s2 = max(li[k],cur.second);
						double e2 = min(li[k]+2*r[k],cur.second+2*r[i]);
						if( (comp(s1,e1) < 0 && comp(s2,e2) < 0)) {
//							cout << "intersect" << endl;
							break;
						}
					}
					if(k == (int) wi.size()) {
						wi.push_back(cur.first);
						li.push_back(cur.second);
						goto next;
					}
				}
			}
			break;
			next:

			continue;
		}
    	if(i == (int) r.size()) {
    		for (int k = 0; k < (int) wi.size(); ++k) {
    			if(k)
    				printf(" ");
				printf("%.1lf %.1lf",wi[ind[k]]+r[ind[k]],li[ind[k]]+r[ind[k]]);
			}
    		done = 1;
    		break;
    	}
    } while(next_permutation(ind.begin(),ind.end()));
    if(!done)
    	printf("ERRRRRRRRRRRRRRRROOOOOOOOOOOOOOORRR");
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
