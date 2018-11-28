#include <cstdio>
#include <cstring>

long long fabs(long long a) {
  if (a>=0) return a;
    else return -a;   
}

long long GCD(long long a,long long b) {
   if (b==0) return a;
     else return GCD(b, a % b);  
}

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int test,ttest,n,i;
    scanf("%d",&test);
    long long a[10];
    for (ttest = 1; ttest<=test; ttest++) {
        scanf("%d",&n);
        for (i = 1; i<=n; i++) 
          scanf("%I64d",&a[i]);  
        long long gcd = fabs(a[2]-a[1]);
        for (i = 3; i<=n; i++)
          gcd = GCD(gcd,fabs(a[i]-a[i-1]));
        long long t = 0;
        while (t<a[1]) t+=gcd;
        printf("Case #%d: %I64d\n",ttest,t-a[1]);  
    }
    return 0;
}
