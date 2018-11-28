/*
 * Author: WHHeV
 * Created Time:  2011/5/7 11:38:43
 * File Name: c.cpp
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

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, N;
    scanf("%d", &T);
    int ca = 0;
    while (T--) {
        ca++;
        int xsum = 0;
        scanf("%d", &N);
        bool b = 0;
        int minn = -1;
        int sum = 0;
        for (int i = 0; i < N; i++) {
            int a;
            scanf("%d", &a);
            if (!b) {
                minn = a;
                b = 1;
            }
            else {
                minn = min(minn, a);
            }
            xsum ^= a;
            sum += a;
        }
        if (xsum == 0)
            printf("Case #%d: %d\n", ca, sum - minn);
        else
            printf("Case #%d: NO\n", ca);
    }
    return 0;
}

