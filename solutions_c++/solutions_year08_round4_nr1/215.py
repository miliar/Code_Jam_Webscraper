/**********************************************************************
Author: momodi
Created Time:  2008-8-3 0:34:11
Modified Time: 2008-8-3 0:46:05
File Name: aa.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

const int maxn = 11000;
int v[maxn];
int oper[maxn];
int can[maxn];

int find(int k, int V) {
    if (v[k] != -1) {
        if (V == v[k]) {
            return 0;
        } else {
            return maxint;
        }
    }
    int ans = maxint;
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
            if (oper[k]) {
                if ((i & j) == V) {
                    get_min(ans, find(k * 2 + 1, i) + find(k * 2 + 2, j));
                }
                if (can[k] && (i | j) == V) {
                    get_min(ans, find(k * 2 + 1, i) + find(k * 2 + 2, j) + 1);
                }
            } else {
                if ((i | j) == V) {
                    get_min(ans, find(k * 2 + 1, i) + find(k * 2 + 2, j));
                }
                if (can[k] && (i & j) == V) {
                    get_min(ans, find(k * 2 + 1, i) + find(k * 2 + 2, j) + 1);
                }
            }
        }
    }
    return ans;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        memset(v, -1, sizeof(v));
        int n, V;
        scanf("%d %d", &n, &V);
        int m = (n - 1) / 2;
        for (int i = 0; i < m; ++i) {
            scanf("%d", oper + i);
            scanf("%d", can + i);
        }
        for (int i = m; i < n; ++i) {
            scanf("%d", v + i);
        }
        int k = find(0, V);
        if (k >= maxint) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", k);
        }
    }
    return 0;
}

