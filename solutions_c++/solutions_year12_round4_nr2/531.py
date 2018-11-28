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

const int TESTCASE = 50;
const int NUMTHREAD = 4;

struct Input {
    int n;
    int width, height;
    vector<double> rad;
    void operator()() {
        int i, j;
        n = getint();
        width = getint();
        height = getint();
        rad.resize(n);
        for (i = 0; i < n; i++) {
            rad[i] = getint();
        }
    }
};


struct Output {
    vector<double> resx, resy;
    void operator()(int id) {
        printf("Case #%d:", id + 1);
        for (int i = 0; i < resx.size(); i++) {
            printf(" %.10f %.10f", resx[i], resy[i]);
        }
        puts("");
    }
};

double get_dist(double x1, double x2, double y1, double y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

struct CaseSolve {
    int n;
    int width, height;
    vector<double> rad;
    vector<double> resx, resy;
    void main(Input* in, Output *out, int test_case) {
        int i, j;
        n = in->n, width = in->width, height = in->height, rad = in->rad;

        double px = 0, py = 0;
        resx.resize(n);
        resy.resize(n);
        for (; ; ) {

            bool ok = 1;
            for (i = 0; i < n; i++) {
                resx[i] = xrand() % (int)1e9 / 1e9 * width;
                resy[i] = xrand() % (int)1e9 / 1e9 * height;
            }

            for (i = 0; i < n; i++) for (j = i + 1; j < n; j++) {
                if (get_dist(resx[i], resx[j], resy[i], resy[j]) <= rad[i] + rad[j]) {
                    ok = 0;
                    break;
                }
            }
            if (ok) break;
        }

        out->resx = resx;
        out->resy = resy;

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
