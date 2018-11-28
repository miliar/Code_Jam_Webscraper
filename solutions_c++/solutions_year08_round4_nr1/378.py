#include <cstdio>
#include <cstring>
using namespace std;

int f[20010][2];
int g[2][2];
int n,obj;
int k[20010],c[20010];

void update(int &a,int k) {
  if (a==-1 || k<a) a=k;
}

int main() {
  int cases,kase=0;
  for (scanf("%d",&cases);cases>0;cases--) {
    scanf("%d%d",&n,&obj);
    int nd=(n-1)/2,nl=(n+1)/2;
    for (int i=1;i<=nd;i++) {
      scanf("%d%d",&k[i],&c[i]);
    }
    memset(f,-1,sizeof(f));
    int tmp;
    for (int i=nd+1;i<=nd+nl;i++) {
      scanf("%d",&tmp);
      f[i][tmp]=0;
      f[i][1-tmp]=-1;
    }
    for (int i=nd;i>=1;i--) {
      int lc=i*2,rc=i*2+1;
      memset(g,-1,sizeof(g));

      if (f[lc][1]!=-1 && f[rc][1]!=-1) {
	g[1][1]=f[lc][1]+f[rc][1];
      }
      if (f[lc][1]!=-1 && f[rc][0]!=-1) {
	update(g[1][0],f[lc][1]+f[rc][0]);
      }
      if (f[lc][0]!=-1 && f[rc][1]!=-1) {
	update(g[1][0],f[lc][0]+f[rc][1]);
      }
      if (f[lc][0]!=-1 && f[rc][0]!=-1) {
	update(g[1][0],f[lc][0]+f[rc][0]);
      }
      
      if (f[lc][0]!=-1 && f[rc][0]!=-1) {
	g[0][0]=f[lc][0]+f[rc][0];
      }
      if (f[lc][1]!=-1 && f[rc][1]!=-1) {
	update(g[0][1],f[lc][1]+f[rc][1]);
      }
      if (f[lc][0]!=-1 && f[rc][1]!=-1) {
	update(g[0][1],f[lc][0]+f[rc][1]);
      }
      if (f[lc][1]!=-1 && f[rc][0]!=-1) {
	update(g[0][1],f[lc][1]+f[rc][0]);
      }

      if (c[i]==0) {
	f[i][0]=g[k[i]][0];
	f[i][1]=g[k[i]][1];
      } else {
	f[i][0]=g[k[i]][0];
	f[i][1]=g[k[i]][1];
	if (g[1-k[i]][0]!=-1) update(f[i][0],g[1-k[i]][0]+1);
	if (g[1-k[i]][1]!=-1) update(f[i][1],g[1-k[i]][1]+1);
      }

      //      printf("%d %d %d\n",i,f[i][0],f[i][1]);
      
    }
    if (f[1][obj]==-1) printf("Case #%d: IMPOSSIBLE\n",++kase);
    else printf("Case #%d: %d\n",++kase,f[1][obj]);
  }
}
