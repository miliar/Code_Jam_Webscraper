#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,s,p;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d%d%d",&n,&s,&p);
        int ans=0,cnt;
        for(int j=0;j<n;j++)
        {
            int x;
            int k1=0,k2=0;
            scanf("%d",&x);
            for(int k=0;k<=x;k++)
                for(int l=0;l<=x-k;l++)
                {
                    int fk=x-l-k;
                    if(abs(fk-k)<=1&&abs(l-k)<=1&&abs(fk-l)<=1)
                    {
                        if(max(fk,max(k,l))>=p)
                            k1=1;

                    }
                    if(abs(fk-k)<=2&&abs(l-k)<=2&&abs(fk-l)<=2)
                    {
                        if(max(fk,max(k,l))>=p)
                            k2=1;
                    }
                }
            if(k1)
            {
                ans++;
                continue;
            }
            if(k2&&s)
            {
                s--;
                ans++;
            }
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
