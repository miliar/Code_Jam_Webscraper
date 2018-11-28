#include<iostream>
using namespace std;
int n,k,cases,t;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&cases),t=0;t<cases;t++)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",t+1);
        if (((k+1)%(1<<n))==0) puts("ON");
        else puts("OFF");
    }
    return 0;
}
