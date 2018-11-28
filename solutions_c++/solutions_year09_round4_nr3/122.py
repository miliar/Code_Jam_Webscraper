#include <cstdio>
#include <vector>
using namespace std;

const int M = 200;

int a[M][M];
int n,k;

vector<int> kraw[M];

bool wieksze(int i,int j) {
  for(int p=1;p<=k;++p)
    if(a[i][p]<=a[j][p]) return false;
  return true;
}

vector<int> graf[M*5];
int n1,n2;

int skoj[M*5];
bool visited[M*5];

bool dfs(int x) {
  visited[x]=true;
  for(int i=0;i<graf[x].size();++i) {
    int y = graf[x][i];
    int z = skoj[y];
    if(!z || (!visited[z] && dfs(z))) {
      skoj[x] = y;
      skoj[y] = x;
      return true;
    }
  }
  return false;
}

int skojarz() {
  int ret = 0;
  bool can = true;
  for(int i=1;i<=n1+n2;++i) skoj[i]=0;
  while(can) { can=false;
    for(int i=1;i<=n1;++i) visited[i]=false;
    for(int i=1;i<=n1;++i) if(!visited[i] && !skoj[i]) {
      bool res=dfs(i);
      ret+=res;
      can|=res;
    }
  }
  return ret;
}


int main() {
  int d;
  scanf("%d\n",&d);
  int tc=0;
  while(d--) {
    ++tc;
    scanf("%d %d",&n,&k);
    for(int i=1;i<=n;++i)
      for(int j=1;j<=k;++j)
        scanf("%d",&a[i][j]);
    for(int i=1;i<=n;++i) kraw[i].clear();
    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n;++j) {
        if(wieksze(i,j)) kraw[i].push_back(j);
      }
    }
/*    printf("graf:\n");
    for(int i=1;i<=n;++i) {
      printf("[%d]: ",i);
      for(int j=0;j<kraw[i].size();++j)
        printf("%d ",kraw[i][j]);
      printf("\n");
    }*/
    n1 = n2 = n;
//    printf("n1=%d n2=%d\n",n1,n2);
    for(int i=1;i<=n1;++i) graf[i].clear();
    for(int i=1;i<=n;++i) {
      for(int j=0;j<kraw[i].size();++j) {
        int y=kraw[i][j];
        graf[i].push_back(n1+y);
      }
    }
/*    printf("graf2:\n");
    for(int i=1;i<=n;++i) {
      printf("[%d]: ",i);
      for(int j=0;j<graf[i].size();++j)
        printf("%d ",graf[i][j]);
      printf("\n");
    }*/
    int sk = skojarz();
//    printf("skojarz=%d\n",sk);
    printf("Case #%d: %d\n",tc,n-sk);
  }
  return 0;
}