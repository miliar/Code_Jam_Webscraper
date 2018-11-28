#include <stdio.h>

using namespace std;

int main()
{       int a[1002],ans[1002][2],t,R,k,n;

    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
        scanf("%d",&t);
        for (int ca=1; ca<=t; ca++)
        {
                printf("Case #%d: ",ca);


                scanf("%d%d%d",&R,&k,&n);
                for (int i=1; i<=n; i++) scanf("%d",&a[i]);
                __int64 sum=0;
                 for (int i=1; i<=n; i++) sum+=a[i];
                if (sum<=k) { sum=sum*R; printf("%I64d\n",sum);continue; }
                for (int i=1; i<=n; i++)
                {
                        int j=i; sum=a[i];
                        while (sum<=k)
                        {
                                j=j%n+1;
                                if (sum+a[j]>k)
                                {
                                        ans[i][1]=j;
                                        ans[i][2]=sum;
                                        break;
                                } else sum+=a[j];
                        }
                }
                __int64 s=0; int now=1;
                        for (int i=1; i<=R; i++)
                        {
                                s+=ans[now][2];
                                now=ans[now][1];
                        }

                        printf("%I64d\n",s);
        }
}
