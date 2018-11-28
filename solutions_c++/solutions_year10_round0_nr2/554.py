/*
 * B.cpp
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
#include "BigIntegerLibrary.hh"

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
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;
typedef BigUnsigned bi;

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

int T;
int n;

#define SMALL
//#define LARGE
int main() {
	freopen("test.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt2.in","rt",stdin);
	freopen("B-small2.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	cin >> T;

	int N = 0;
	string si;
	bi gi;
	rep2(nn,1,T+1) {
		vector<bi> vb;
		vector<bi> vt;

		cin >> N;
		printf("Case #%d: ", nn);

		rep(i,N){
			cin >> si;
			gi = stringToBigUnsigned(si);
			vb.pb(gi);
		}

        sort(all(vb));
		rep (i,N){
            rep2 (j,i+1,N){
            	if (vb[j]-vb[i]>0)
					vt.pb(vb[j]-vb[i]);
            }
        }

//		rep (i,vt.sz){
//			cout << vt[i] << " ";
//		}

		bi g = vt[0];
		rep2 (i,1,vt.sz){
			g = min(g,gcd(g,vt[1]));

		}

 //      cout << "g = " << g << endl;
        bi y = 0;
        if (g>1 )
        {
       		y = (vb[0]/g + 1)*g - vb[0];

       		if (y==g)
       			y = 0;
        }

        string sy = bigUnsignedToString(y);


        cout << sy << endl;
	}


	return 0;
}

