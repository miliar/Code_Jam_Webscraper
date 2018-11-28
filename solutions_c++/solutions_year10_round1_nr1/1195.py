// cj2010r1a_a.cpp
#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

#define rep(i, n) for (int i=0; i<n; i++)
#define repr(i, n) for (int i=n; i>=0; i--)
#define repi(i, n) for (int i=1; i<=n; i++)
#define all(c) c.begin(), c.end()
#define foreach(it, c) for (__typeof(c.begin()) it=c.begin(); it!=c.end(); it++)

#define eq(a, b) ( abs((a)-(b)) < EPS )
#define eqv(a, b) ( eq((a).real(), (b).real()) && eq((a).imag(), (b).imag()) )

#define dd_v(v) { rep(_i, v.size()) cout << v[_i] << " "; cout << endl; }
#define dd_vv(vv) { rep(_i, vv.size()) { rep(_j, vv[_i].size()) cout << vv[_i][_j] << " "; cout << endl; } cout << endl; }
#define dd_c(c) { foreach(_it, c) cout << *_it << " "; cout << endl; }

const int INF = 1<<28;
const double EPS = 1e-10;
const double PI = 3.14159265358979;

typedef complex<double> P;
typedef long long llong;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

typedef int Vertex;
typedef int Weight;
typedef pair<Vertex, Weight> Edge;
typedef vector<Edge> Edges;
typedef map<Vertex, Edges> Graph;
//typedef vector<Edges> Graph;

//#include "../gviz/gviz.h"
//Gviz gviz("../gviz/");

const int dx[] = { 1, 1, 0 };
const int dy[] = { 0, 1, 1 };

int n, k;

vector<string> rotate(const vector<string>& field) {
    vector<string> ret = field;
    rep(i, n) rep(j, n)
	ret[i][j] = field[n-j-1][i];
    return ret;
}

vector<string> fall(const vector<string>& field) {
    vector<string> ret = field;
    repr(i, n-2) rep(j, n) {
	if (ret[i][j]!='.') {
	    int idx = i;
	    while (idx+1<n && ret[idx+1][j]=='.') {
		swap(ret[idx][j], ret[idx+1][j]);
		idx++;
	    }
	}
    }
    return ret;
}

bool match(const vector<string>& field, char ch) {
    rep(i, n) rep(j, n) {
	rep(d, 3) {
	    int px=j, py=i;
	    int cnt = 0;
	    while (0<=px && px<n && 0<=py && py<n && field[py][px]==ch) {
		cnt++;
		px += dx[d]; py += dy[d];
	    }
	    if (cnt == k)
		return true;
	}
    }
    return false;
}

int main()
{
    
    int N, T=0;

    cin >> N;

    while (N--) {
	cin >> n >> k;

	vector<string> field(n);

	rep(i, n)
	    cin >> field[i];

	//dd_vv(field);

	field = rotate(field);

	//dd_vv(field);

	field = fall(field);

	//dd_vv(field);

	bool r = match(field, 'R');
	bool b = match(field, 'B');

	cout << "Case #" << ++T << ": ";

	if (r & b)
	    cout << "Both" << endl;
	else if (r)
	    cout << "Red" << endl;
	else if (b)
	    cout << "Blue" << endl;
	else
	    cout << "Neither" << endl;
    }

    return 0;
}
