#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstring>
using namespace std;

int L, D, N;

int ptrs[16 * 5001 * 26], *ptrs_tail;
int *nodes[16 * 5001], node_count;

int Solve(char const* p, int v = 0, int d = 0) {
    if (d == L)
        return 1;
    char const* q = p + 1;
    if (*p == '(') {
        for (; *q != ')'; ++q);
        ++q;
    }
    int r = 0;
    for (; p < q; ++p)
        if ('a' <= *p && *p <= 'z' && nodes[v][*p - 'a'] != -1)
            r += Solve(q, nodes[v][*p - 'a'], d + 1);
    return r;
}

void Insert(char const* p) {
    int v = 0;
    for (int i = 0; i < L; ++i) {
        int t = *p++ - 'a';
        if (nodes[v][t] == -1) {
            int vv = node_count++;
            nodes[vv] = ptrs_tail;
            ptrs_tail += 26;
            nodes[v][t] = vv;
        }
        v = nodes[v][t];
    }
}

int main(int argc, char* argv[]) {
    freopen((string(argv[1]) + ".in").c_str(), "r", stdin);
    freopen((string(argv[1]) + ".out").c_str(), "w", stdout);

    cin >> L >> D >> N;
    {
        memset(ptrs, -1, sizeof(ptrs));
        nodes[0] = ptrs;
        node_count = 1;
        ptrs_tail = ptrs + 26;
    }
    {
        for (int i = 0; i < D; ++i) {
            string s;
            cin >> s;
            Insert(s.c_str());
        }
    }
    {
        for (int i = 0; i < N; ++i) {
            string s;
            cin >> s;
            cout << "Case #" << i + 1 << ": " << Solve(s.c_str()) << endl;
        }
    }
    return 0;
}
