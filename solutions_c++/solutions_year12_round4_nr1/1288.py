#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;

const int maxn=20000;
int a[maxn],b[maxn],c[maxn],n,dd;
int f[maxn];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int times;
    scanf("%d", &times);
    for (int tt=1;tt<=times;tt++)
    {
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%d %d",&a[i],&b[i]);
        memset(f,0,sizeof(f));
        f[0]=a[0];
        scanf("%d",&dd);
        int tmp=0;
        for (int i=0;i<n;i++){
            for (int j=i+1;j<n;j++) {
                if (a[i]+f[i]<a[j]) break;
                f[j]=max(f[j],min(b[j],a[j]-a[i]));
            }
            //printf("%d %f\n",i,f[i]);
            if (f[i]+a[i]>tmp) tmp=a[i]+f[i];
            //printf("!!! %d %d %d\n",i,a[i],f[i]);
        }
        //printf("%f %d\n",tmp,dd);
        printf("Case #%d: ",tt);
        if (tmp>=dd) printf("YES\n");
        else printf("NO\n");
    }
}




