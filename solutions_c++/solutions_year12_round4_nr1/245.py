#include <stdio.h>
#include <string.h>
using namespace std;
#define min(a,b) (a>b?b:a)

int d[11000], l[11000];
int n;
int len[11000];
/*
int dp(int k,int left) {
    if (k == n) {
       return 1;
    }
    if (left <= 0) return false;
    char s[20];
    sprintf(s,"%d+%d",k,left);
    if (mm.count(s)) {
       return mm[s];
    }
    for (int i = n; i > k; --i) {
        if (d[i]-d[k] <= left && dp(i,min(l[i],d[i]-d[k]))) {
           mm[s] = 1;
           return true;
        }
    }
    mm[s] = 0;
    return false;
}
*/
int main () {
    int kase;
    freopen("A-small-attempt0(1).in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    int h = 1;
    while (kase--) {
          scanf("%d", &n);
          for (int i = 0; i < n; ++i) {
              scanf("%d %d", &d[i], &l[i]);
          }
          scanf("%d", &d[n]);
          printf("Case #%d: ",h++);
          memset(len,-1,sizeof(len));
          len[0] = min(l[0],d[0]);
          for (int i = 0; i < n; ++i) {
              if (len[i] == -1) break;
              for (int j = i+1; j <= n; ++j) {
                  if (len[i] >= d[j]-d[i] && len[j] < min(l[j],d[j]-d[i])) {
                     len[j] = min(l[j],d[j]-d[i]);
                  }
              }    
          }
          if (len[n] != -1) {
             printf("YES\n");
          }
          else {
             printf("NO\n");
          }
    }
    return 0;
}
