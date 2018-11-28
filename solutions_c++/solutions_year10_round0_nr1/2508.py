#include <iostream>

using namespace std;
int n,k;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,K=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&k);
        if(k%(1<<n)==(1<<n)-1)printf("Case #%d: ON\n",K++);
        else printf("Case #%d: OFF\n",K++);
    }
    return 0;
}
