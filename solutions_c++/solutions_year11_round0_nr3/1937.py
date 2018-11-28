#include<cstdio>
#include<cstring>
#define maxn 1010
#define inf 0x3fffffff
using namespace std;

int n;
int a[maxn];
int main()
{
    freopen("C.out","w",stdout);
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
    {
        scanf("%d",&n);
        int xr=0,mi=inf,sum=0;
        for(int i=0;i<n;i++) {
            scanf("%d",a+i);
            xr^=a[i];
            if(a[i]<mi) mi=a[i];
            sum+=a[i];
        }
        printf("Case #%d: ",t);
        if(xr!=0)      printf("NO\n");
        else printf("%d\n",sum-mi);
    }
    return 0;
}

            /*  int mx=0;
        for(int i=1;i<(1<<n)-1;i++)
        {
            int cnt1=0,cnt2=0,val=0;
            for(int j=0;j<n;j++)
                if(i&(1<<j)) cnt1^=a[j],val+=a[j];
                else cnt2^=a[j];
            if(cnt1==cnt2 && val>mx) mx=val;
        }
        printf("Case #%d: ",t);
        if(mx==0) printf("NO\n");
        else printf("%d\n",mx);*/
