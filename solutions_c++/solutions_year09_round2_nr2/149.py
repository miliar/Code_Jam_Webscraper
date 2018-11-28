#include <stdio.h>
#include <string.h>
int t,tt,n,i,j,k,c[100];
char s[25];
int main() {
   freopen("Bl.in","r",stdin);
   freopen("Bl.out","w",stdout);
   scanf("%d\n",&t);
   for (tt=1; tt<=t; tt++) {
      gets(s+1); n=strlen(s+1); s[0]='0';
      for (i=n; i>=1; i--) if (s[i]>s[i-1]) {
         c[s[i]]++; c[s[i-1]]++;
         for (j=s[i-1]+1; ; j++) if (c[j]>0) { s[i-1]=j; c[j]--; break; }
         for (j='0', k=i; j<='9'; j++) while (c[j]>0) { s[k++]=j; c[j]--; }
         if (i==1) k=0; else k=1;
         break;
      } else c[s[i]]++;
      printf("Case #%d: ",tt);
      puts(s+k);
   }
   return 0;
}
