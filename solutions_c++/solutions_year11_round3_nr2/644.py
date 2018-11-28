/*
 * Author: WHHeV
 * Created Time:  2011/5/22 16:50:35
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

int T, C, N, L, t;
int a[1010];
int s[1010];
int ss[1010];
int tt[1010];
int ret[1010];
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    int tc = 1;
    int sum = 0;
    while (T--) {
        scanf("%d%d%d%d", &L, &t, &N, &C);
        for (int i = 0; i < C; i++)
            scanf("%d", &a[i]);
        sum = 0;
        for (int i = 0; i < N; i++) {
            s[i] = a[i % C];
            sum += s[i];
            ss[i] = sum;
            //printf("%d ", s[i]);
        }
        if (L == 0) {
            printf("Case #%d: %d\n", tc++, sum * 2);
            continue;
        }
        if (L == 1) {
            int minn = sum * 2;
            for (int i = 0; i < N; i++) {
                int t1;
                if (i == 0)
                    t1 = 0;
                else
                    t1 = 2 * ss[i-1];
                if (t1 > t) {
                    t1 += s[i];
                } else if (t1 + 2 * s[i] > t) {
                    t1 = t + (s[i] - 0.5 * (t - t1));
                } else {
                    t1 = 2 * ss[i];
                }
                t1 += 2 * (sum - ss[i]);
                if (t1 < minn)
                    minn = t1;
            }
            printf("Case #%d: %d\n", tc++, minn);
        }
        if (L == 2) {
            int minn = sum * 2;
            for (int i = 0; i < N; i++) {
                for (int j = i + 1; j < N; j++) {
                    int t1;
                    if (i == 0)
                        t1 = 0;
                    else
                        t1 = 2 * ss[i-1];
                    if (t1 > t) {
                        t1 += s[i];
                    } else if (t1 + 2 * s[i] > t) {
                        t1 = t + (s[i] - 0.5 * (t - t1));
                    } else {
                        t1 = 2 * ss[i];
                    }
                    t1 += 2 * (ss[j-1] - ss[i]);
                    if (t1 > t) {
                        t1 += s[j];
                    } else if (t1 + 2 * s[j] > t) {
                        t1 = t + (s[j] - 0.5 * (t - t1));
                    } else {
                        t1 = 2 * ss[j];
                    }
                    t1 += 2 * (sum - ss[j]);
                    if (t1 < minn)
                        minn = t1;
                }
            }
            printf("Case #%d: %d\n", tc++, minn);
        }
        //for (int i = 0; i <= N; i++) {
            //for (int j )
        //}
        //tt[0] = 0;
        //memset(ret, 0, sizeof(ret));
        //for (int i = 0; i < N; i++) {
            //tt[i+1] = tt[i] + s[i];
        //}
        //for (int i = 0; i < N; i++) {
            //if (tt[i+1] > b) {
               // 
            //}
        //}
    }
    return 0;
}

