#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <vector>
#include <cmath>
#include <cstring>

#define oo 2000000000
#define mp make_pair
#define S second
#define F first
#define pb push_back
#define debug(x) cout << #x << " " << x << endl;
#define MAXV 

using namespace std;

#define didalam(x, y) x >= 0 && y >= 0 && x < row && y < row

char x[110][110], s[110][110];
int ar[8] = {0,  0, 1,  1, 1, -1, -1, -1};
int ac[8] = {1, -1, 0, -1, 1, -1,  1,  0};
int row, K;
queue<pair<int, pair<int, int> > > Q;

inline bool bfs(int a, int b, int koor) {
     while (!Q.empty()) Q.pop();
     Q.push(mp(a, mp(b, 1)));
     
     while (!Q.empty()) {
           int r = Q.front().F, c = Q.front().S.F, d = Q.front().S.S;
           Q.pop();
           if (d == K)
              return true;
           if (didalam(r + ar[koor], c + ac[koor]) && x[r][c] == x[r + ar[koor]][c + ac[koor]])
              Q.push(mp(r + ar[koor], mp(c + ac[koor], d + 1)));
     }
     return false;
}

int main () {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tcc;
    scanf("%d", &tcc);
    for (int i = 0; i < tcc; ++i) {
        memset(x, 0, sizeof(x));
        scanf("%d%d", &row, &K);
        for (int j = 0; j < row; ++j)
            scanf("%s", s[j]);
            
        for (int j = 0; j < row; ++j) 
            for (int k = 0; k < row; ++k)
                x[j][k] = s[row - k - 1][j];     
        
        for (int j = row - 1; j >= 0; --j)
            for (int k = 0; k < row; ++k) {
                if (x[j][k] != '.' && j + 1 < row) {
                   char z = x[j][k];
                   for (int l = j + 1; l < row; ++l)
                       if (x[l][k] == '.') {
                          x[l][k] = z;
                          x[l - 1][k] = '.';
                          z = x[l][k];
                       }
                       else
                           break;
                }
            }
        
        bool RR = false, BB = false;
        for (int j = 0; j < row; ++j) {
            for (int k = 0; k < row; ++k) {
                if (x[j][k] != '.') {
                   if (x[j][k] == 'B' && BB) continue;
                   if (x[j][k] == 'R' && RR) continue;
                   for (int l = 0; l < 8; ++l) {
                       if (bfs(j, k, l)) {
                          if (x[j][k] == 'B')
                             BB = true;
                          else
                              RR = true;
                       }
                   }
                }
            }
        }
        
        if (BB && RR) printf("Case #%d: Both\n", i + 1);
        else if (!BB && !RR) printf("Case #%d: Neither\n", i + 1);
        else if (BB) printf("Case #%d: Blue\n", i + 1);
        else printf("Case #%d: Red\n", i + 1);
    }
    return 0;
}
