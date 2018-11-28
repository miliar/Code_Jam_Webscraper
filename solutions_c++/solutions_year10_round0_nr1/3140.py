#include<iostream>
using namespace std;
int main()
{
    freopen("jam.in","r",stdin);
    freopen("jam.out","w",stdout);
    int t,n,k;
    scanf("%d",&t);
    for (int i=0;i<t;i++)
    {
        string s;
        scanf("%d %d",&n,&k);
        if ((((1<<n)-1)&k)==((1<<n)-1)) {printf("Case #%d: ON\n",i+1);}
        else {printf("Case #%d: OFF\n",i+1);}
    }
    return 0;
}
