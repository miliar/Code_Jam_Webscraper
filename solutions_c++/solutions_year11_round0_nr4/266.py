#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
int n;
int a[1010];
bool flag[1010];
void Init()
{
     scanf("%d",&n);
     for(int i=1;i<=n;++i) scanf("%d",&a[i]);
     memset(flag,true,sizeof(flag));
}
void Work()
{
     int ans=0;
     for(int i=1;i<=n;++i)
        if(flag[i])
        {
           int j=i;
           int temp=0;
           while(flag[j])
           {
              flag[j]=false;
              j=a[j];
              ++temp;
           }
           if(temp!=1) ans+=temp;
        }
     printf("%d.000000\n",ans);
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
}
