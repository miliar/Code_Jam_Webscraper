/*
 * Author: ZaviOr
 * Created Time:  2011/5/22 17:17:01
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define FORIT(I,V) for (typeof(V.begin()) I = V.begin(); I != V.end(); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
typedef long long LL;

char b[51][51];
int n, m;

const char c[] = {'\\', '\\', '/'};
const int dx[] = {0, 1, 1};
const int dy[] = {1, 0, 1};

inline bool find(pair<int, int> &p) {
    REP(i, n)
        REP(j, m)
            if (b[i][j] == '#') {
                p = MP(i, j);
                return true;
            }
    return false;
}

inline bool put(const pair<int, int> &p) {
    int x = p.first, y = p.second;
    b[x][y] = '/';
    REP(i, 3) {
        int tx = x + dx[i], ty = y + dy[i];
        if (tx < 0 || tx >= n || ty < 0 || ty >= m)
            return false;
        if (b[tx][ty] != '#') return false;
        b[tx][ty] = c[i];
    }
    return true;
}

int main() {
    freopen("A.out", "w", stdout);
    int T, t = 0;
    scanf("%d", &T);
    while (t++ < T) {
        scanf("%d%d", &n, &m);
        REP(i, n)
            REP(j, m) {
                scanf(" %c", b[i] + j);
            }
        pair<int, int> p;
        bool ans = true;
        printf("Case #%d:\n", t);
        while (find(p)) {
            //cout << p.first << " " << p.second << endl;
            if (!put(p)) {
                puts("Impossible");
                ans = false;
                break;
            }
        }
        if (ans) {
            REP(i, n) {
                REP(j, m)
                    printf("%c", b[i][j]);
                puts("");
            }
        }
    }
    return 0;
}

