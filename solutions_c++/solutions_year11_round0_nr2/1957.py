/*
 * File:   B.cpp
 * Author: yzq110abc
 *
 * Created on 2011年5月7日, 下午8:11
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

char tmp[110];
bool des[30][30];
int cnt[26], conv[30][30], C, D, N;
vector<int> ans;

inline int hash(char c) {
    return (int)(c - 'A');
}

bool Base(char c) {
    return c == 'A' || c == 'S' || c == 'D' || c == 'F' || c == 'Q' || c == 'W' || c == 'E' || c == 'R';
}

int Solve() {

    memset(conv, -1, sizeof(conv));
    memset(des, false, sizeof(des));
    memset(cnt, 0, sizeof(cnt));
    scanf("%d", &C);
    for (int i = 0; i < C; i++) {
        scanf("%s", tmp);
        int a = hash(tmp[0]), b = hash(tmp[1]), c = hash(tmp[2]);
        if (conv[a][b] != -1) while (1);
        conv[a][b] = c;
        conv[b][a] = c;
    }
    scanf("%d", &D);
    for (int i = 0; i < D; i++) {
        scanf("%s", tmp);
        int a = hash(tmp[0]), b = hash(tmp[1]);
        if (!Base(tmp[0]) || !Base(tmp[1])) while (1);
        des[a][b] = true;
        des[b][a] = true;
    }
    ans.clear();
    scanf("%d", &N);
    scanf("%s", tmp);
    for (int i = 0; i < N; ++i) {
        int now = hash(tmp[i]);
        if (ans.size() == 0) {
            ans.PB(now);
            ++cnt[now];
        } else {
            int top = ans.back();
            if (conv[top][now] != -1) {
                --cnt[top];
                ans.pop_back();
                tmp[i] = conv[top][now] + 'A';
                if (Base(tmp[i])) while (1);
                --i;
            } else {
                bool ff = true;
                for (int j = 0; j < 26; j++) {
                    if (cnt[j] && des[j][now]) {
                        memset(cnt, 0, sizeof(cnt));
                        ff = false;
                        ans.clear();
                        break;
                    }
                }
                if (ff) {
                    ans.PB(now);
                    ++cnt[now];
                }
            }
        }
    }
    putchar('[');
    for (int i = 0; i < ans.size(); i++) {
        if (i > 0) {
            printf(", %c", ans[i] + 'A');
        } else printf("%c", ans[i] + 'A');
    }
    printf("]\n");
    return 0;
}

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++cas);
        Solve();
    }
    return 0;
}
