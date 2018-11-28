#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

typedef struct {
    int b,e,w;
}nd;

bool operator < (nd a, nd b) {
    return a.b < b.b;
}

bool cmp(nd a, nd b) {
    return a.w < b.w;
}

nd node[13100];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int ff = 0;
    while (T--) {
        int X, S, R, t;
        int N;
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        int sum = X;
        for (int i = 0; i < N; ++i) {
            scanf("%d%d%d", &node[i].b, &node[i].e, &node[i].w);
        }
        sort(node, node + N);
        int len = N;
        node[len].b = 0;
        node[len].e = node[0].b;
        node[len].w = 0;
        ++len;
        for (int i = 1; i < N; ++i) {
            node[len].b = node[i - 1].e;
            node[len].e = node[i].b;
            node[len].w = 0;
            ++len;
        }
        node[len].b = node[N - 1].e;
        node[len].e = X;
        node[len].w = 0;
        ++len;
        sort(node, node + len, cmp);
        double ret = 0;
        double rd = t;
        for (int i = 0; i < len; ++i) {
            double lens = node[i].e - node[i].b;
            if (node[i].w + S < node[i].w + R) {
                if (lens * 1.0 / (R + node[i].w) < rd) {
                    rd -= lens * 1.0 / (node[i].w + R);
                    ret += lens * 1.0 / (node[i].w + R);
                } else {
                    lens -= rd * (node[i].w + R);
                    ret += rd;
                    rd = 0;
                    ret += lens * 1.0 / (node[i].w + S);
                }
            } else {
                ret += lens * 1.0 / (node[i].w + S);
            }
        }
        ++ff;
        printf("Case #%d: ", ff);
        printf("%.7lf\n", ret);
    }
    return 0;
}
