#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<string>list[300];
char str[1000], s[1000];
string r;

int main () {
    int kase, i, m, n, j, k, h = 1;
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d", &kase); 
    while (kase--) {
          scanf("%d %d", &n, &m);
          for (i = 0; i < n+m; i++) {
              scanf("%s", str);
              if (str[0] == '/') j = 1;
              else j = 0; 
              int ptr = 0;
              for (; str[j] != 0; j++) {
                  if (str[j] == '/') {
                     s[ptr] = 0;
                     r = s;
                     list[i].push_back(r);
                     ptr = 0;
                  }  
                  else s[ptr++] = str[j];  
              }
              if (ptr != 0) {
                 s[ptr] = 0;
                 r = s;
                 list[i].push_back(r);
              }
          }
          int ans = 0;
          for (i = n; i < n+m; i++) {
              int ptr = 0;
              for (j = 0; j < i; j++) {
                  int tmp1 = list[i].size();
                  int tmp2 = list[j].size();
                  for (k = 0; k < tmp1 && k < tmp2; k++) {
                      if (list[i][k] != list[j][k]) break;
                  }
                  if (ptr < k) ptr = k;
              }
              ans += list[i].size() - ptr;
          }
          printf("Case #%d: %d\n",h++,ans);
          for (i = 0; i < n+m; i++)
              list[i].clear();
    }
    return 0;
}
