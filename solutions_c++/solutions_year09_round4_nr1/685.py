#include <stdio.h>
int i,n,t,it,rk,j,kk,i1;
int rd[1000];
char s[1000];
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d\n",&t);
for(it=1;it<=t;it++)
   {
   scanf("%d\n",&n);
   for(i=0;i<n;i++)
      {
      gets(s);
      for(j=n-1;j;j--)
         if(s[j]=='1')
            break;
      rd[i]=j;
      }
   for(rk=i=0;i<n;i++)
      if(rd[i]>i)
         for(j=i+1;j<n;j++)
            if(rd[j]<=i)
               {
               kk=rd[j];
               for(i1=j;i1>i;i1--)
                  rd[i1]=rd[i1-1];
               rk+=j-i;
               rd[i]=kk;
               break;
               }
   printf("Case #%d: %d\n",it,rk);
   }
return 0;
}
