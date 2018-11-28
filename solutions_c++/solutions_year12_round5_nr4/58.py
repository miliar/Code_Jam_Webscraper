#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int c[10]={'o','i','#','e','a','s','#','t','b','g'};
int t,tt,n,k,i,e,co,cc,tot,a[44],b[44],g[44][44],u[44];
char s[1010];
bool q;
void edge(int i, int j) {
  if (i<0 || j<0) return;
  if (g[i][j]!=t) {
    a[i]++;
    b[j]++;
    e++;
    g[i][j]=t;
  }
}
int another(char cur) {
  for (int k=0; k<10; k++) if (cur==c[k]) return 26+k;
  return -1;
}
void dfs(int i) {
  u[i]=t;
  if (a[i]!=b[i]) {
    q=true;
    tot+=abs(a[i]-b[i]);
  }
  for (int j=0; j<36; j++) if ((g[i][j]==t || g[j][i]==t) && u[j]!=t) dfs(j);
}
int main() {
  freopen("Ds.in","r",stdin);
  freopen("Ds.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&k);
    scanf("%s",s);
    n=strlen(s);
    for (e=i=0; i<36; i++) a[i]=b[i]=0;
    for (i=1; i<n; i++) {
      edge(s[i-1]-'a',s[i]-'a');
      edge(another(s[i-1]),s[i]-'a');
      edge(s[i-1]-'a',another(s[i]));
      edge(another(s[i-1]),another(s[i]));
    }
    for (tot=cc=co=i=0; i<36; i++) if ((a[i]!=0 || b[i]!=0) && u[i]!=t) {
      q=false;
      dfs(i);
      co++;
      if (!q) cc++;
    }
    tot/=2;
    if (cc) {
      if (co>1) {
        if (co>cc) cc++;
        tot+=cc;
      } else tot++;
    }
    printf("Case #%d: %d\n",t,tot+e);
  }
  return 0;
}
