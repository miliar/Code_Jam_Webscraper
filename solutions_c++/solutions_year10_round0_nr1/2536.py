#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    int Case=0;
    while(t--)
    {
         int n,k;
         scanf("%d%d",&n,&k);
         bool flag=true;
         for(int i=1;i<=n;++i)
         {
             if(!(k&1))
             {
                 flag=false;
                 break;
             }
             k>>=1;
         }
         if(flag) printf("Case #%d: ON\n",++Case);
         else printf("Case #%d: OFF\n",++Case);
    }
    return 0;
}
