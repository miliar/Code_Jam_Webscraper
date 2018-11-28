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

int A[1010];
void solve() {
    int N, L, H;
    scanf("%d %d %d", &N, &L, &H);
    for (int i = 0; i < N; ++i) {
        scanf("%d", A + i);
    }
    for (int i = L; i <= H; ++i) {
        bool ok = true;
        for (int j = 0; j < N; ++j) {
            if (!(A[j] % i == 0 || i % A[j] == 0)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            printf("%d\n", i);
            return ;
        }
    }
    printf("NO\n");
}
int main() {
    freopen("c.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        solve();
    }
    return 0;
}


