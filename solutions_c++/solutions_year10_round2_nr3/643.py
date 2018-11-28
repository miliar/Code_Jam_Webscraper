#include <cstdio>
#include <cstring>

int n,m,a[30],ans[30],now,b[30];

void Check() {
     int i,tot = 0;
     for (i = 2; i<=n; i++)
       if (a[i]) b[++tot] = i,a[i] = tot;
//     for (i = 1; i<=tot; i++)
//       printf("%d ",b[i]); printf("\n");   
     i = tot;
     while (i!=1) {
    //   printf("%d ",i);   
       if (!a[i]) break;
       i = a[i];   
     }  
     if (i==1) ans[n]++;
}

void Search(int k){
     if (k==n) {
        a[k] = 1;
        Check();
        return;       
     }
     a[k] = 0;
     Search(k+1);
     a[k] = 1;
     Search(k+1);
}

int main() {
    int i,j,k,test,tt;
    for (n = 2; n<=25; n++) {
      Search(2);
      printf("%d %d\n",n,ans[n]); 
    }
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
        scanf("%d",&n);
        printf("Case #%d: %d\n",tt,ans[n] % 100003);
    }
    return 0;
}
