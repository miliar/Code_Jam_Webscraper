#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"

using namespace std;

void solve(int i, vector<int> const& v, vector<int> paul, vector<int> sean, int &value)
{
    if (i == v.size()) {
        if (sean.size() == 0 || paul.size() == 0) return;
        int ss = 0, ps = 0;
        int srs = 0, prs = 0;
        for (int j = 0; j < sean.size(); ++j) {
            ss ^= sean[j];
            srs += sean[j];
        }
        for (int j = 0; j < paul.size(); ++j) {
            ps ^= paul[j];
            prs += paul[j];
        }
        if (ss == ps) {
            value = max(value,max(srs,prs));
        }
        return;
    }
    paul.push_back(v[i]);
    solve(i+1, v, paul, sean, value);
    paul.pop_back();
    sean.push_back(v[i]);
    solve(i+1, v, paul, sean, value);
}

int main() {
    int T; scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        int N; scanf("%d", &N);
        vector<int> v(N);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &v[i]);
        }
        int m = -1;
        vector<int> paul, sean;
        solve(0, v, paul, sean, m);
        if (m == -1)
            printf("Case #%d: NO\n", Ti);
        else
            printf("Case #%d: %d\n", Ti, m);
    }
    return 0;
}

