#include <stdio.h>
char s[]="welcome to code jam";
int i,j,i1,n,k;
char st[1000];
int mas[1000][50];
int main()
{
freopen("C-large.in","r",stdin);
freopen("C-large.out","w",stdout);
scanf("%d\n",&n);
for(i=0;i<n;i++)
   {
   gets(st);
   for(j=0;st[j];j++)
      for(i1=0;i1<19;i1++)
         mas[j+1][i1+1]=0;
   for(j=0;st[j];j++)
      mas[j+1][0]=1;
   mas[0][0]=1;
   for(j=0;st[j];j++)
      for(i1=0;i1<19;i1++)
         {
         mas[j+1][i1+1]=mas[j][i1+1];
         if(st[j]==s[i1])
            mas[j+1][i1+1]+=mas[j][i1];
         mas[j+1][i1+1]%=10000;
         }
   k=mas[j][i1];
   printf("Case #%d: %d%d%d%d\n",i+1,k/1000,(k/100)%10,(k/10)%10,k%10);
   }
return 0;
}
