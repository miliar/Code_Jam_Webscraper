/**********************************************************************
Author: momodi
Created Time:  2008-7-18 0:05:01
Modified Time: 2008-7-18 0:28:22
File Name: b.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
vector<int> A[1500], B[1500];
int numa[1500], numb[1500];
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        for (int i = 0; i < 1500; ++i) {
            A[i].clear();
            B[i].clear();
        }
        int r;
        scanf("%d", &r);
        int n, m;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; ++i) {
            int a, b;
            scanf("%d:%d", &a, &b);
            int k = a * 60 + b;
            scanf("%d:%d", &a, &b);
            int kk = a * 60 + b;
            A[k].push_back(kk);
        }
        for (int i = 0; i < m; ++i) {
            int a, b;
            scanf("%d:%d", &a, &b);
            int k = a * 60 + b;
            scanf("%d:%d", &a, &b);
            int kk = a * 60 + b;
            B[k].push_back(kk);
        }
        int ansa = 0, ansb = 0;
        memset(numa, 0, sizeof(numa));
        memset(numb, 0, sizeof(numb));
        for (int i = 0; i < 24 * 60; ++i) {
            ansa += max((int)A[i].size() - numa[i], 0);
            numa[i + 1] += max(numa[i] - (int)A[i].size(), 0);
            for (unsigned j = 0; j < A[i].size(); ++j) {
                ++numb[A[i][j] + r];
            }
            ansb += max((int)B[i].size() - numb[i], 0);
            numb[i + 1] += max(numb[i] - (int)B[i].size(), 0);
            for (unsigned j = 0; j < B[i].size(); ++j) {
                ++numa[B[i][j] + r];
            }
        }
        printf("Case #%d: %d %d\n", t, ansa, ansb);
    }
    return 0;
}

