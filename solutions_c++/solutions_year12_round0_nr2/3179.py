#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int num[1000];
int n,s,p;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int j=0; j<t; ++j)
    {
        scanf("%d%d%d",&n,&s,&p);
        int a=0,b=0;
        for(int i=0; i<n; ++i)
        {
            scanf("%d",&num[i]);
            if(num[i]>=3*p-2)
                a++;
            else if(num[i]>=3*p-4 && num[i]>=2)
                b++;
        }
        int ans=a+(s>b?b:s);
        printf("Case #%d: %d\n",j+1,ans);
    }
    return 0;
}
