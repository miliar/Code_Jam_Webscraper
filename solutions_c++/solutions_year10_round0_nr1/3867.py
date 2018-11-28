#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long lld;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    while(EOF!=scanf("%d",&T))
    {
         lld N,K;
         for(int testcase=1;testcase<=T;++testcase)
         {
              scanf("%lld%lld",&N,&K);
              lld m=(1<<N)-1;
              if(m==(K&m))
                printf("Case #%d: ON\n",testcase);
              else
                printf("Case #%d: OFF\n",testcase);
         }
     }
     return 0;
}
