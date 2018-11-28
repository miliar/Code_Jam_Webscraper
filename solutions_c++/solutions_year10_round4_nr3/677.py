#include <stdio.h>
#include <stdlib.h>
int t,r;
int ans;
int remain;
int tab[1001][1001];
int newtab[1001][1001];
int x1,y1,x2,y2;
main()
{
 freopen("C-small-attempt0.in","r",stdin);
 freopen("C-small.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d",&r);
  remain=0;
  ans=0;
  for(int j=0;j<=100;j++)
  {
   for(int k=0;k<=100;k++)
   {
    tab[j][k]=0;
   }
  }
  for(int l=1;l<=r;l++)
  {
  scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
  for(int j=x1;j<=x2;j++)
  {
   for(int k=y1;k<=y2;k++)
   {
    if(tab[k][j]==0){tab[k][j]=1;remain++;}
   }
  }
  }
  while(remain>0)
  {
   remain=0;
   ans++;
   for(int j=1;j<=100;j++)
   {
    for(int k=1;k<=100;k++)
    {
     if(tab[k][j]==1)
     {
      if(tab[k-1][j]==1||tab[k][j-1]==1)
      {
        newtab[k][j]=1;
        remain++;
      }
      else
      {
       newtab[k][j]=0;
      }
     }
     else
     {
       if(tab[k-1][j]==1&&tab[k][j-1]==1)
      {
        newtab[k][j]=1;
        remain++;
      }
      else
      {
       newtab[k][j]=0;
      }
     }
    }
   }
   for(int j=1;j<=100;j++)
   {
    for(int k=1;k<=100;k++)
    {
     tab[k][j]=newtab[k][j];
    // if(j<=10&&k<=10){printf("%d",tab[k][j]);}
    }
  //  if(j<=10){printf("\n");}
   }
 //  printf("------\n");
  }
  printf("Case #%d: %d\n",i,ans);
 }
 return 0;
}
