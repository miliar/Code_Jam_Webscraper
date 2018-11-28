#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int n, m;
string str[10005];

int cur;
string comp;

vector<int> V;

bool mycmp(int a, int b) {
    if (cur == -1) {
        if (str[a].size() != str[b].size()) return str[a].size() < str[b].size();
        return a < b;
    }
    int size = str[a].size();
    for (int i = 0; i < size; ++i) {
        if (str[a][i] == comp[cur] && str[b][i] != comp[cur]) return 1;
        if (str[a][i] != comp[cur] && str[b][i] == comp[cur]) return 0;
    }
    return a < b;
}

bool equal(int a, int b, int c) {
    if (c == -1) {
        if (str[a].size() != str[b].size()) return 0;
        return 1;
    }
    int size = str[a].size();
    for (int i = 0; i < size; ++i) {
        if ((str[a][i] == comp[c]) != (str[b][i] == comp[c])) return 0;
    }
    return 1;
}

int f(int a, int b) {
    if (b == -1) return 0;
    for (int i = 0; i < str[a].size(); ++i)
        if (str[a][i] == comp[b])
            return 0;
    return 1;
}

pair<int, int> solve(vector<int> V, int at) {
    if (V.size() == 1) {
        return make_pair(0, V[0]);
    }
    cur = at;
    sort(V.begin(), V.end(), mycmp);
    vector<int> nV;
    int res = 0;
    int idx = 918234;
    int qwe = f(V[0], at);
    if (qwe == 1) return solve(V, at + 1);
    for (int i = 0; i <= V.size(); ++i) {
        if (i == 0 || i == V.size() || !equal(V[i], V[i - 1], at)) {
            if (i > 0) {
                pair<int, int> nres = solve(nV, at + 1);
                int tmp = f(V[i - 1], at);
                if (nres.first + tmp > res || nres.first + tmp == res && idx > nres.second) {
                    res = nres.first + tmp;
                    idx = nres.second;
                }
            }
            nV.clear();
        }
        if (i != V.size()) nV.push_back(V[i]);
    }
    return make_pair(res, idx);
}

int main() {
    freopen("bla.in", "r", stdin);
    freopen("bla.out", "w", stdout);
    int tests;
    scanf("%d", &tests);
    for (int testID = 1; testID <= tests; ++testID) {
        scanf("%d%d", &n, &m);
        V.clear();
        char tmp[30];
        for (int i = 0; i < n; ++i) {
            scanf("%s", &tmp);
            str[i] = tmp;
            V.push_back(i);
        }
        printf("Case #%d:", testID);
        for (int t = 0; t < m; ++t) {
            scanf("%s", &tmp);
            comp = tmp;
            printf(" %s", str[solve(V, -1).second].c_str());
        }
        printf("\n");
    }
    return 0;
}
