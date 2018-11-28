/*
 * C.cpp
 *
 *  Created on: 2010-5-8
 *      Author: wooley
 */

#include <cstring>
#include <string.h>
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

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
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
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
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

ll I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

ll R,k;
int T,N;
int n;

//#define SMALL
#define LARGE
int main() {
	freopen("test.in", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	cin >> T;

	rep2(nn,1,T+1) {
		vll Q;
		vi ts;
		ll gi;
		ll y = 0;
		ll s = 0;
//		ll r = 0;
		ll total = 0;

		cin >> R >> k >> N;
		printf("Case #%d: ", nn);

		rep(i,N){
			cin >> gi;
			total += gi;
			Q.pb(gi);
		}


//		rep (i,N)
//			cout << Q[i] << " ";
//		cout << endl;
//
//		cout << "total = " << total << endl;

		vi indexs;
		int pos = 0;
		indexs.pb(0);

		if (total <= k){
			ts.pb(total);
			goto End;
		}
		for(ll i=0;i<R*N;i++) {
				if (s+Q[i%N] > k){
					ts.pb(s);
					s = Q[i%N];

					rep (q,indexs.sz+1) {
						if (q==(int)indexs.sz) {
							indexs.pb(i%N);
							break;
						}
						else if (i%N==indexs[q]){
							pos = q;
							goto End;
						}
					}
				}
				else{
					s += Q[i%N];
				}
		}
		End:;

//		cout << "ts : ";
//		rep(i,ts.sz)
//		{
//			cout << ts[i] << " ";
//		}
//		cout << endl;
//		cout << "indexs : ";
//		rep(i,indexs.sz)
//		{
//			cout << indexs[i] << " ";
//		}
//		cout << endl;
//
//		cout << "pos = " << pos << endl;

		ll sum = 0;
		rep2(i,pos,ts.sz){
			sum += ts[i];
		}

//		cout << "sum = " << sum <<endl;
//		cout << "R = " << R <<endl;
//		cout << "ts.sz = " << ts.sz <<endl;
//		cout << "(ll)(R-pos)%(ts.sz-pos) = " << (ll)(R-pos)%(ts.sz-pos) <<endl;
		y = sum*((R-pos)/(ts.sz-pos));
//		cout << " y1 = " << y <<endl;

		rep(i,pos){
			y += ts[i];
		}
//		cout << " y2 = " << y <<endl;


		rep(i,(R-pos)%(ts.sz-pos)){
			y += ts[i+pos] ;
		}

		cout << y << endl;
	}

	return 0;
}

