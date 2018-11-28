#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>

using namespace std;

#define rep(i,n) for(int i=0;i<(n);i++)
#define foru(i,a,b) for(int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

const int maxn = 111;
const int maxl = 500;

char chd[maxn][maxl], sa[maxl], sb[maxl];
//vector<int> a[maxn], b[maxn];
int n, m, ok, ok1, x, y,a[maxn][maxn],b[maxn][maxn],opp[maxn],used[maxn];

int cmp(int a, int b) {
    return strcmp(chd[a], chd[b]) < 0;
}
/*
int doa(int pth, int u, char s[maxl]) {
    int nl = 0, q[maxn];   
    int sz = a[u].size();
    rep(i, sz) {
           if (a[u][i] == pth)continue;
           doa(u, a[u][i], chd[u]);           
           q[nl++] = u;           
    }            
//    printf("sz = %d\n", sz);
    sort(q, q + nl, cmp);
    int tl = 0;
    s[tl++] = '(';   s[tl] = 0;
    rep(i, nl) strcat(s, chd[q[i]]);
    tl = strlen(s);
    s[tl++] = ')';
    s[tl++] = 0;    
    strcpy(chd[u], s);
//    printf("%d %s\n", u, chd[u]);
}

int dob(int pth, int u, char s[maxl]) {
    int nl = 0, q[maxn];   
    int sz = b[u].size();
    rep(i, sz) {
           if (b[u][i] == pth)continue;
           dob(u, b[u][i], chd[u]);           
           q[nl++] = u;           
    }            
    sort(q, q + nl, cmp);
    int tl = 0;
    s[tl++] = '(';   s[tl] = 0;
    rep(i, nl) strcat(s, chd[q[i]]);
    tl = strlen(s);
    s[tl++] = ')';
    s[tl++] = 0;        
    strcpy(chd[u], s);
}

*/

void dfs(int dep) {
     if (dep == n) {
//     foru(i, 1, m) printf("%d ", opp[i]);
//     printf("\n");
             foru(i, 1, m) foru(j, 1, m) if (b[i][j]) {
                     if (a[opp[i]][opp[j]] == 0) return;
             }
             ok = 1;
             return;
     }
     
     foru(i, 1, n) if (used[i] == 0) {
        used[i] = 1;
        opp[i] = dep + 1;
        dfs(dep + 1);
        used[i] = 0;
        }
}

int main() {
    int cas;
    scanf("%d", &cas);
    rep(tt, cas) {
            printf("Case #%d: ", tt + 1);
            scanf("%d", &n);
            memset(a,0,sizeof(a));
//            rep(i, n + 1) a[i].clear();
            rep(i, n - 1) {
                   scanf("%d%d", &x, &y);
                   a[x][y] = a[y][x] = 1;
//                   a[x].push_back(y);
//                   a[y].push_back(x);
            }            
            scanf("%d", &m);
            memset(b,0,sizeof(b));
//            rep(i, m + 1) b[i].clear();
            rep(i, m - 1) {
                   scanf("%d%d", &x, &y);
                   b[x][y] = b[y][x] = 1;
//                   b[x].push_back(y);
  //                 b[y].push_back(x);
            }
//            printf("lalala = %d %d\n", a[1].size(), a[2].size());
ok = 0; memset(used, 0, sizeof(used));
              dfs(0);
/*              
            ok = 0;
            foru(ii, 1, n) foru(jj, 1, m) {
                    if (ok) continue;
                    doa(-1, ii, sa);
                    dob(-1, jj, sb);
                    if (check(ii, jj)) 
//                    printf("%s %s\n", sa, sb);
                    int la = strlen(sa), lb = strlen(sb);
                    rep(i, la) {
                           int ok1 = 1;
                           rep(j, lb) 
                           if (sa[i + j] != sb[j]) { ok1 = 0; break;}
                           if (ok1) ok = 1;
                    }
                    
            }
            */
            
            printf("%s\n", ok ? "YES" : "NO");
    }
    return 0;
}
