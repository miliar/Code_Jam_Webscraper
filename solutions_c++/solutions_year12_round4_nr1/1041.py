#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
struct aa{
    int d,l;
}a[10010];
int n;
int w,len,m;
int f[10010];
int main(){
    freopen("a.in","r",stdin);        
    freopen("a.out","w",stdout);
    int ca,cc=0;
    int flag,i,j;
    scanf("%d",&ca);
    while (ca--){
        scanf("%d",&n);
        for (i=0;i<n;i++) scanf("%d%d",&a[i].d,&a[i].l);
        scanf("%d",&m);
        memset(f,0,sizeof(f));
        a[n].d=m;a[n].l=1;
        f[0]=min(a[0].d,a[0].l);
        for (i=1;i<=n;i++){
            for (j=0;j<i;j++){
                if (f[j]+a[j].d>=a[i].d) f[i]=max(f[i],min(a[i].l,a[i].d-a[j].d));
            }
        }
        cc++;
        if (f[n]>0) printf("Case #%d: YES\n",cc);
        else printf("Case #%d: NO\n",cc);
    }
    return 0;        
}
            
