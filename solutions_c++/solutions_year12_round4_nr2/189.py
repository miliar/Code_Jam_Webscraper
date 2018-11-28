
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

int w, l;
vector<pair<int, int> > r;
lli dist(lli x1, lli y1, lli x2, lli y2) {
    return SQR(x1 - x2) + SQR(y1 - y2);
}

int n;
vector<pair<int, int> > tryit(int pp) {
vector<pair<int, int> > gdzie;
    fup(i, 0, siz(r) - 1) {
        //cout << i << endl;
        int x, y;
        while (pp) {
            pp--;
            x = rand() % (w + 1);
            y = rand() % (l + 1);
            if (i == 0) { x = 0; y = 0; }
            bool ok = true;
            fup(j, 0, i - 1) {
                lli u = dist(gdzie[j].first, gdzie[j].second, x, y);
                lli d2 = r[i].first + r[j].first;
                if (u <= d2 * d2) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                //cout << i << " " << x << " " << y << endl;
                gdzie.PB(MP(x, y));
                break;
            }
        }
    }
    if (siz(gdzie) == siz(r)) {
        return gdzie;
    } else {
        gdzie.clear();
        return gdzie;
    }
}

pair<int, int> G[1005];

int main() {
    int cas;
    cin >> cas;
    fup(c, 1, cas) {
    r.clear();
    cin >> n >> w >> l;
    fup(i, 1, n) {
        int x; cin >> x;r.PB(MP(x, i - 1));
    }
    sort(ALL(r));
    reverse(ALL(r));
    vector<pair<int, int> > gdzie;
    //debugv(r);
    while (true) {
//        cout << "TTT" << endl;
        gdzie = tryit(100000);

        if (!gdzie.empty()) break;
    //    break;
    }

    fup(i, 0, siz(r) - 1) {
        G[r[i].second] = gdzie[i];
    }

    
        printf("Case #%d:", c);
        fup(i, 0, siz(r) - 1) {
                cout << " " << G[i].first << " " << G[i].second;
        }
        //FORE(it, gdzie) cout << " " << it -> first << " " << it -> second;
        cout << endl;
    }



	return 0;
}

