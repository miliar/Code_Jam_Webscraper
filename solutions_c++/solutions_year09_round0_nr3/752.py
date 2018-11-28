#include <stdio.h>
#include <string.h>
const char T[20]={'#','w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
int t,tt,f[20],i,j,n;
char s[510];
int main() {
   freopen("Cl.in","r",stdin);
   freopen("Cl.out","w",stdout);
   scanf("%d\n",&t);
   for (tt=1; tt<=t; tt++) {
      gets(s); n=strlen(s); f[0]=1;
      for (i=1; i<20; i++) f[i]=0;
      for (i=0; i<n; i++) for (j=1; j<=19; j++) if (s[i]==T[j]) f[j]=(f[j]+f[j-1])%10000;
      printf("Case #%d: ",tt);
      if (f[19]<10) putchar('0');
      if (f[19]<100) putchar('0');
      if (f[19]<1000) putchar('0');
      printf("%d\n",f[19]);
   }
   return 0;
}
