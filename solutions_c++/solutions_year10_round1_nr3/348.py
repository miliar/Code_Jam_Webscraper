#include <stdio.h>
#include <stdlib.h>
int lose[50][50];
int q,r;
int t;
int a1,a2,b1,b2;
int ans;
int find(int a,int b)
{
 if(a<b){return find(b,a);}
 else if(a==b){return 0;}
 else
 {
   q=a/b;
   r=a%b;
   if(q>=2){return 1;}
   else if(find(b,r)==1){return 0;}
   else{return 1;}
 }
}
main()
{
 freopen("C-small-attempt0.in","r",stdin);
 freopen("C-small-attempt0.out","w",stdout);
/* for(int i=1;i<=50;i++)
 {
  lose[i][0]=1;
 }
 for(int i=2;i<=50;i++)
 {
  for(int j=1;j<i;j++)
  {
   q=i/j;
   r=i%j;
   if(q>=2){lose[i][j]=1;}
   else if(lose[j][r]==1)
   {
    lose[i][j]=(-1);
   }
   else
   {
   lose[i][j]=1;
   }
  }
 }
  for(int i=1;i<=40;i++)
  {
   for(int j=0;j<i;j++)
   {
    printf("%d ",lose[i][j]);
   }
   printf("\n");
  }*/
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
  ans=0;
  for(int j=a1;j<=a2;j++)
  {
   for(int k=b1;k<=b2;k++)
   {
    ans+=find(j,k);
   }
  }
  printf("Case #%d: %d\n",i,ans);
 }

 //system("pause");
 return 0;
}
