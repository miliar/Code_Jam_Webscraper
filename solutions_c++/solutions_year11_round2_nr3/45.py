/*
 * Author: Dumbear
 * Created Time:  2011/5/22 0:50:27
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << enddl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int t, n, m, start[10], endd[10], best, color[10], col[10];
vector<int> pol[10];

void solve();
void get_num(int d);
void check();

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; ++i) {
        scanf("%d", &start[i]);
        --start[i];
    }
    for (int i = 0; i < m; ++i) {
        scanf("%d", &endd[i]);
        --endd[i];
    }
    int cnt = 0;
    vector<int> tmp;
    for (int i = 0; i < n; ++i)
        tmp.push_back(i);
    pol[cnt++] = tmp;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < cnt; ++j) {
            int k1 = -1, k2 = -1;
            for (int k = 0; k < pol[j].size(); ++k) {
                if (pol[j][k] == start[i])
                    k1 = k;
                if (pol[j][k] == endd[i])
                    k2 = k;
            }
            if (k1 != -1 && k2 != -1) {
                vector<int> a, b;
                for (int k = k1; ; k = (k + 1) % pol[j].size()) {
                    a.push_back(pol[j][k]);
                    if (k == k2)
                        break;
                }
                for (int k = k2; ; k = (k + 1) % pol[j].size()) {
                    b.push_back(pol[j][k]);
                    if (k == k1)
                        break;
                }
                pol[j] = a;
                pol[cnt++] = b;
                break;
            }
        }
    }
    m = cnt;
    //for (int i = 0; i < m; ++i) {
        //for (int j = 0; j < pol[i].size(); ++j)
            //printf("%d ", pol[i][j]);
        //puts("");
    //}
    best = 0;
    get_num(0);
    printf("Case #%d: %d\n", ++t, best);
    for (int i = 0; i < n; ++i)
        printf((i == n - 1 ? "%d\n" : "%d "), color[i]);
}

void get_num(int d) {
    if (d == n) {
        check();
        return;
    }
    if (d == 0) {
        col[d] = 1;
        get_num(d + 1);
    } else {
        for (int i = 1; i <= 8; ++i) {
            col[d] = i;
            get_num(d + 1);
        }
    }
}

void check() {
    bool f[10] = {};
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        if (!f[col[i]]) {
            ++cnt;
            f[col[i]] = true;
        }
    }
    if (cnt <= best)
        return;
    //int ans[] = {1, 2, 3, 1, 1, 3, 2, 3};
    //for (int i = 0; i < n; ++i)
        //if (ans[i] != col[i])
            //return;
    for (int i = 0; i < m; ++i) {
        bool ff[10] = {};
        int c = 0;
        for (int j = 0; j < pol[i].size(); ++j) {
            if (!ff[col[pol[i][j]]]) {
                ++c;
                ff[col[pol[i][j]]] = true;
            }
        }
        if (c != cnt)
            return;
    }
    best = cnt;
    memcpy(color, col, sizeof(col));
}
