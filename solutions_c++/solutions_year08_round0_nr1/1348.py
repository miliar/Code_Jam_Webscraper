/**********************************************************************
Author: momodi
Created Time:  2008-7-17 23:21:19
Modified Time: 2008-7-17 23:55:07
File Name: D:\My Documents\WorkSpace\a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int oo=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
vector<string> dt;
int get_num(char *buf) {
    for (unsigned i = 0; i < dt.size(); ++i) {
        if (dt[i] == buf) {
            return i;
        }
    }
    printf("error");
    return -1;
}
int dp[1010][110];
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n;
        scanf("%d\n", &n);
        dt.clear();
        for (int i = 0; i < n; ++i) {
            char buf[1000];
            gets(buf);
            dt.push_back(buf);
        }
        int m;
        scanf("%d\n", &m);
        if (m == 0) {
            printf("Case #%d: %d\n", t, 0);
        }
        memset(dp, -1, sizeof(dp));
        for (int i = 0; i < m; ++i) {
            char buf[1000];
            gets(buf);
            int k = get_num(buf);
            if (i == 0) {
                for (int j = 0; j < n; ++j) {
                    if (j != k) {
                        dp[0][j] = 0;
                    }
                }
            } else {
                for (int j = 0; j < n; ++j) {
                    if (j != k) {
                        for (int jj = 0; jj < n; ++jj) {
                            if (dp[i - 1][jj] != -1 && (dp[i][j] == -1 || dp[i - 1][jj] + (jj != j) < dp[i][j])) {
                                dp[i][j] = dp[i - 1][jj] + (jj != j);
                            }
                        }
                    }
                }
            }
            if (i == m - 1) {
                int ans = -1;
                for (int j = 0; j < n; ++j) {
                    if (dp[i][j] != -1 && (ans == -1 || dp[i][j] < ans)) {
                        ans = dp[i][j];
                    }
                }
                printf("Case #%d: %d\n", t, ans);
            }
        }
    }
    return 0;
}

