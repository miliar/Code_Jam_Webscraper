#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int cas,n,s,p,i,t,ans,cnt;
   int scores[105],ready[105];
   scanf("%d",&cas);
   for(t = 1;t <= cas;++t) {
    scanf("%d %d %d",&n,&s,&p);
    ans = cnt = 0;
    for(i = 0;i < n;++i) {
      scanf("%d",&scores[i]);
      if(scores[i] % 3 == 0) {
        if(scores[i] / 3 >= p) ans++;
        else if(scores[i] >= 3)  ready[cnt++] = (scores[i] - 3) / 3;
      }
      else if(scores[i] % 3 == 1) {
        if(scores[i] / 3 + 1 >= p) ans++;
        else if(scores[i] >= 4) ready[cnt++] = (scores[i] - 4) / 3;
      }
      else {
        if(scores[i] / 3 + 1 >= p) ans++;
        else if(scores[i] >= 2) ready[cnt++] = (scores[i] - 2) / 3;
      }
    }
    sort(ready,ready + cnt);
    for(i = cnt - 1;i >= 0 && s > 0;--i,--s) {
      if(ready[i] + 2 >= p) ans++;
    }
    printf("Case #%d: %d\n",t,ans);
   }
}
