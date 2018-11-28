#include <cstdio>
#include <cstring>

using namespace std;

int li[256];
bool idx[256];
int g[256][256];
bool op[256][256];
char s[256];

int main() {
  //freopen("B-large.in","r",stdin);
  //freopen("B-large.out","w",stdout);
  memset(idx,0,sizeof(idx));
  idx['Q'] = 1; idx['W'] = 1; idx['E'] = 1; idx['R'] = 1;
  idx['A'] = 1; idx['S'] = 1; idx['D'] = 1; idx['F'] = 1;
  int ntest;
  scanf("%d",&ntest);
  for (int loop = 1; loop<=ntest; loop++) {
    memset(g,-1,sizeof(g));
    int n;
    scanf("%d",&n);
    for (int i = 0; i<n; i++) {
      scanf("%s",s);
      g[s[0]][s[1]] = s[2];
      g[s[1]][s[0]] = s[2];
    }
    memset(op,0,sizeof(op));
    scanf("%d",&n);
    for (int i = 0; i<n; i++) {
      scanf("%s",s);
      op[s[0]][s[1]] = op[s[1]][s[0]] = 1;
    }
    scanf("%d%s",&n,s);
    int ans = 0;
    for (int i = 0; i<n; i++) {
      if (ans==0) {
        li[ans++] = s[i];
        continue;
      }
      int ca = li[ans-1],cb = s[i];
      if (g[ca][cb]>=0) li[ans-1] = g[ca][cb];
      else {
        bool opp = 0;
        for (int j = 0; j<ans; j++)
          if (op[li[j]][cb]) opp = 1;
        if (opp) ans = 0;
        else li[ans++] = cb;
      }
    }
    printf("Case #%d: [",loop);
    for (int i = 0; i<ans; i++)
      if (i<ans-1) printf("%c, ",li[i]);
      else printf("%c",li[i]);
    printf("]\n");
  }
  return 0;
}
