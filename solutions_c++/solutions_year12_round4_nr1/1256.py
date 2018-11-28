/*
 * Author: WHHeV
 * Created Time:  2012/5/26 21:53:18
 * File Name: a.cpp
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
#define MAXN 10010
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

struct Node {
    int d, l, f;
} a[MAXN];
int N, D;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, tc;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; ++tc) {
        scanf("%d", &N);
        for (int i = 0; i < N; ++i) {
            scanf("%d%d", &a[i].d, &a[i].l);
            a[i].f = -1;
        }
        scanf("%d", &D);
        //sort(a + 1, a + N);
        if (a[0].l < a[0].d) {
            printf("Case #%d: NO\n", tc);
            continue;
        }
        int po = 0, ll =a[0].d, id = 0;
        bool flag = false;
        a[0].f = a[0].d * 2;
        if (a[0].f >= D) {
            printf("Case #%d: YES\n", tc);
            continue;
        }
        for (int i = 1; i < N; ++i) {
            for (int j = 0; j < i; ++j) {
                if (a[j].f >= a[i].d) {
                    a[i].f = max(a[i].f, a[i].d + min(a[i].d - a[j].d, a[i].l));
                }
            }
            if (a[i].f >= D) {
                flag = true;
                break;
            }
        }
        /*while (true) {
            printf("[%d] [%d] [%d]\n", po, ll, id);
            int dd = po + ll * 2;
            if (dd >= D) {
                flag = true;
                break;
            }
            int maxl = -1, iid = -1, ppo = -1, maxd = -1;
            for (int i = id + 1; i < N; ++i) {
                if (dd < a[i].d)
                    break;
                if (a[i].l >= a[i].d - a[id].d) {
                    if (maxd <= a[i].d - a[id].d + a[i].d) {
                        maxd = a[i].d - a[id].d + a[i].d;
                        //maxl = a[i].d - a[id].d;
                        iid = i;
                        //ppo = a[i].d;
                    }
                } else {
                    if (maxd <= a[i].d + a[i].l) {
                        maxd = a[i].d + a[i].l;
                        iid = i;
                    }
                }
            }
            if (maxd < 0) {
                break;
            }
            if (a[iid].l >= a[iid].d - a[id].d) {
                po = a[id].d;
                ll = a[iid].d - a[id].d;
            } else {
                po = a[iid].d - a[iid].l;
                ll = a[iid].l;
            }
            id = iid;
        }*/
        if (flag) {
            printf("Case #%d: YES\n", tc);
        } else {
            printf("Case #%d: NO\n", tc);
        }
    }
    return 0;
}
