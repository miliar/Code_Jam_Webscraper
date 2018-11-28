#include <cstdio>
int a[100];
char c[100];
int main()
{
    freopen ("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 1;t<=T;t++){
        int s = 0,n;
        scanf("%d",&n);
        for(int i = 1;i<=n;i++){
            a[i] = 0;
            scanf("%s",c);
            for(int j=1;j<=n;j++){
                if(c[j-1] == '1')  a[i] = j;
            }
        }
        for(int i = 1;i<=n;i++){
            int j = 0 ,k = 0;
            while(a[j]>i || a[j] ==-1) { k +=(a[j] >i) ; j++;}
            a[j] = -1; s += k;
        }
        printf("Case #%d: %d\n",t,s);
    }
}
