#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int T,n,s,p,C=1;
int v[128];
int res[128];
int ans;

int main(){

  scanf("%d",&T);
  while(T--){
    scanf("%d %d %d",&n,&s,&p);
    for(int i=0;i<n;i++) scanf("%d",v+i);
    printf("Case #%d: ",C++);

    memset(res,0,sizeof(res));
    for(int i=0;i<n;i++)
      res[(int)ceil((double)v[i]/3.0)]++;

    ans=0; for(int i=10;i>=p;i--) ans+=res[i];

    // remove 1,0,0 from res
    for(int i=0;i<=10;i++)
      for(int j=0;j<n;j++)
        if(v[j]==1+(i*3)) res[i+1]--;
    if(p>=2) ans+=min(res[p-1],s);
    printf("%d\n",ans);
  }

  return 0;
}
