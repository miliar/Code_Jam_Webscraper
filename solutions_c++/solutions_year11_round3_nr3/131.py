
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBU true
#define debug(x) { if (DEBU) cerr << #x << " = " << x << "\n"; }
#define debugv(x) { if (DEBU) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; } }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;


int main() {
    int cas;
    cin >> cas;
    fup(ca, 1, cas) {
        vector<lli> t;
        int n, l, h;
        cin >> n >> l >> h;
        fup(i, 1, n) { int a; cin >> a; t.push_back(a); }
        int x = 0;
        fup(i, l, h) {
            bool ok = 1;
            FORE(it, t) {
                if (i % (*it) == 0 || (*it) % i == 0); else { ok = 0; break;}
            }
            if (ok) { x = i; break; }
        }
        printf("Case #%d: ", ca);
        if (x == 0) cout << "NO" << endl;
        else cout << x << endl;

    }
	return 0;
}


