#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>

using namespace std;

#define MP make_pair
typedef pair<int, int> PII;
typedef long long LL;

const int INF = 0x3f3f3f3f;
const int MAXN = 10;
int id[MAXN], r[MAXN];
double ans[MAXN][2];

void solved(int nCase) {
    int N, W, L;
    scanf("%d %d %d", &N, &W, &L);
    for (int i = 0; i < N; ++i) {
        scanf("%d", &r[i]);
        id[i] = i;
    }
    bool flag = false;
    do {
        int mh = 0, np = 0, i;
        for (i = 0; i < N; ) {
            int ch = 0, j = i;
            while (np <= W && i < N) {             
                ans[i][0] = np;
                if (np != 0) {
                    ans[i][0] += r[id[i]];
                    if (ans[i][0] > W) break;
                    ch = max(ch, r[id[i]]);
                    np += 2 * r[id[i++]]; 
                } else {
                    ch = max(ch, r[id[i]]);
                    np += r[id[i++]];   
                }
            }
            for (int k = j; k < i; ++k) {
                ans[k][1] = mh;
                if (j != 0) ans[k][1] += ch;
            }
            np = 0;
            mh += 2 * ch;
            if (mh > L) break;
        }
        if (i == N) {
            flag = true;
        }
    } while (!flag && next_permutation(id, id + N));
    printf("Case #%d:", nCase);
    if (!flag) 
        puts("error");
    else {
        for (int i = 0; i < N; ++i) {
            printf(" %.0lf %.0lf", ans[i][0], ans[i][1]);
        }puts("");
    }
}

int main() {
    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B3.out", "w", stdout);
    int nCase; scanf("%d", &nCase);
    for (int tCase = 1; tCase <= nCase; ++tCase) {
        //printf("Case #%d:", tCase);
        solved(tCase);
    }
    return 0;
}