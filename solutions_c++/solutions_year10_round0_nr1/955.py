#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int n,k;
int temp;
int main()
{
    int t;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cas=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&k);
        temp=(1<<n);
        temp=k%temp;
        if(temp==((1<<n)-1))
        {
            printf("Case #%d: ON\n",cas++);
        }
        else
        {
            printf("Case #%d: OFF\n",cas++);
        }
    }
    return 0;
}
