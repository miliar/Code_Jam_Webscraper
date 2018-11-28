#define FILENAME "b"

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
typedef long long i64; 

void init(string file) {
    string ifile = file + ".in";
    string ofile = file + ".out";
	freopen(ifile.c_str(), "rt", stdin);
	freopen(ofile.c_str(), "wt", stdout);
}

void solve() {
    int T; cin>>T;
    int OMGPANDA = 1000010;
    vector<i64> a(OMGPANDA), d(OMGPANDA);
    int cnt[20011];
    REP(test,T){
        int l,n,c; i64 t; cin>>l>>t>>n>>c;
        REP(i,c)cin>>a[i],a[i]*=2;
        FOR(i,c,n+1)a[i]=a[i-c];
        FOR(i,1,n+1)d[i]=d[i-1]+a[i-1];
        CL(cnt,0);
        REP(i,n+1){
            if (d[i] < t) continue;
            if (d[i-1] < t && d[i] > t) ++cnt[d[i]-t];
            else ++cnt[a[i-1]];
        }
        double res = d[n];
        FORD(i,20010,1){
            int allowed = min(cnt[i], l);
            res -= i/2. * allowed;
            l -= allowed;
            //if (cnt[i]) cout << i << " " << cnt[i] << " " << l << endl;
        }
        printf("Case #%d: ", test+1); cout << i64(res) << endl;
    }
}

int main() {
	init(FILENAME);
	solve();
	return 0;
}
