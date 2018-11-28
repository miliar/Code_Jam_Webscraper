/*
 * Author: WHHeV
 * Created Time:  2010/5/22 23:59:22
 * File Name: \Users\WHHeV\Desktop\a.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <cctype>
using namespace std;
#ifdef __DEBUG__
#define dp(fmt, x...) fprintf(stderr, "[%d] " fmt "\n", __LINE__, ##x)
#else
#define dp(fmt, x...)
#endif
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))
#define sqr(x) ((x)*(x))
const int maxint = -1u>>1;
const double pi = acos(-1.0);
const long long maxint64 = 0x7FFFFFFFFFFFFFFFLL;
const double eps = 1e-10;

int T, N, M;
char s[200][100][100];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc, i, j, k, n, ans;
    char tmp1[100], tmp2[100], a, b;
    int len[200];
    scanf("%d", &T);
    for (tc = 1; tc <= T; tc++) {
        memset(len, 0, sizeof(len));
        memset(s, '\0', sizeof(s));
        ans = 0;
        scanf("%d %d", &N, &M);
        a = getchar();
        n = N + M;
        for (i = 0; i < N; i++) {
            j = -1, k = 0;
            //memset(tmp1, '\0', sizeof(tmp1));
            while(scanf("%c", &a) != EOF) {
                if (a == '/') {
                    j++;
                    k = 0;
                } else {
                    if (isalpha(a) || isdigit(a)) {
                        s[i][j][k++] = a;
                    } else {
                        break;
                    }
                }
            }
            len[i] = j + 1;
        }
        for (i = N; i < n; i++) {
            j = -1, k = 0;
            //memset(tmp1, '\0', sizeof(tmp1));
            while(scanf("%c", &a) != EOF) {
                if (a == '/') {
                    j++;
                    k = 0;
                } else {
                    if (isalpha(a) || isdigit(a)) {
                        s[i][j][k++] = a;
                    } else {
                        break;
                    }
                }
            }
            len[i] = j + 1;
            int maxpp = 0;
            for (j = 0; j < i; j++) {
                int pp = 0;
                for (k = 0; k < len[j]; k++) {
                    if (!strcmp(s[i][k], s[j][k]))
                        pp++;
                    else
                        break;
                }
                if (pp > maxpp)
                    maxpp = pp;
            }
            ans += len[i] - maxpp;
        }
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}

