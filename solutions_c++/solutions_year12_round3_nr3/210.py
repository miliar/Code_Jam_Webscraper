#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <functional>
#include <sstream>
#include <cassert>
using namespace std;

#pragma comment(linker, "/STACK:56777216")

typedef long long LL;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

typedef pair<LL, int> SItem;
typedef pair< SItem, SItem > State;

LL go(const State& state, const vector< pair<LL, int> >& A, const vector< pair<LL, int> >& B, map<State, LL>& memo) {
    if (memo.count(state)) {
        return memo[state];
    }

    int i = state.first.second;
    int j = state.second.second;
    LL cntA = state.first.first;
    LL cntB = state.second.first;

    if (i < 0 || j < 0) {
        return 0;
    }

    if (state.first.first == 0 && i == 0 && state.second.first == 0 && j == 0) {
        return 0;
    }

    if (A[i].second == B[j].second) {
        LL rem = min(cntA, cntB);

        if (cntA == cntB) {
            LL v1 = i == 0 ? 0 : A[i - 1].first;
            LL v2 = j == 0 ? 0 : B[j - 1].first;

            return memo[state] = go(State(SItem(v1, i - 1), SItem(v2, j - 1)), A, B, memo) + rem;
        } else if (cntA < cntB) {
            LL v1 = i == 0 ? 0 : A[i - 1].first;

            return memo[state] = go(State(SItem(v1, i - 1), SItem(state.second.first - rem, j)), A, B, memo) + rem;
        } else {
            LL v2 = j == 0 ? 0 : B[j - 1].first;

            return memo[state] = go(State(SItem(state.first.first - rem, i), SItem(v2, j - 1)), A, B, memo) + rem;
        }
    } else {
        LL v1 = i == 0 ? 0 : A[i - 1].first;
        LL v2 = j == 0 ? 0 : B[j - 1].first;

        LL ans1 = go(State(SItem(v1, i - 1), state.second), A, B, memo);
        LL ans2 = go(State(state.first, SItem(v2, j - 1)), A, B, memo);
        return memo[state] = max(ans1, ans2);
    }
}

int main() {
#ifndef ONLINE_JUDGE
//    freopen("../DefaultProject/1.txt", "rb", stdin);
    freopen("../DefaultProject/C-large.in", "rb", stdin);
    freopen("../DefaultProject/C-large.out", "wb", stdout);
#endif

    int T;
    scanf("%d", &T);
    rep(tc, T) {
        printf("Case #%d: ", tc + 1);

        int N, M;
        scanf("%d%d", &N, &M);

        vector< pair<LL, int> > A(N), B(M);

        rep(i, N) {
            cin >> A[i].first >> A[i].second;
        }
        rep(i, M) {
            cin >> B[i].first >> B[i].second;
        }

        map<State, LL> memo;

        LL ans = go(State(SItem(A[N - 1].first, N - 1), SItem(B[M - 1].first, M - 1)), A, B, memo);
        stringstream ss;
        ss << ans;
        puts(ss.str().c_str());
    }

    return 0;
}
