// cj2010q_a.cpp
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

int main()
{
    int N, T = 0;

    cin >> N;

    while (N--) {
	int n, k;

	cin >> n >> k;

	int mask = (1<<n) - 1;

	cout << "Case #" << ++T << ": ";
	cout << ( ~(k | ~mask) == 0 ? "ON" : "OFF" ) << endl;
    }

    return 0;
}
