#include <stdio.h>
int it,t,n,R,i,j,k;
int mas[600][600],C[600][600];
int main()
{
freopen("C-large.in","r",stdin);
freopen("C-large.out","w",stdout);
scanf("%d",&t);
C[0][0]=1;
for(i=1;i<=505;i++)
   for(j=0;j<=i;j++)
      C[i][j] = (C[i-1][j-1]+C[i-1][j])%100003;
for(i=2;i<=505;i++)
   for(mas[i][1]=1,j=2;j<i;j++)
      for(mas[i][j]=0,k=1;k<j;k++)
         mas[i][j]+=((long long)mas[j][k] * (long long)C[i-j-1][j-k-1])%100003,
         mas[i][j]%=100003;
for(it=1;it<=t;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d",&n);
   for(R=0,i=1;i<n;i++)
      R+=mas[n][i],
      R%=100003;
   printf("%d\n",R);
   }
return 0;
}
