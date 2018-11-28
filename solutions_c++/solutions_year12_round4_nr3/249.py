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

unsigned int xrand() {
    static unsigned int t, x = 0x12b9b0a1, y = 0x156596fb, z = 0x3270f812, w = 0x138c1fd0;
    t = x ^ x << 11; x = y; y = z; z = w;
    return w = w ^ w >> 19 ^ t ^ t >> 8;
}

#include <sys/time.h>
struct TimeManager {
    typedef unsigned long long ull;
    double sd, tps, d;
    ull sc;
    double get_time() { if (tps) return (tic() - sc) / tps; d = day() - sd; if (d < 0.5) return d; tps = (tic() - sc) / d; return get_time(); }
    void reset() { tps = 0; sd = day(); sc = tic(); }
    ull tic() { unsigned int a, b; __asm__ volatile ("rdtsc" : "=a" (a), "=d" (b)); return a | ((ull)b << 32); }
    double day() { timeval t; gettimeofday(&t, 0); return t.tv_sec + t.tv_usec * 1e-6; }
};

TimeManager timer;

const int TESTCASE = 100;
const int NUMTHREAD = 30;
const double TIME_LIMIT = 60 * 3;

struct Input {
    int n;
    vector<int> idx;
    void operator()() {
        int i, j;
        n = getint();
        idx.resize(n);
        for (i = 0; i < n - 1; i++) {
            idx[i] = getint();
        }
    }
};

struct Output {
    vector<int> res;
    void operator()(int id) {
        printf("Case #%d:", id + 1);
        if (res.empty()) {
            puts(" Impossible");
        } else {
            for (int i = 0; i < res.size(); i++) {
                printf(" %d", res[i]);
            }
            puts("");
        }
    }
};

const int M = 1e9;

struct CaseSolve {
    int n;
    vector<int> idx;
    vector<int> res;
    vector<int> app;
    void main(Input* in, Output *out, int test_case) {
        int i, j;
        n = in->n;
        idx = in->idx;
        res.resize(n);
        app.assign(n, 0);
        for (i = 0; i < n; i++) idx[i]--;
        for (i = 0; i < n; i++) app[idx[i]] = 1;
        for (; ; ) {
            if (timer.get_time() > TIME_LIMIT) {
                res.clear();
                break;
            }
            // res[0] = 0;
            bool ok = 0;
            for (int step = 0; step < 1000; step++) {
                for (i = 0; i < n; i++) {
                    res[i] = xrand() % M + 1;
                }
                ok = 1;
                for (i = 0; i < n; i++) {
                    for (j = i + 1; j < n; j++) if (j != idx[i]) {
                        ll yk = res[j];
                        ll yi = res[i];
                        ll yj = res[idx[i]];
                        ll xk = j;
                        ll xi = i;
                        ll xj = idx[i];
                        if ((yj - yi) * (xk - xi) + yi * (xj - xi) <= yk * (xj - xi)) {
                            ok = 0;
                            break;
                        }
                    }
                }
                if (ok) break;
            }
            if (ok) break;
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
    timer.reset();
    for (i = 0; i < t; i++) in[i]();
#pragma omp parallel for schedule(dynamic, 1)
    for (i = 0; i < t; i++) sol[omp_get_thread_num()].main(in + i, out + i, i);
    for (i = 0; i < t; i++) out[i](i);
    return 0;
}
