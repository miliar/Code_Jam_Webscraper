#include <cstdio>
#include <cstring>

struct ttype {
  int x,y;
} a[1100];
int n,m;

int Cross(int i,int j) {
    if (a[i].x<a[j].x && a[i].y>a[j].y) return 1;
    if (a[i].x>a[j].x && a[i].y<a[j].y) return 1;
    return 0;
}
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int tt,test,i,k,j;
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
        scanf("%d",&n);
        for (i = 1; i<=n; i++)
          scanf("%d%d",&a[i].x,&a[i].y);
        int ans = 0;  
        for (i = 1; i<=n; i++)
          for (j =1; j<=n; j++) if (i!=j) {
            if (Cross(i,j)) ans++;  
          }  
        printf("Case #%d: %d\n",tt,ans/2);        
    }
    return 0;
}
