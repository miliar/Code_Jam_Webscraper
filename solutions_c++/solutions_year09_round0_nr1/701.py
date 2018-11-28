/**********************************************************************
Author: Xay
Created Time:  2009-9-3 14:41:27
File Name: contest\gcj09\a.cpp
Description: 
**********************************************************************/
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
using namespace std;

const int maxint = 0x7FFFFFFF;
const int maxd = 5000 + 10;
const int maxl = 15 + 2;

int l, d, n;
char s[maxd][maxl];
char str[maxl * 30];
bool used[maxd][30];

bool ok(int x) {
    for (int i = 0; i < l; ++i) {
        if (!used[i][s[x][i] - 'a']) return false;
    }
    return true;
}
int main()
{
    freopen("a.out", "w", stdout);
    while (scanf("%d%d%d", &l, &d, &n) == 3) {
        for (int i = 0; i < d; ++i) {
            scanf("%s", s[i]);
        }
        for (int ca = 1; ca <= n; ++ca) {
            scanf("%s", str);
            int len = 0, next;
            memset(used, 0, sizeof(used));
            for (int i = 0; str[i]; i = next) {
                next = i + 1;
                if (str[i] == '(') {
                    for (; str[next] != ')'; ++next);
                    for (int j = i + 1; j < next; ++j) used[len][str[j] - 'a'] = true;
                    ++next;
                } else {
                    used[len][str[i] - 'a'] = true;
                }
                ++len;
            }
            int ans = 0;
            for (int i = 0; i < d; ++i) {
                if (ok(i)) ++ans;
            }
            printf("Case #%d: %d\n", ca, ans);
        }
    }
    return 0;
}

