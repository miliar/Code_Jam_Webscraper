#include <iostream>
#include <cstdlib>
#include <cstdio>
int a[1010];
int n,ans;
void Init()
{
     scanf("%d",&n);
     ans=0;
     for(int i=0;i!=n;++i)
     {
        scanf("%d",&a[i]);
        ans+=a[i];
     }
}
void Work()
{
     int temp=0;
     for(int i=0;i!=n;++i) temp^=a[i];
     if(temp==0)
     {
        temp=0x7fffffff;
        for(int i=0;i!=n;++i)
           if(a[i]<temp) temp=a[i];
        printf("%d\n",ans-temp);
     }
     else printf("NO\n");
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i!=T;++i)
    {
       Init();
       printf("Case #%d: ",i+1);
       Work();
    }
    return 0;
}
