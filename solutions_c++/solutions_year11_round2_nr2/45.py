/*
 * Author: Dumbear
 * Created Time:  2011/5/22 0:26:20
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int t, n, d;
int pos[256], num[256];

void solve();
double get_time();
bool can(double t);

int main() {
    freopen("B.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        solve();
        fprintf(stderr, "%d\n", i);
    }
    return 0;
}

void solve() {
    scanf("%d%d", &n, &d);
    for (int i = 0; i < n; ++i)
        scanf("%d%d", &pos[i], &num[i]);
    printf("Case #%d: %.10lf\n", ++t, get_time());
}

double get_time() {
    double lb = 0, ub = 1e32;
    int cnt = 0;
    while (lb + 1e-10 < ub && ++cnt < 512) {
        double mid = (lb + ub) / 2.0;
        if (can(mid))
            ub = mid;
        else
            lb = mid;
    }
    return (lb + ub) / 2.0;
}

bool can(double t) {
    double cur = -1e64;
    for (int i = 0; i < n; ++i) {
        double x = pos[i] - t, y = pos[i] + t;
        double p = (x > cur + d ? x : cur + d) + (num[i] - 1) * (double)d;
        if (p > y)
            return false;
        cur = p;
    }
    return true;
}
