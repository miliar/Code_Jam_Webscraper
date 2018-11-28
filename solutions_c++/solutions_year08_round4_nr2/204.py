/**********************************************************************
Author: momodi
Created Time:  2008-8-3 0:30:49
Modified Time: 2008-8-3 1:13:46
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        int n, m, a;
        scanf("%d %d %d", &n, &m, &a);
        int flag = false;
        for (int i = 0; i <= n && flag == false; ++i) {
            for (int j = 0; j <= m && flag == false; ++j) {
                for (int ii = 0; ii <= n && flag == false; ++ii) {
                    for (int jj = 0; jj <= m && flag == false; ++jj) {
                        if (abs(i * jj - j * ii) == a) {
                            flag = true;
                            printf("%d %d %d %d %d %d\n", 0, 0, i, j, ii, jj);
                        }
                    }
                }
            }
        }
        if (flag == false) {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}

