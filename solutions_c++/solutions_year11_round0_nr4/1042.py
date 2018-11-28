#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int a[1111],f[1111];
int main()
{
    int t,T,n,i,j;

    freopen("D-large.in","r",stdin);
   freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        double ans=0.0;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            if(a[i]==i) f[i]=0;
            else f[i]=1;
        }
        for(i=1;i<=n;i++)
        {
            if(!f[i]) continue;
            j=a[i];
            f[i]=0;
            int c=1;
            while(j!=i)
            {
                f[j]=0;
                j=a[j];
                c++;
            }
            ans+=c;
        }
        printf("Case #%d: %.6f\n",t,ans);
    }
//system("pause");

    return 0;
}
