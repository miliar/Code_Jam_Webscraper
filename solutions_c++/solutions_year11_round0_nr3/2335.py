// google_jam.cpp : Defines the entry point for the console application.
//


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

#include <stdio.h>
#include <tchar.h>

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
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
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

#define LARGE

int N,nx;

int _tmain(int argc, _TCHAR* argv[])
{
#ifdef SMALL
	freopen("./data/C-small-attempt0.in", "rt", stdin);
	freopen("./data/C-small-attempt0.out", "wt", stdout);
#endif

#ifdef LARGE
	freopen("./data/C-large.in", "rt", stdin);
	freopen("./data/C-large.out", "wt", stdout);
#endif
	cin >> N;
	for (int nn=1; nn<=N; nn++){
		cout << "Case #" << nn << ": ";
		cin >> nx;
		ll summ=0;
		ll xor_sum=0;
		ll min_ll=0;
		for (int n=0; n<nx; n++){
			ll number;
			cin >> number;
			summ += number;
			xor_sum = xor_sum ^ number;
			if ((min_ll==0) || (min_ll>number))
				min_ll = number;
		}
		if (xor_sum != 0)
			cout << "NO" << endl;
		else
			cout << summ-min_ll << endl;
	}
	return 0;
}

