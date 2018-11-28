#include <iostream>
#include <cstdio>
#include <bitset>
#include <cstring>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

char a[256][256];
int b[256][256];

int main() {
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int test;
    scanf ("%d\n", &test);
    FOR (test_num, 1, test + 1) {
        int n;
        scanf ("%d", &n);
        gets (a[0]);
        REP (i, 2*n-1) {
            gets (a[i]);
        }
        int qy = 0;
        for (int y = n-1, x = 0; y < 2*n-1; ++y, ++x) {
            REP (qx, n)
                b[qy][qx] = a[y-qx][x+qx]-'0';
            qy++;
        }
        int e, r;
        int ans;
        for (int size = n; ; ++size) {
            REP (q, size-n+1)
                REP (w, size-n+1) {
                    bool ok = true;
                    FOR (yy, q, q + n) FOR (xx, w, w + n) {
                        if (xx >= q && xx < q + n && yy >= w && yy < w+n && b[xx-q][yy-w] != b[yy-q][xx-w]) {
                            ok = false;                            
                            goto out;
                        }
                        if (size-xx-1 >= q && size-xx-1 < q + n && size-yy-1 >= w && size-yy-1 < w+n && b[size-xx-1-q][size-yy-1-w] != b[yy-q][xx-w]) {
                            ok = false;                            
                            goto out;
                        }
                    }              
out:;
                    if (ok) {
                        ans = size*size - n*n;
                        goto output;
                    }          
                }
        }
output:
        printf ("Case #%d: %d\n", test_num, ans);
    }
	return 0;
}
