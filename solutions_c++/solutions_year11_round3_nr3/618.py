/*
 * Author: WHHeV
 * Created Time:  2011/5/22 17:43:57
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

int N, L, H;
int a[110];

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int tc = 1;
    while (T--) {
        scanf("%d%d%d", &N, &L, &H);
        for (int i = 0; i < N; i++)
            scanf("%d", &a[i]);
        int ret;
        bool can = 0;
        for (ret = L; ret <= H; ret++) {
            bool flag = true;
            for (int i = 0; i < N; i++) {
                if (ret % a[i] != 0 && a[i] % ret != 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                can = 1;
                break;
            }
        }
        printf("Case #%d: ", tc++);
        if (can)
            printf("%d\n", ret);
        else
            printf("NO\n");
    }
    return 0;
}

