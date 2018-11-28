#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
   freopen("2vl.txt","r",stdin);
    freopen("o2l.txt","w",stdout);
    int t,n,s,p,ans,i,c=1,anycase,min;
    char a[105],x[10];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&s,&p);
        ans=0;
        for(i=0;i<n;++i)
            scanf("%d",&a[i]);
        anycase=3*p-3;
        min=3*p-5;
        if(min<0)
        {
            min=0;
        }
        for(i=0;i<n;++i)
            {
                if(a[i]>anycase)
                    ans++;
                 else  if(a[i]>min&&(s))
                 {
                        ans++;
                        s--;
                 }


                    }
       printf("Case #%d: %d\n",c++,ans);

    }
    return 0;
}
