//-*- coding: utf-8-unix -*-
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
#include <stack>
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

#define dd_v(v) { rep(_i, v.size()) cerr << v[_i] << " "; cerr << endl; }
#define dd_vv(vv) { rep(_i, vv.size()) { rep(_j, vv[_i].size()) cerr << vv[_i][_j] << " "; cerr << endl; } cerr << endl; }
#define dd_c(c) { foreach(_it, c) cerr << *_it << " "; cerr << endl; }
#define dd(v) { cout << "[ " << __LINE__ << ": " << v << " ]" << endl; }

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
        int n; cin >> n;
        vector<pii> v;
        vi vo, vb;
        char c; int p;
        rep(i, n) {
            cin >> c >> p;
            v.push_back(pii(c, p));
            if (c == 'O') vo.push_back(p);
            else vb.push_back(p);
        }
        int time = 0;
        int io = 0, ib = 0;
        int now_o = 1, now_b = 1;
        rep(i, n) {
            //cout << "o: " << now_o << ", b: " << now_b << endl;
            if (v[i].first == 'O') {
                int m = abs(v[i].second - now_o) + 1;
                time += m; now_o = v[i].second;
                if (ib < vb.size()) {
                    int dist = abs(vb[ib] - now_b);
                    if (dist <= m) now_b = vb[ib];
                    else {
                        if (abs(vb[ib] - (now_b + m)) < dist) now_b += m;
                        else now_b -= m;
                    }
                }
                io++;
            }
            else {
                int m = abs(v[i].second - now_b) + 1;
                time += m; now_b = v[i].second;
                if (io < vo.size()) {
                    int dist = abs(vo[io] - now_o);
                    if (dist <= m) now_o = vo[io];
                    else {
                        if (abs(vo[io] - (now_o + m)) < dist) now_o += m;
                        else now_o -= m;
                    }
                }
                ib++;
            }
        }
        cout << "Case #" << ++T << ": " << time << endl;
    }
    
    return 0;
}
