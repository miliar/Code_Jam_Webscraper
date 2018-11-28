#include <cstdio>
#include <cstring>
using namespace std;

char name[110][110];
bool ap[110];
int n,m;
char s[10000],now[10000];

int main() {
  int cases;
  scanf("%d",&cases);
  gets(s);
  int kase=0;
  for (;cases>0;cases--) {
    scanf("%d",&n);
    gets(s);
    memset(name,0,sizeof(name));
    for (int i=1;i<=n;i++) gets(name[i]);
    scanf("%d",&m);
    gets(s);
    int k=0,ans=0;
    memset(ap,0,sizeof(ap));
    for (int i=1;i<=m;i++) {
      int code=0;
      gets(now);
      for (int j=1;j<=n;j++) {
	if (strcmp(now,name[j])==0) {
	  code=j;
	  break;
	}
      }
      if (code==0) continue;
      if (!ap[code]) {
	ap[code]=true;
	k++;
	if (k==n) {
	  k=1;
	  memset(ap,0,sizeof(ap));
	  ap[code]=true;
	  ans++;
	}
      }
    }
    printf("Case #%d: %d\n",++kase,ans);
  }
}
