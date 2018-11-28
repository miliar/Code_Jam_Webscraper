#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;

//BEGIN TEMPLATE HERE
typedef long long int64;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
//END TEMPLATE HERE

int p[2][105], N[2];
int color[105];
int pos[105];
int n;

int main() {
    freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
    //freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int caseId = 1; caseId <= T; caseId ++) {
        scanf("%d", &n);
        N[0] = N[1] = 0;
        for (int i = 0; i < n; i ++) {
            char s[10];
            scanf("%s%d", s, &pos[i]);
            if (s[0] == 'O') {
                p[0][N[0] ++] = i;
            } else {
                p[1][N[1] ++] = i;
            }
        }
        int ans = 0, L = 0, R = 0, tl = 0, tr = 0, p1 = 1, p2 = 1;
        while (L < N[0] && R < N[1]) {
            int cost;
            if (p[0][L] < p[1][R]) {
                cost = abs(pos[p[0][L]] - p1);
                if (tl + cost <= ans) {
                    ans ++;
                } else {
                    ans = tl + cost + 1;
                }
                tl = ans;
                p1 = pos[p[0][L]];
                L ++;
            } else {
                cost = abs(pos[p[1][R]] - p2);
                if (tr + cost <= ans) {
                    ans ++;
                } else {
                    ans = 1 + tr + cost;
                }
                tr = ans;
                p2 = pos[p[1][R]];
                R ++;
            }
            //cout << ans << endl;
        }
        for (; L < N[0]; L ++) {
            int cost = abs(pos[p[0][L]] - p1);
            if (tl + cost <= ans) {
                ans ++;
            } else {
                ans = 1 + tl + cost;
            }
            tl = ans;
            p1 = pos[p[0][L]];
            //cout << ans << endl;
        }
        for (; R < N[1]; R ++) {
            int cost = abs(pos[p[1][R]] - p2);
            if (tr + cost <= ans) {
                ans ++;
            } else {
                ans = 1 + tr + cost;
            }
            tr = ans;
            p2 = pos[p[1][R]];
            //cout << ans << endl;
        }
        printf("Case #%d: %d\n", caseId, ans);
    }
    return 0;
}

