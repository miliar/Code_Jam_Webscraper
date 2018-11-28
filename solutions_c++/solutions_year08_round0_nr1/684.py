#include <cstdio>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
map<string, int> ss;
map<string, bool> app;
int s, q;
char sea[151][151];
char str[151];
int cnt;
int main() {
    int T, cc = 0;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--) {
           scanf("%d", &s);
           getchar();
           ss.clear();
           for (int i = 0; i < s; i++) {
                gets(sea[i]);
                ss[sea[i]] = i;
           }
           cnt = 0;
           int res = 0;
           app.clear();
           scanf("%d", &q);
           getchar();
           while (q--) {
                  gets(str);
                  if (!app[str]) {
                      app[str] = 1;
                      cnt++;
                      if (cnt == s) {
                          cnt = 1;
                          app.clear();
                          app[str] = 1;
                          res++;
                      }
                  }
                  else {
                      continue;
                  }
           }
           printf("Case #%d: %d\n",++cc , res);
    }
}
