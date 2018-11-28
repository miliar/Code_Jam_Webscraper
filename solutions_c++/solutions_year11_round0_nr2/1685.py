#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

char strA[200][200], strB[200][200], str[200];
int sta[100000];
int top;
int n, m, len;
int mg[50][50], rm[50][50];

void solve() {
    rep(i, 30) rep(j, 30) mg[i][j] = -1;
    rep(i, 30) rep(j, 30) rm[i][j] = 0;

    for (int i = 0; i < n; i++) {
        mg[strA[i][0] - 'A'][strA[i][1] - 'A'] = strA[i][2] - 'A';
        mg[strA[i][1] - 'A'][strA[i][0] - 'A'] = strA[i][2] - 'A';
    }
    for (int i = 0; i < m; i++) {
        rm[strB[i][0] - 'A'][strB[i][1] - 'A'] = 1;
        rm[strB[i][1] - 'A'][strB[i][0] - 'A'] = 1;
    }
    top = 0;
    for (int i = 0; i < len; i++) {
        sta[top++] = str[i] - 'A';
        if (top > 1) {
            if (mg[sta[top - 2]][sta[top - 1]] >= 0) {
                int ch = mg[sta[top - 2]][sta[top - 1]];
                top--;
                top--;
                sta[top++] = ch;
            }
        }
        if (top > 1) {
            for (int j = 0; j < top; j++)
                if (rm[sta[j]][sta[top - 1]]) {
                    top = 0;
                    break;
                }
        }
    }
}

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf(" %s", strA[i]);
        scanf("%d", &m);
        for (int i = 0; i < m; i++) scanf(" %s", strB[i]);
        scanf("%d", &len);
        for (int i = 0;i < len; i++) scanf(" %c", &str[i]);
        solve();
        printf("Case #%d: ", tt + 1);
        printf("[");
        for (int i = 0; i < top; i++) {
            if (i > 0) printf(", ");
            printf("%c", 'A' + sta[i]);
        }
        printf("]\n");
    }
    return 0;
}
