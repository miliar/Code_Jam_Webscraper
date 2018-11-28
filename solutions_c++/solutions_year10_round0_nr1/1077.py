#include <stdio.h>
#include <stdlib.h>

int T,N,K,line;
unsigned int res[31];

void init()
{
    res[0]=0;
    for(int i=1;i<31;++i) {
        res[i]=res[i-1]*2+1;
       // printf("%u\n",res[i]);
    }
}

void solve()
{
   int ret=K-res[N];
   if(ret>=0 && ret%(res[N]+1)==0)
        printf("Case #%d: ON\n",line);
   else
        printf("Case #%d: OFF\n",line);;
}
int main()
{
      freopen("C:\\³Ì±ó\\code jam\\Snapper Chain\\A-large.in","r",stdin);
      freopen("C:\\³Ì±ó\\code jam\\Snapper Chain\\A-large.out","w",stdout);
      init();
      scanf("%d",&T);
      for(line=1;line<=T;++line) {
         scanf("%d%d",&N,&K);
         solve();
      }
    //  system("PAUSE");
      return 0;
}
