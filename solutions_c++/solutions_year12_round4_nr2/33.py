#include <cstdio>
#include <cmath>
#include <algorithm>
#define MAXN 1050

using namespace std;

typedef pair<int,int> pii;

const int inf=1100000000;

int n,w,h;
pii rad[MAXN];
int ans[MAXN][2];

int z;

void dfs(int x1,int x2,int y1,int y2,int sx1,int sx2,int sy1,int sy2) {
   if(x1>x2||y1>y2) return;
   if(z<0) return;
   int r=rad[z].first;
   int id=rad[z].second;
   int xo=max(x1+r,sx1);
   int yo=max(y1+r,sy1);
   int mx=min(x2-r,sx2);
   int my=min(y2-r,sy2);
   if(xo<=mx&&yo<=my) {
      ans[id][0]=xo;
      ans[id][1]=yo;
      z--;
      dfs(x1,xo+r,yo+r,y2,sx1,sx2,sy1,sy2);
      dfs(xo+r,x2,y1,y2,sx1,sx2,sy1,sy2);
   }
}

inline bool check() {
}

inline void solve() {
   sort(rad,rad+n);
   z=n-1;
   dfs(-inf,inf,-inf,inf,0,w,0,h);
   for(int i=0;i<n;i++)
      printf(" %d %d",ans[i][0],ans[i][1]);
   puts("");
   if(z>=0) fprintf(stderr,"ERROR!!\n");
}

int main(void)
{
   int t,cas=1;
   scanf("%d",&t);
   while(t--) {
      scanf("%d %d %d",&n,&w,&h);
      for(int i=0;i<n;i++) {
         scanf("%d",&(rad[i].first));
         rad[i].second=i;
      }
      printf("Case #%d:",cas++);
      solve();
   }
   return 0;
}
