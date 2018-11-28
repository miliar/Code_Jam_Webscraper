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

    int c, d, n;
    vector<string> vc, vd;
    string s, ans;
    
    while (N--) {
        cin >> c; vc.assign(c, "");
        rep(i, c) cin >> vc[i];
        cin >> d; vd.assign(d, "");
        rep(i, d) cin >> vd[i];
        cin >> n >> s;
        ans = ""; ans += s[0];
        char prev = s[0];
        repi(i, n-1) {
            char now = s[i];
            int found = 0;
            //cout << "now:" << now << " ans:" << ans << endl;
            rep(j, c) {
                if ((vc[j][0] == prev && vc[j][1] == now) ||
                    (vc[j][0] == now && vc[j][1] == prev)) {
                    ans[ans.size()-1] = vc[j][2];
                    found = 1; break;
                }
            }
            if (!found) {
                int cleared = 0;
                rep(j, d) {
                    found = 0;
                    if (vd[j][0] == now) { found = vd[j][1]; }
                    else if (vd[j][1] == now) { found = vd[j][0]; }
                    if (found) {
                        rep(j, ans.size())
                            if (ans[j] == found) { ans.clear(); cleared = 1; break; }
                        if (cleared) break;
                    }
                }
                if (!cleared) ans += now;
            }
            prev = ans.size() > 0 ? ans[ans.size()-1] : -1;
        }
        cout << "Case #" << ++T << ": [";
        rep(i, ans.size()) cout << ans[i] << (i < ans.size()-1 ? ", " : "");
        cout << "]" << endl;
    }
    
    return 0;
}
