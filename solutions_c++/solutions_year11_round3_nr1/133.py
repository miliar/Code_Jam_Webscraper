
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

char t[55][55];
int h, w;

bool isok(int x, int y) { return x >= 1 && y >= 1 && x <= h && y <= w; }

int main() {
    int cas;
    cin >> cas;
    fup(ca, 1, cas) {
        cin >> h >> w;
        fup(i, 1, h) fup(j, 1, w) cin >> t[i][j];
        bool ok = 1;
        fup(i, 1, h) fup(j, 1, w) {
            if (t[i][j] == '#') {
                if (!isok(i + 1, j + 1)) { ok = 0; break; }
                if (t[i + 1][j] != '#') {ok = 0; break; } else t[i + 1][j] = '\\';
                if (t[i][j] != '#') {ok = 0; break; } else t[i][j] = '/';
                if (t[i][j + 1] != '#') {ok = 0; break; } else t[i][j + 1] = '\\';
                if (t[i + 1][j + 1] != '#') {ok = 0; break; } else t[i + 1][j + 1] = '/';

            }
        }
        printf("Case #%d:\n", ca);
        if (!ok) cout << "Impossible" << endl;
        else {
            fup(i, 1, h) {
                fup(j, 1, w) cout << t[i][j];
                cout << endl;
            }
        }   

    }
	return 0;
}


