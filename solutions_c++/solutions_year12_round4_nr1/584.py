#include <algorithm>
#include <bitset>
#include <cctype>
#include <cfloat>
#include <climits>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unistd.h>
#include <utility>
#include <vector>
#include <omp.h>

using namespace std;
typedef long long ll;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
template<class T> void clear_vector(vector<T>& v) { vector<T> u; u.swap(v); }

const int TESTCASE = 30;
const int NUMTHREAD = 4;

struct Input {
    int n, d;
    vector<int> ds, len;
    void operator()() {
        int i, j;
        n = getint();
        ds.resize(n);
        len.resize(n);
        for (i = 0; i < n; i++) {
            ds[i] = getint();
            len[i] = getint();
        }
        d = getint();
    }
};

struct Output {
    bool res;
    void operator()(int id) {
        printf("Case #%d: ", id + 1);
        if (res) {
            puts("YES");
        } else {
            puts("NO");
        }
    }
};

struct CaseSolve {
    int n, d;
    vector<int> ds, len;
    vector<int> pos;
    bool res;

    void main(Input* in, Output *out, int test_case) {
        int i, j;
        n = in->n, d = in->d, ds = in->ds, len = in->len;
        pos.assign(n, -1);
        pos[0] = ds[0];
        res = 0;
        for (i = 0; i < n; i++) {
            int dist = pos[i];
            if (dist < 0) continue;
            if (ds[i] + dist >= d) {
                res = 1;
                break;
            }
            for (j = i + 1; j < n; j++) {
                if (ds[i] + dist >= ds[j]) {
                    int tmp = min(ds[j] - ds[i], len[j]);
                    if (tmp <= len[j]) {
                        pos[j] = max(pos[j], tmp);
                    }
                } else {
                    break;
                }
            }
        }
        out->res = res;
        fprintf(stderr, "-->%d done at %d.\n", test_case, omp_get_thread_num());
    }
};

Input in[TESTCASE];
Output out[TESTCASE];
CaseSolve sol[NUMTHREAD];

int main () {
    int i, j, t = getint();
    omp_set_num_threads(NUMTHREAD);


    for (i = 0; i < t; i++) in[i]();
#pragma omp parallel for schedule(dynamic, 1)
    for (i = 0; i < t; i++) sol[omp_get_thread_num()].main(in + i, out + i, i);
    for (i = 0; i < t; i++) out[i](i);
    return 0;
}
