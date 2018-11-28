#define FILENAME "a"

#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <string.h>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define CTO500 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()
#define VI vector<int>
#define VII vector<VI >
#define CL(a,b) memset(a,b,sizeof(a))  
#define UN(v) SORT(v),v.erase(unique(ALL(v)),v.end())  

typedef pair<int, int> PII;
typedef pair<double, PII > PD;
typedef long long i64; 

void init(string file) {
    string ifile = file + ".in";
    string ofile = file + ".out";
	freopen(ifile.c_str(), "rt", stdin);
	freopen(ofile.c_str(), "wt", stdout);
}

bool pred(const PD& x, const PD& y) {
    return x.X < y.X;
}

void solve() {
    int T; cin>>T;
    REP(test,T){
        int x,s,r,n; double t; cin>>x>>s>>r>>t>>n;
        int d = r-s;
        vector<bool> z(x+1);
        vector<PII > a;
        VI w;
        REP(i,n){
            int b,e,v; cin>>b>>e>>v;
            FOR(j,b,e+1){
                z[j] = 1;
            }
            a.pb(PII(e-b, v+s));
            w.pb(b), w.pb(e);
        }
        //REP(i,x+1)cout<<z[i];
        //cout<<endl;
        w.pb(0), w.pb(x);
        SORT(w);
        REP(i,w.sz){
            if (i % 2) continue;
            if (w[i+1] - w[i] > 0) {
                a.pb(PII(w[i+1]-w[i], s));
                //cout << w[i] << " " << w[i+1] << endl;
            }
        }
        vector<PD > o;
        REP(i,a.sz){
            double to = (a[i].X+0.)/a[i].Y;
            double ti = (a[i].X+0.)/(a[i].Y + d);
            double k = (to - ti)/ti;
            o.pb(PD(k, a[i]));
        }
        sort(ALL(o), pred);
        reverse(ALL(o));
        //REP(i,o.sz){
            //cout << o[i].X << " " << o[i].Y.X << " " << o[i].Y.Y << endl;
        //}
        double res = 0;
        REP(i,o.sz){
            //cout << o[i].X << " " << o[i].Y.X << " " << o[i].Y.Y << " ";
            PII k = o[i].Y;
            double vo = k.Y;
            double vi = k.Y + d;
            double to = k.X/vo;
            double ti = k.X/vi;
            double tt = t;
            if (t > ti) t -= ti, res += ti;
            else {
                double s = k.X - t*vi;
                res += t + s/vo;
                t = 0;
            }
            //if (tt > 0) cout << tt << " --> " << t << endl; else cout << endl;
        }
        printf("Case #%d: %.10f\n", test+1, res);
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
