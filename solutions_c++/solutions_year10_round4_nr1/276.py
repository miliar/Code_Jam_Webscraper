#include<stdio.h>
#include<string.h>
#define abs(x) (x>0?x:-(x))
int a[400][400];
int b[400][400];
int main()
{
    freopen("c:\\A-large.in","r",stdin);
    freopen("c:\\output.txt","w",stdout);
    int nn;
    scanf("%d",&nn);
    for (int ii=1;ii<=nn;ii++) {
        printf("Case #%d: ",ii);
        for (int i=0;i<400;i++) for (int j=0;j<400;j++) a[i][j]=-1;
        int n;
        scanf("%d",&n);
        int beg=n;
        for (int i=1;i<=n;i++) {
            int sit=beg;
            for (int j=1;j<=i;j++) {
                scanf("%d",a[i]+sit);
                sit+=2;
            }
            beg--;
        }
        beg=2;
        for (int i=n+1;i<n+n;i++) {
            int sit=beg;
            for (int j=n+n-i;j>=1;j--) {
                scanf("%d",a[i]+sit);
                sit+=2;
            }
            beg++;
        }
        for (int i=0;i<400;i++) for (int j=0;j<400;j++)
            b[i][j]=a[j][i];
        /*
        puts("");
        for (int i=1;i<n+n;i++) {
            for (int j=1;j<n+n;j++) printf("%d ",a[i][j]);
                    puts("");
        }
        puts("");*/
        int ans1=n;
        for (int k=1;k<n+n;k++) {
            bool can=1;
            for (int i=1;i<n+n;i++) for (int j=1;j<k;j++)
                if (a[i][j]!=-1&&a[i][k+k-j]!=-1&&a[i][j]!=a[i][k+k-j]) {can=0;goto next;}
            next:;
            if (can&&ans1>abs(n-k)) ans1=abs(n-k);
        }
        //printf("%d\n",ans1);

        int ans2=n;
        for (int k=1;k<n+n;k++) {
            bool can=1;
            for (int i=1;i<n+n;i++) for (int j=1;j<k;j++)
                if (b[i][j]!=b[i][k+k-j]&&b[i][j]!=-1&&b[i][k+k-j]!=-1) {can=0;goto next2;}
            next2:;
            if (can&&ans2>abs(n-k)) ans2=abs(n-k);
        }
        //printf("%d\n",ans2);
        int res=(ans1+ans2+n)*(ans1+ans2+n)-n*n;
        printf("%d\n",res);
    }

}