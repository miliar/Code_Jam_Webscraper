#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);
    int T,i;
    scanf("%d",&T);
    for(T,i=1;T;T--,i++)
    {
        printf("Case #%d: ",i);
        int N,K;
        cin>>N>>K;
        N = (1<<N)-1;
        K++;
        if((K&N) == 0)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}
