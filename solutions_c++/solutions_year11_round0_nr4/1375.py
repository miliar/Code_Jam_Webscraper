#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
using namespace std;
const int Max=1100;
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        printf("Case #%d: ",cas);
        int a[Max],b[Max];
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;++i)
        {
            scanf("%d",&a[i]);
            b[i]=a[i];
        }
        sort(b,b+n);
        int ans=0;
        for(int i=0;i<n;++i)
        {
            if(a[i]!=b[i])ans++;
        }
        printf("%d.000000\n",ans);
    }
    return 0;
}
