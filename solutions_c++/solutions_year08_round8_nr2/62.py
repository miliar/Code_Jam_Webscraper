#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <iostream>

using namespace std;

#define PROBLEM "b"

const int MAX = 310;
const int SIZE = 10100;

int n;
char str[MAX][22];
int ls[MAX], rs[MAX];
char used[SIZE];

int main(){
  freopen(PROBLEM".in", "r", stdin);
  freopen(PROBLEM".out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    int i, j, h;
    scanf("%d\n", &n);
    for (i=0; i<n; i++){
      scanf("%s%d%d", &str[i], &ls[i], &rs[i]);
    }
    int ans = MAX;
    for (i=0; i<(1<<n); i++){
      int cnt = 0;
      set<string> S;
      S.clear();
      memset(used, 0, sizeof(used));
      for (j=0; j<n; j++){
        if (i & (1<<j)){
          cnt++;
          S.insert(string(str[j]));
          for (h=ls[j]; h<=rs[j]; h++){
            used[h] = 1;
          }
        }
      }
      if (S.size() > 3) cnt = MAX;
      for (j=1; j<=10000; j++){
        if (!used[j]) cnt = MAX;
      }
      if (cnt < ans) ans = cnt;
    }
    if (ans == MAX) printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
  }
  return 0;  
}