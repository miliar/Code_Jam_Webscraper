/**********************************************************************
Author: chaeyeon
Created Time:  Sat 26 Jul 2008 10:19:34 AM CST
Modified Time: Sat 26 Jul 2008 10:29:55 AM CST
File Name: bb.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(x) printf("%s: %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
vector<pair<int, int> > bear[2100];
int need[2100];
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d:", t);
        int n, m;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < m; ++i) {
            bear[i].clear();
            need[i] = -1;
            int cnt;
            scanf("%d", &cnt);
            while (cnt--) {
                int a, b;
                scanf("%d %d", &a, &b);
                bear[i].push_back(make_pair(a - 1, b));
                if (b == 1) {
                    need[i] = a - 1;
                }
            }
        }
        int flag[2100] = {};
        int ff;
        while (1) {
            ff = true;
            bool changed = false;
            for (int i = 0; i < m; ++i) {
                int ok = false;
                for (unsigned j = 0; j < bear[i].size(); ++j) {
                    if (flag[bear[i][j].first] == bear[i][j].second) {
                        ok = true;
                    }
                }
                if (ok == false) {
                    if (need[i] != -1) {
                        flag[need[i]] = 1;
                        changed = true;
                        continue;
                    }
                    ff = false;
                    break;
                }
            }
            if (!changed) {
                break;
            }
            if (ff == false) {
                break;
            }
        }
        if (ff == false) {
            printf(" IMPOSSIBLE\n");
        } else {
            for (int i = 0; i < n; ++i) {
                printf(" %d", flag[i]);
            }
            printf("\n");
        }
    }
    return 0;
}

