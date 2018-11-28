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

int A[1010000];
long long sum[1010000];
int dist[1010000];
long long solve() {
    int L, N, C;
    long long t;
    scanf("%d %I64d %d %d", &L, &t, &N, &C);
    for (int i = 0; i < C; ++i) {
        scanf("%d", A + i);
    }
    sum[0] = 0;
    for (int i = 0, j = 0; i < N; ++i) {
        dist[i] = A[j];
        j = (j + 1) % C;
        sum[i + 1] = sum[i] + dist[i];
    }
    long long best = sum[N] * 2;
    if (L == 0) {
        return best;
    }
    for (int i = 0; i < N; ++i) {
        if (sum[i + 1] * 2 > t) {
            long long now = sum[N] * 2;
            if (sum[i] * 2 > t) {
                now -= dist[i];
            } else {
                now -= sum[i + 1] - t / 2;
            }
            sort(dist + i + 1, dist + N);
            int LL = L;
            for (int j = N - 1; j >= i + 1; --j) {
                if (--L == 0) {
                    break;
                }
                now -= dist[j];
            }
            get_min(best, now);
            now = sum[N] * 2;
            for (int j = N - 1; j >= i + 1; --j) {
                now -= dist[j];
                if (--LL == 0) {
                    break;
                }
            }
            get_min(best, now);
            break;
        }
    }
    return best;
}
int main() {
    freopen("bb.out", "w", stdout);
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        printf("%I64d\n", solve());
    }
    return 0;
}


