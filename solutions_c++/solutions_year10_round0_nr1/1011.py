#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,N,K,cas=0;
    scanf("%d",&T);
    while(T--)
    {
        cas++;
        scanf("%d%d",&N,&K);
        int te=(1<<N)-1;
        if((K&te)==te) printf("Case #%d: ON\n",cas);
        else printf("Case #%d: OFF\n",cas);
    }
    return 0;
}

