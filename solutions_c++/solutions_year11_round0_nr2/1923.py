#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <iostream>
#include <ctime>
using namespace std;
#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,a,b) for(int i=a;i<b;++i)
#define sz size()
#define pb(x) push_back(x)
typedef long long LL;
const int N = 1001;


int n, m;
char s[41][5];
char ss[41][5];
char str[200], ans[200];
int len;

int solve() {
    int top = -1;
    for (int i = 0; i < len; ++i) {
        ans[++top] = str[i];
        if (top >= 1) {
            bool flag =true;
            while (top >= 1 && flag ==true) {
                flag = false;
                for (int j = 0; j < n ; ++j)
                    if (ans[top] == s[j][0] && ans[top - 1] == s[j][1]) {
                        ans [--top] = s[j][2];
                        flag =true;
                    } else if (ans[top] == s[j][1] && ans[top - 1] == s[j][0]) {
                        ans [--top] = s[j][2];
                        flag = true;
                    }
            }
            for (int j = 0; j < m && top >= 1; ++j)
                if (ans[top] == ss[j][0]) {
                    for (int k = top - 1; k >= 0; --k)
                        if (ans[k] == ss[j][1]) {
                            top = -1;
                            break;
                        }
                    if (top == -1) break;
                } else if (ans[top] == ss[j][1]) {
                    for (int k = top - 1; k >= 0; --k)
                        if (ans[k] == ss[j][0]) {
                            top = -1;
                            break;
                        }
                    if (top == -1) break;
                }
        }
    }

    printf("[");
    for (int i = 0; i <= top; ++i) {
        if (i) printf(", ");
        putchar(ans[i]);
    }
    printf("]\n");
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("outB.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 1; i <= cas; ++i) {
        scanf("%d", &n);
        for (int j = 0; j < n; ++j)
            scanf("%s", s[j]);
        scanf("%d", &m);
        for (int j = 0; j < m; ++j)
            scanf("%s", ss[j]);
        scanf("%d%s", &len, str);
        printf("Case #%d: ", i);
        solve();
    }
}
