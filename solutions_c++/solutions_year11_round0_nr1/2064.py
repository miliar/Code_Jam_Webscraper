/*
 * File:   A.cpp
 * Author: yzq110abc
 *
 * Created on 2011年5月7日, 下午9:38
 */

#include <algorithm>
#include <iostream>
#include <utility>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
using namespace std;
typedef pair<int, int> PII;
typedef pair<int, double> PID;
typedef long long LL;

const int MAXN = 1100;
int pos[MAXN], wh[MAXN], n;
char tmp[110];

int Solve() {

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", tmp);
        wh[i] = (tmp[0] == 'O' ? 0 : 1);
        scanf("%d", &pos[i]);
    }
    int x = 1, y = 1, tim = 0;
    int nx = 0, ny = 0;
    while (nx < n && wh[nx] != 0) nx++;
    while (ny < n && wh[ny] != 1) ny++;
    while (nx < n || ny < n) {
        if (nx < ny) {
            int ct = abs(pos[nx] - x);
            x = pos[nx];
            tim += ct + 1;
            if (ny < n) {
                if (pos[ny] > y) {
                    y += ct + 1;
                    y = min(pos[ny], y);
                } else {
                    y -= ct + 1;
                    y = max(pos[ny], y);
                }
            }
            do {
                ++nx;
            } while (nx < n && wh[nx] != 0);
        } else {
            int ct = abs(pos[ny] - y);
            y = pos[ny];
            tim += ct + 1;
            if (nx < n) {
                if (pos[nx] > x) {
                    x += ct + 1;
                    x = min(pos[nx], x);
                } else {
                    x -= ct + 1;
                    x = max(pos[nx], x);
                }
            }
            do {
                ++ny;
            } while (ny < n && wh[ny] != 1);
        }
    }
    printf("%d\n", tim);
    return 0;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++cas);
        Solve();
    }
    return 0;
}
