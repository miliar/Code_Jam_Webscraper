/*
 * Author: momodi
 * Created Time:  2009/9/26 23:52:37
 * File Name: a.cpp
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <set>
using namespace std;
#define out(x) fprintf(stderr, "%s: %I64d\n", #x, (long long)(x))
#define SZ(v) ((int)(v).size())
const int maxint=-1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
char dts[100][100];
int dt[100];
int n;
int need[100];
bool can(int k) {
    if (dt[k + 1] > need[k]) {
        return false;
    }
    swap(dt[k], dt[k + 1]);
    need[k] = k;
    need[k + 1] = k + 1;
    return true;
}
int solve() {
    int ans = 0;
    while (true) {
        bool moved = false;
        for (int i = 0; i + 1 < n; ++i) {
            if (dt[i] > need[i]) {
                if (can(i)) {
                    ++ans;
                    moved = true;
                } else {
                    need[i + 1] = need[i];
                }
            }
        }
        if (moved == false) {
            return ans;
        }
    }
}
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cc = 1; cc <= ca; ++cc) {
        printf("Case #%d: ", cc);
        int ans = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", dts[i]);
            dt[i] = -1;
            for (int j = 0; j < n; ++j) {
                if (dts[i][j] == '1') {
                    dt[i] = j;
                }
            }
            need[i] = i;
        }
        printf("%d\n", solve());
    }
    return 0;
}

