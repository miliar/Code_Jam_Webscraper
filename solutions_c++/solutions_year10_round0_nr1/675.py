#include<iostream>//4294967296
using namespace std;
int main()
{
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int cas,T,n,k;
    scanf("%d",&T);
    for(cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&k);
        //int temp=((1<<n)-1)&(k+1);
        //printf("%d\n",temp);
        //if(temp == 0)
        if((((1<<n)-1)&(k+1)) == 0)
        {
            printf("Case #%d: ON\n",cas);
        }
        else
        {
            printf("Case #%d: OFF\n",cas);
        }
    }
    return 0;
}
