/*
 * Author: momodi
 * Created Time:  2010/5/8 19:00:54
 * File Name: a.cpp
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
#define take(a, b) (((a) >> (b)) & 1)
#define move(v) (1 << (v))

void solve(int n, int k) {
    int f = 0;
    while (k--) {
        for (int i = 0; i < n; ++i) {
            if (take(f, i) == 0) {
                f ^= move(i);
                break;
            } else {
                f ^= move(i);
            }
        }
    }
    for (int i = 0; i + 0 < n; ++i) {
        if (take(f, i) == 0) {
            puts("OFF");
            return ;
        }
    }
    puts("ON");
}

int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        int n, k;
        scanf("%d %d", &n, &k);
        solve(n, k);
    }
    return 0;
}

