#include <stdio.h>
#include <stdlib.h>
#include<utility>
using namespace std;

int T,R,K,N,line,g[1002];
pair<int,int> res[1002];

void init()
{
    int s=0,sum=0,ret=0,end=s;
    for(int s=0;s<N;++s) {
       while(ret<N && (sum+g[end])<=K){
          sum+=g[end];++ret; ++end;
          if(end==N) end=0;
       }
       res[s]=make_pair(end,sum);
       sum-=g[s];--ret;
    }
}

void solve()
{
    init();
    int s=0;  __int64 ret=0;
    for(int i=0;i<R;++i) {
         ret+=res[s].second;
         s=res[s].first;
    }
    printf("Case #%d: %I64d\n",line,ret);
}
int main()
{
      freopen("C:\\³Ì±ó\\code jam\\Theme Park\\C-large.in","r",stdin);
      freopen("C:\\³Ì±ó\\code jam\\Theme Park\\C-large.out","w",stdout);
      scanf("%d",&T);
      for(line=1;line<=T;++line) {
         scanf("%d%d%d",&R,&K,&N);
         for(int i=0;i<N;++i) scanf("%d",&g[i]);
         solve();
      }
      //system("PAUSE");
      return 0;
}

