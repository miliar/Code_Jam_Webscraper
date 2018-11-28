#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

#define maxn 107

int c, d, n;
int times;
char a[maxn][3];
char b[maxn][2];
char ch;
int e[26];
char t[maxn];
int m;

int main()
{
    freopen("B1.in","r",stdin);
    freopen("B.out","w",stdout);
    
    scanf("%d",&times);
    for (int k = 1; k <= times; ++k) {
      printf("Case #%d: ", k);
      scanf("%d",&c);
      for (int i = 1; i <= c; ++i) {
        scanf("%c",&ch);
        scanf("%c%c%c",&a[i][0],&a[i][1],&a[i][2]);
      }
      scanf("%d",&d);
      for (int i = 1; i <= d; ++i) {
        scanf("%c",&ch);
        scanf("%c%c",&b[i][0],&b[i][1]);
      }
      memset(e,0,sizeof(e));
      scanf("%d",&n);
      scanf("%c",&ch);
      m = 0;
      for (int i = 1; i <= n; ++i) {
        scanf("%c",&t[++m]);
        ++e[t[m]-'A'];
        if (i == 1) continue;
        for (int j = 1; j <= c; ++j) 
          if ((a[j][0] == t[m] && a[j][1] == t[m-1])||(a[j][0] == t[m-1] && a[j][1] == t[m])) {
            --e[t[m]-'A'];
            --e[t[m-1]-'A'];
            t[--m] = a[j][2];
          }
        for (int j = 1; j <= d; ++j) 
          if (e[b[j][0]-'A'] && e[b[j][1]-'A']) {
            memset(e,0,sizeof(e));
            m = 0;
          } 
      }
      printf("[");
      for (int i = 1; i < m; ++i) 
        printf("%c, ",t[i]);
      if (m) printf("%c",t[m]);
      printf("]");
      printf("\n");
    }
    return 0;
}
