#include<stdio.h>
#include<string.h>
int a[110][110];
int b[110][110];
int main()
{
    int nn,n;
    freopen("c:\\C-small-attempt0.in","r",stdin);
    freopen("c:\\output.txt","w",stdout);
    scanf("%d",&nn);
    for (int ii=1;ii<=nn;ii++) {
        scanf("%d",&n);
        memset(a,0,sizeof(a));
        printf("Case #%d: ",ii);
        for (int i=1;i<=n;i++) {
            int x1,x2,y1,y2;
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            for (int j=x1;j<=x2;j++) for (int k=y1;k<=y2;k++) a[j][k]=1;
        }
        int step=0;
        while (1) {
            bool ok=1;
            for (int i=1;i<=100;i++) for (int j=1;j<=100;j++) if (a[i][j]) {
                ok=0;goto next;
            }
            next:;
            if (ok) break;
            else step++;
            memset(b,0,sizeof(b));
            for (int i=1;i<=100;i++) for (int j=1;j<=100;j++) {
                b[i][j]=a[i][j];
                if (a[i][j]&&a[i-1][j]==0&&a[i][j-1]==0) b[i][j]=0;
                if (a[i-1][j]&&a[i][j-1]) b[i][j]=1;
            }
            memcpy(a,b,sizeof(a));
        }
        printf("%d\n",step);
    }
}