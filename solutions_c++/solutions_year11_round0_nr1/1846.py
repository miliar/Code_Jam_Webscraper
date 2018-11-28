
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
    deque<pair<int, int> > task;
    deque<int> next[2];

    fup(ca, 1, cas) {
        int n; cin >> n;
        fup(i, 1, n) {
        char a; int b;
        int aa;
        cin >> a >> b;
        if (a == 'O') aa = 0; else aa = 1;
        task.push_back(MP(aa, b));
        next[aa].push_back(b);
        }
        int pos[2];
        pos[0] = pos[1] = 1;
        int moves = 0;
        while (!task.empty()) {
            ++moves;
            int a, b;
            a = task.front().first;
            b = task.front().second;
            bool stay0 = false, stay1 = false;
            if (pos[a] == b) {
                task.pop_front();
                next[a].pop_front();
                if (a == 0) stay0 = 1;
                else stay1 = 1;
            }

            if (!next[0].empty() && !stay0) {
                if (pos[0] < next[0].front()) {
                    pos[0]++;
                }
                if (pos[0] > next[0].front()) {
                    pos[0]--;
                }
            }

            if (!next[1].empty() && !stay1) {
                if (pos[1] < next[1].front()) {
                    pos[1]++;
                }
                if (pos[1] > next[1].front()) {
                    pos[1]--;
                }
            }

        }
        printf("Case #%d: %d\n", ca, moves);

    }

	return 0;
}


