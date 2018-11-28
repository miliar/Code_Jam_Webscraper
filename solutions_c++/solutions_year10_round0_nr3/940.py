#include <cstdio>
#include <cstring>

int a[3000],get[3000],l[3000],;
int main() {
    int tt,i,j,k,r,n,test,sums;
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&test);
    for (tt = 1; tt<=test; tt++) {
      scanf("%d%d%d",&r,&k,&n);
      sums = 0; 
      for (i = 1; i<=n; i++) {
        scanf("%d",&a[i]);
        sums += a[i];
        a[i+n] = a[i];  
      }
      int ss = 0,t = 0,time = 0;
      for (i = 1; i<=n ; i++) {
        if (a[i]>k) break;
        if (t+a[i]<=k) t += a[i];
           else {
             time ++;
             if (time == r) break;
             t = a[i];   
           }
        ss+=a[i];  
      }
      if (i<=n) { printf("Case #%d: %d\n",tt,ss); continue; }
      for (i = 1; i<=n; i++) {
        int ss = 0;
        for (j = i; (a[j]+ss<=k)&&(j<n+i); j++)  
          ss += a[j];
        get[i] = ss;
        l[i] = j;  
      }
    //  for (i = 1; i<=n; i++)
    //    printf("%d %d %d\n",i,get[i],l[i]);
    //  printf("-------\n");
      long long ans = 0;
      int now = 1;
      time = 1;
      while (time<=r) {
        ans += get[now]; 
        now = l[now];
        if (now>n) now -= n;   
        time++;
      } 
      printf("Case #%d: %I64d\n",tt,ans);
    }
    return 0;
}
