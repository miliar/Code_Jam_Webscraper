/* Trân Vu Lâm */
/*             */
/*             */
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <cstring>
#include <set>
#include <math.h>
#include <map>
#include <stack>
#include <queue>

#define ii pair<int, int>
#define si pair<string, int>
#define is pair<int, string>

#define mp make_pair
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pbp(a,b) push_back(make_pair(a,b))
#define insp(a,b) insert(make_pair(a,b))
#define pb(a) push_back(a)
#define ins(a) insert(a)

#define uint64 unsigned long long
#define int64 long long

#define INF 1071071071
#define Pr 9875321
#define pi 3.1415926535897932384626433832795
#define eps 1e-8
#define maxN 5

using namespace std;

char s[maxN][maxN];

bool dia(char c) {
    int cnt = 0, m = 0;
    for (int i = 0; i < 4; i++)
        if (s[i][i] == 'T' || s[i][i] == c) {
            cnt++;
            if (s[i][i] == c)
                m++;
        }
    if (cnt == 4 && m > 0) return true;
    cnt = 0, m = 0;
    for (int i = 0; i < 4; i++)
        if (s[i][3 - i] == 'T' || s[i][3 - i] == c) {
            cnt++;
            if (s[i][3 - i] == c)
                m++;
        }
    if (cnt == 4 && m > 0) return true;
    return false;
}

bool row(char c) {
    for (int i = 0; i < 4; i++) {
        int cnt = 0, m = 0;
        for (int j = 0; j < 4; j++)
            if (s[i][j] == 'T' || s[i][j] == c) {
            cnt++;
            if (s[i][j] == c)
                m++;
        }
        if (cnt == 4 && m > 0)
            return true;
    }
    return false;
}
bool col(char c) {
    for (int i = 0; i < 4; i++) {
        int cnt = 0, m = 0;
        for (int j = 0; j < 4; j++)
            if (s[j][i] == 'T' || s[j][i] == c) {
            cnt++;
            if (s[j][i] == c)
                m++;
        }
        if (cnt == 4 && m > 0)
            return true;
    }
    return false;
}
int main(void) {
    freopen("A-large.in", "r", stdin);
    freopen("A.OUT", "w", stdout);
    int tcs;
    cin>>tcs;
    for (int tcNo = 1; tcNo <= tcs; tcNo++) {
        for (int i = 0; i < 4; i++)
            scanf("%s", s[i]);
        bool full = true;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (s[i][j] == '.') {
                    full = false;
                    break;
                }
        bool x = dia('X') || row('X') || col('X');
        bool o = dia('O') || row('O') || col('O');
        if (x && o)
            printf("Case #%d: Draw\n", tcNo);
        else if (x) printf("Case #%d: X won\n", tcNo);
            else if (o) printf("Case #%d: O won\n", tcNo);
                else if (full)
                    printf("Case #%d: Draw\n", tcNo);
                    else
                        printf("Case #%d: Game has not completed\n", tcNo);
    }



    return 0;
}
