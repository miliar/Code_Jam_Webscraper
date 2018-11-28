#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <bitset>
#include <algorithm>
#include <cstring>
using namespace std;

#define rep(i,a,b) for(int i = (a); i < int(b); ++i)
#define trav(it, v) for (typeof((v).begin()) it = (v).begin(); \
        it != (v).end(); ++it)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define MAX_N 10000

int round = 0;
int used[MAX_N][MAX_N];
bool store[MAX_N][MAX_N];
vector<pii> vines;
int D;
int N;

bool possible(int f, int s) {
    if (used[f][s] == round) return store[f][s];
    if (s == N+1) return true;

    used[f][s] = round;

    // find all vines that are possible to reach
    int r = min(vines[s].first - vines[f].first, vines[s].second);
    rep(i,f+1,N+2) {
        if (vines[i].first <= vines[s].first + r) {
            if (possible(s,i))
                return store[f][s] = true;
        } else break;
    }
    return store[f][s] = false;
}

void solve(int tc) {
    round = tc;
    cin >> N;
    vines.assign(N+2,pii(-1,-1));
    rep(i,0,N) cin >> vines[i+1].first >> vines[i+1].second;
    cin >> D;
    vines[0] = pii(0,1);
    vines[N+1] = pii(D, 1000000000);


    cout << "Case #" << tc << ": " << (vines[1].first != 0 && possible(0,1) ? "YES" : "NO") << "\n";

}

int main() {
    int T;
    cin >> T;
    rep(i,0,T) solve(i+1);
    return 0;
}
