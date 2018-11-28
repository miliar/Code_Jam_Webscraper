#include <iostream>

#include <vector>
#include <string>
#include <map>

#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<long long> vll;

vector<vector<int> > memo;

int f(const vb& op, const vi& val, int V, int pos) {
    if (memo[V][pos] != -1) {
        return memo[V][pos];
    }

    if (2 * pos >= val.size()) {
        if (V != val[pos]) {
            memo[V][pos] = 100000;
            return 100000;
        } else {
            memo[V][pos] = 0;
            return 0;
        }
    }

    int ans = 0;

    int l = 2 * pos;
    int r = l + 1;
    if (V == 0) {
        int a, b, c, d;
        a = f(op, val, 1, l) + f(op, val, 0, r) + (op[pos] ? 0 : (val[pos]==1 ? 1 : 100000));
        b = f(op, val, 0, l) + f(op, val, 1, r) + (op[pos] ? 0 : (val[pos]==1 ? 1 : 100000));
        c = f(op, val, 0, l) + f(op, val, 0, r) + (op[pos] ? 0 : (val[pos]==1 ? 1 : 100000));
        d = f(op, val, 0, l) + f(op, val, 0, r) + (op[pos] ? (val[pos]==1 ? 1 : 100000) : 0);

        ans = min(a, min(b, min(c, d)));
    } else {
        int a, b, c, d;
        a = f(op, val, 1, l) + f(op, val, 1, r) + (op[pos] ? 0 : (val[pos]==1 ? 1 : 100000));
        b = f(op, val, 1, l) + f(op, val, 0, r) + (op[pos] ? (val[pos]==1 ? 1 : 100000) : 0);
        c = f(op, val, 0, l) + f(op, val, 1, r) + (op[pos] ? (val[pos]==1 ? 1 : 100000) : 0);
        d = f(op, val, 1, l) + f(op, val, 1, r) + (op[pos] ? (val[pos]==1 ? 1 : 100000) : 0);

        ans = min(a, min(b, min(c, d)));
    }

    if (ans >= 100000) {
        memo[V][pos] = 100000;
        return 100000;
    } else {
        memo[V][pos] = ans;
        return ans;
    }
}

int solve(const vb& op, const vi& val, int V) {
    memo.resize(2);
    for (int i=0; i<2; ++i) {
        memo[i].resize(val.size());
        for (int j=1; j<val.size(); ++j) {
            memo[i][j] = -1;
        }
    }
    int ans = f(op, val, V, 1);
    return ans;
}

int main(int argc, char* argv[]) {
    int testsNum;
    cin >> testsNum;
    for (int test = 1; test <= testsNum; ++test) {
        int M, V;
        cin >> M >> V;

        vb op((M-1)/2 + 1);
        vi v(M + 1);
        for (int i=1; i<op.size(); ++i) {
            int a;
            cin >> a >> v[i];
            op[i] = (a == 1);
        }
        for (int i=op.size(); i<v.size(); ++i) {
            cin >> v[i];
        }

        int ans = solve(op, v, V);
        cout << "Case #" << test << ": ";
        if (ans >= 100000) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }

    return 0;
}
