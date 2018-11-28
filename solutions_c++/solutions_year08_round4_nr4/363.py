#include <cstdio>
#include <cstring>
using namespace std;

char s[10000],p[10000];
int f[10];
bool been[10];
int len,ans,k;

void check() {
  int now=0;
  memset(p,0,sizeof(p));
  while (now<len) {
    for (int x=1;x<=k;x++) {
      p[f[x]+now-1]=s[now-1+x];
    }
    now=now+k;
  }
  int sum=1;
  for (int i=0;i<=len-2;i++) {
    if (p[i]!=p[i+1]) sum++;
  }
  if (sum<ans) ans=sum;
}

void search(int dep) {
  if (dep==k+1) {
    check();
    return;
  }
  for (int x=1;x<=k;x++) {
    if (!been[x]) {
      f[dep]=x;
      been[x]=true;
      search(dep+1);
      f[dep]=0;
      been[x]=false;
    }
  }
}

int main() {
  int cases,kase=0;
  for (scanf("%d",&cases);cases>0;cases--) {
    ans=10000;
    scanf("%d",&k);
    gets(s);
    gets(s);
    len=strlen(s);
    memset(been,0,sizeof(been));
    memset(f,0,sizeof(f));
    search(1);
    printf("Case #%d: %d\n",++kase,ans);
  }
}
