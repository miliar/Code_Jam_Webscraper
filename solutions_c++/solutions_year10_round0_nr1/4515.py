#include <cstdio>
#include <iostream>
using namespace std;

main(){
       freopen("A.in","r",stdin);
       freopen("A.out","w",stdout);
       int t;
       scanf("%d",&t);
       int tt=1;
       do{
          int n;
          long long ret=0LL,k=0LL,cou=0LL;
          scanf("%d %lld",&n,&k);
          for (int i=1;i<=n;++i) cou=(cou*2)+1;
          if (k%(cou+1)==cou) printf("Case #%d: ON\n",tt);
          else printf("Case #%d: OFF\n",tt);
       } while(tt++<t);
}
