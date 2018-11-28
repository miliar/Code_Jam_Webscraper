#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;
const int  Max=1010;
int c[Max];
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ",cas);
        int n;
        scanf("%d",&n);
        int flag=0;
        int sum=0;
        int min0=0x7fffffff;
        for(int i=0;i<n;++i)
        {
            scanf("%d",&c[i]);
            flag^=c[i];
            sum+=c[i];
            if(min0>c[i])min0=c[i];
        }
        if(flag)printf("NO\n");
        else printf("%d\n",sum-min0);
    }
    return 0;
}
