#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN=1005;
const int inf=0x3f3f3f3f;
int T,n;
int a[MAXN];
int ans;     
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: ",cas);
        int i,j,sum=0,total=0;
        ans=-inf;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            sum=sum^a[i];
            total+=a[i];
        }
        if(sum) {printf("NO\n");continue;}
        sort(a+1,a+1+n);
        printf("%d\n",total-a[1]);
    }
    return 0;
}
