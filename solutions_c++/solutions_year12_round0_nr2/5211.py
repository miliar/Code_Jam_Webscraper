#include <algorithm>
#include <cstdio>
using namespace std;

int n, s, p;
int ans = 0;
int scores[10], triplet[4][3];
void dfs(int v) {
     if(v==0) {
              int scnt, pcnt;
              scnt = pcnt = 0;
              
              for(int i = 0; i < n; i++) {
                      int a = triplet[i][0];
                      int b = triplet[i][1];
                      int c = triplet[i][2];
                      if((a+b+c)!=scores[i]) return;
                      int mx = max(a, max(b, c));
                      int mn = min(a, min(b, c));
                      if((mx-mn)>2) return;
                      if((mx-mn)==2) scnt++;
                      if(mx>=p) pcnt++;
              }
              /*printf("Case \n");
              for(int i = 0; i < n; i++) {
                      int a = triplet[i][0];
                      int b = triplet[i][1];
                      int c = triplet[i][2];
                      printf("%d %d %d\n", a, b, c);
              }
              getchar();
              */
              if(scnt==s) {
                          ans = max(ans, pcnt);
              }
              return;
     }
     
     for(int i = 0; i <= 10; i++) {
             for(int j = 0; j <= 10; j++) {
                     if(abs(i-j)>2) continue;
                     for(int k = 0; k <= 10; k++) {
                             if(abs(j-k)>2) continue;
                             if(abs(i-k)>2) continue;
                             triplet[v-1][0] = i;
                             triplet[v-1][1] = j;
                             triplet[v-1][2] = k;
                             dfs(v-1);
                     }
             }
     }
}                        
              
int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    
    for(int test = 1; test <= t; test++) {
            scanf("%d%d%d", &n, &s, &p);
            for(int i = 0; i < n; i++) scanf("%d", &scores[i]);
            ans = 0;
            dfs(n);
            printf("Case #%d: %d\n", test, ans);
    }
}
