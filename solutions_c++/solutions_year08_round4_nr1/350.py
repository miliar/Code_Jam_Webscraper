#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN=40005;
const int INF=1<<20;

int res[MAXN][2], val[MAXN], gate[MAXN], change[MAXN];
int n, targetVal;

void calcOR(int u, int ch)
{
  res[u][0] = min(res[u][0], res[2*u][0]+res[2*u+1][0]+ch);
  
  res[u][1] = min(res[u][1], res[2*u][1]+ch);
  res[u][1] = min(res[u][1], res[2*u+1][1]+ch);
}

void calcAND(int u, int ch)
{
  res[u][1] = min(res[u][1], res[2*u][1]+res[2*u+1][1]+ch);
  
  res[u][0] = min(res[u][0], res[2*u][0]+ch);
  res[u][0] = min(res[u][0], res[2*u+1][0]+ch);
}

void calc(int u)
{
  if(gate[u]==-1) {//leaf
    res[u][val[u]]=0;
    res[u][!val[u]]=INF;
    return;
  }
  calc(2*u);
  calc(2*u+1);
  
  res[u][0]=res[u][1]=INF;
  if(gate[u]==1) //AND
    calcAND(u, 0);
  else
    calcOR(u, 0);

  if(change[u]) {
    calcAND(u, 1);
    calcOR(u, 1);
  }
}

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    memset(change,0,sizeof(change));
    memset(gate,-1,sizeof(gate));
    scanf("%d%d", &n, &targetVal);
    for(int i=1;i<=n;i++)
      res[i][0]=res[i][1]=INF;
    for(int i=1;i<=n;i++)
      if(i<= n/2) {
	scanf("%d%d", &gate[i], &change[i]);
      } else {
	gate[i]=-1;
	scanf("%d", &val[i]);
      }
    calc(1);
    
    if(res[1][targetVal]>=INF)
      printf("Case #%d: IMPOSSIBLE\n", t);
    else 
      printf("Case #%d: %d\n", t, res[1][targetVal]);
  }

  return 0;
}
