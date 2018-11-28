#include<stdio.h>
#include<algorithm>
using namespace std;
int sit[200],sp[200];
bool can[200];
struct node{
    int x,y;
}a[200];
bool op(node x,node y){return x.x<y.x||x.x==y.x&&x.y<y.y;}
int main()
{
    freopen("c:\\B-large.in","r",stdin);
    freopen("c:\\output.txt","w",stdout);
    int nn;
    scanf("%d",&nn);
    for (int ii=1;ii<=nn;ii++) {
        int n,k,b,t;
        scanf("%d%d%d%d",&n,&k,&b,&t);
        printf("Case #%d: ",ii);
        for (int i=1;i<=n;i++) scanf("%d",&a[i].x);
        for (int i=1;i<=n;i++) scanf("%d",&a[i].y);
        sort(a+1,a+n+1,op);
        for (int i=1;i<=n;i++) {
            sit[i]=a[i].x;
            sp[i]=a[i].y;
        }
        int first=0,cnt=0;
        for (int i=n;i>=1;i--) {
            int tem;
            if ((long long)sit[i]+sp[i]*t>=b) {
                can[i]=1;
                cnt++;
            }
            else {
                can[i]=0;
                if (first==0) first=i;
            }
        }
        if (first==0) {puts("0");continue;}
        if (cnt<k) {puts("IMPOSSIBLE");continue;}
        cnt=0;
        int ans=0;
        for (int i=n;i>=1;i--) {
            if (can[i]) cnt++;
            if (i<first&&can[i]) {
                ans+=first-i;
                first--;
            }
            if (cnt==k) break;
        }
        printf("%d\n",ans);
    }
}