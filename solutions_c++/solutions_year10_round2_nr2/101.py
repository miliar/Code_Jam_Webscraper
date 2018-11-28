/*
 * Author: momodi
 * Created Time:  2010/5/8 21:54:14
 * File Name: b.cpp
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
int X[100], V[100];
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        int N, K, B, T;
        scanf("%d %d %d %d", &N, &K, &B, &T);
        for (int i = 0; i < N; ++i) {
            scanf("%d", X + i);
        }
        for (int i = 0; i < N; ++i) {
            scanf("%d", V + i);
        }
        int ans = 0;
        int add = 0;
        for (int i = N - 1; i >= 0 && K > 0; --i) {
            if ((B - X[i]) <= T * V[i]) {
            ans += add;
                --K;
            } else {
                ++add;
            }
        }
        if (K <= 0) {
            printf("%d\n", ans);
        } else {
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}

