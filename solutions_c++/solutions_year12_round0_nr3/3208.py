#include <iostream>
#include <cstdio>
using namespace std;
int main() {
  freopen("3i.txt","r",stdin);
   freopen("o3.txt","w",stdout);
    int t,a,b,i,c=1,ans,j,x1,x2,x3,l1,l2,test;
    scanf("%d",&test);
    while(test--)
    {
        ans=0;
        scanf("%d%d",&a,&b);
        if(b<10){
        printf("Case #%d: %d\n",c++,ans);}
       else if (b<100){
        for(i=a;i<b;++i)
        {
            t=i;
            x1=t%10;
            t/=10;
            x2=t%10;
            l1=x1*10+x2;
            if(l1<=b&&l1>i)
                    ans++;
            }
        printf("Case #%d: %d\n",c++,ans);
        }
        else if(b>=100){
        for(i=a;i<b;++i)
        {
            t=i;
            x1=t%10;
            t/=10;
            x2=t%10;
            t/=10;
            x3=t%10;
            l1=x1*100+x3*10+x2;
            l2=x2*100+x1*10+x3;
            if(l1<=b&&l1>i)
                    ans++;
            if(l2<=b&&l2>i)
                    ans++;
            }
         printf("Case #%d: %d\n",c++,ans);
        }
    }
    return 0;
}
