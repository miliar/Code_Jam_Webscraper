
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

int n, d;
#define maxn 10005
pair<int, int> t[maxn];
int best[maxn];

int main() {
    int cas;
    cin >> cas;
    fup(c, 1, cas) {
        cin >> n;
        fup(i, 1, n) cin >> t[i].first >> t[i].second;
        cin >> d;
        CLR(best);
        best[1] = t[1].first;
        bool tak = false;

        fup(i, 1, n) {
            //cout << i << " " << best[i] << endl;
            fup(j, i + 1, n) {
                int z = t[j].first - t[i].first;
                int a = best[i];
                if (a >= z) {
                    int x = min(z, t[j].second);
                    best[j] = max(best[j], x);
                }
            }

            if (best[i] + t[i].first >= d) {
                //cout << "TAK " << i << endl;
                tak = true;
            }
        }
        if (tak) printf("Case #%d: YES\n", c);
        else printf("Case #%d: NO\n", c);
    }

	return 0;
}

