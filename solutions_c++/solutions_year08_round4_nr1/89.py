/**********************************************************************
Author: WHU_GCC
Created Time: 2008年08月03日 星期日 00时09分05秒
File Name: gcj_a.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) (cout << #x << ": " << x << endl)
const int maxint = 0x7FFFFFFF;
template <class T> void get_max(T &a, const T &b) {b > a ? a = b : 1;}
template <class T> void get_min(T &a, const T &b) {b < a ? a = b : 1;}

int m, V;

const int maxn = 20010;

int g[maxn];
int c[maxn];
int v[maxn];

int dfs(int i, int t) {
//    printf("i = %d, t = %d\n", i, t);
    if (i > (m - 1) / 2) {
        if (v[i] == t) {
//            printf("node %d, %d = %d\n", i, t, 0);
            return 0;
        }
        else
            return -1;
    }
    int t1[2], t2[2];
    t1[0] = dfs(2 * i, 0), t2[0] = dfs(2 * i + 1, 0);
    t1[1] = dfs(2 * i, 1), t2[1] = dfs(2 * i + 1, 1);
    
//    printf("t1[0] = %d\n", t1[0]);
//    printf("t1[1] = %d\n", t1[1]);
//    printf("t2[0] = %d\n", t2[0]);
//    printf("t2[1] = %d\n", t2[1]);
    
    if (g[i] == 1) {
        int ret = maxint;
        for (int p = 0; p <= 1; p++)
            for (int q = 0; q <= 1; q++) {
                if (t1[p] != -1 && t2[q] != -1 && (p & q) == t) {
                    get_min(ret, t1[p] + t2[q]);
                }
                if (c[i] == 1 && t1[p] != -1 && t2[q] != -1 && (p | q) == t) {
                    get_min(ret, t1[p] + t2[q] + 1);
                }
            }
        if (ret == maxint)
            return -1;
        else {
//            printf("node %d, %d = %d\n", i, t, ret);
            return ret;
        }
    }
    else {
        int ret = maxint;
        for (int p = 0; p <= 1; p++)
            for (int q = 0; q <= 1; q++) {
                if (t1[p] != -1 && t2[q] != -1 && (p | q) == t) {
                    get_min(ret, t1[p] + t2[q]);
                }
                if (c[i] == 1 && t1[p] != -1 && t2[q] != -1 && (p & q) == t) {
                    get_min(ret, t1[p] + t2[q] + 1);
                }
            }
        if (ret == maxint)
            return -1;
        else {
//            printf("node %d, %d = %d\n", i, t, ret);            
            return ret;
        }
    }
}

int main() {
    int ca;
    int T = 1;
    freopen("gcj_a.out", "w", stdout);
    for (scanf("%d", &ca); ca--;) {
        printf("Case #%d: ", T++);
        scanf("%d%d", &m, &V);
        for (int i = 1; i <= (m - 1) / 2; i++) {
            scanf("%d%d", &g[i], &c[i]);
        }
        for (int i = 1; i <= (m + 1) / 2; i++) {
            scanf("%d", &v[i + (m - 1) / 2]);
        }
        int ans = dfs(1, V);
        if (ans == -1)
            printf("IMPOSSIBLE\n"); 
        else
            printf("%d\n", ans);       
    }
    return 0;
}

