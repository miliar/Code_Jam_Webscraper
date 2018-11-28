#include <iostream>
#include <cstring>

using namespace std;

int ch[10001];
int type[10001];
int target, m;

inline bool internal(int x) {
    return x <= (m-1) / 2;
}

const int IMP = 20000;

int dp[20000][4];

int go(int node, int target) {
    if (internal(node)) {
        if (dp[node][target] >= 0) return dp[node][target];

        int minLeft0  = go(node*2, 0);
        int minLeft1  = go(node*2, 1);
        int minRight0 = go(node*2 + 1, 0);
        int minRight1 = go(node*2 + 1, 1);
        int best = IMP;
        if (target == 0) {
            int test = minLeft0 + minRight0;
            best <?= test;

            test = minLeft0 + minRight1;
            if (type[node] == 1) best <?= test;
            else if (ch[node]) best <?= (test+1);

            test = minLeft1 + minRight0;
            if (type[node] == 1) best <?= test;
            else if (ch[node]) best <?= (test+1);
        } else {
            int test = minLeft1 + minRight1;
            best <?= test;

            test = minLeft0 + minRight1;
            if (type[node] == 0) best <?= test;
            else if (ch[node]) best <?= (test+1);

            test = minLeft1 + minRight0;
            if (type[node] == 0) best <?= test;
            else if (ch[node]) best <?= (test+1);
        }

        return dp[node][target] = best;
    } else {
        if (target == type[node]) return 0;
        return IMP;
    }
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        memset(dp, 0xff, sizeof(dp));
        cin >> m >> target;
        for (int i = 1; i <= m; i++) {
            cin >> type[i];
            if (internal(i)) cin >> ch[i];
        }
        int res = go(1, target);
        cout << "Case #" << t << ": ";
        if (res >= IMP) cout << "IMPOSSIBLE" << endl; else cout << res << endl;
    }
    return 0;
}


