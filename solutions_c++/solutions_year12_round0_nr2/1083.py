#include <iostream>
#include <string.h>
#include <cstring>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    freopen("outlarge.txt","w",stdout);
    int T,n,s,p,ans;
    int t[110];
    cin>>T;
    for(int i=1;i<=T;i++)
    {

        ans=0;
        scanf("%d%d%d",&n,&s,&p);
        for(int j=0;j<n;j++)scanf("%d",&t[j]);
//        if(i==62)
//        {
//            printf("%d %d %d ",n,s,p);
//            for(int j=0;j<n;j++)printf("%d ",t[j]);
//        }
        for(int j=0;j<n;j++)
        {
            //if(t[j]==0)continue;
            int k=t[j]/3;
            int mod=t[j]%3;

            if((mod>0?k+1:k)>=p)ans++;
            else if(s>0&&t[j]>0)
            {
                if(mod==0&&k+1>=p)
                {
                    ans++;
                    s--;
                }
                else if(mod==2&&k+2>=p)
                {
                    ans++;
                    s--;
                }
            }
        }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
