#include<algorithm>
#include<stdio.h>
#include<vector>
#include<stdlib.h>
using namespace std;
int T;
char c[10];
char a[10][10];
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
    int i,j,k;
    int p,q,r;
    int t,tt,ttt;
    int x,o,empty;
scanf("%d",&T);
for(int ii=1;ii<=T;ii++)
{
  empty=0;
  for(i=1;i<=4;i++)
   {
     scanf("%s",c);
     for(j=1;j<=4;j++)
      {
        a[i][j]=c[j-1];
        if(a[i][j]=='.')empty=1;
      }
   }
   /*
  for(i=1;i<=4;i++)
   {
     for(j=1;j<=4;j++)printf("%c",a[i][j]);printf("\n");
   }*/
 // printf("%d %d\n",ii,empty);
  p=0;q=0;
  for(i=1;i<=4;i++)
   {
     x=0;o=0;t=0;
     for(j=1;j<=4;j++)
      {
        if(a[i][j]=='X')x++;
        if(a[i][j]=='O')o++;
        if(a[i][j]=='T')t++;
      }
     if(x==4)p=1;
     if(o==4)q=1;
     if(x==3&&t==1)p=1;
     if(o==3&&t==1)q=1;
   }
  for(i=1;i<=4;i++)
   {
     x=0;o=0;t=0;
     for(j=1;j<=4;j++)
      {
        if(a[j][i]=='X')x++;
        if(a[j][i]=='O')o++;
        if(a[j][i]=='T')t++;
      }
     if(x==4)p=1;
     if(o==4)q=1;
     if(x==3&&t==1)p=1;
     if(o==3&&t==1)q=1;     
   }
       x=0;o=0;t=0;
  for(i=1;i<=4;i++)
   {
     if(a[i][i]=='X')x++;
     if(a[i][i]=='O')o++;
     if(a[i][i]=='T')t++;
   }
       if(x==4)p=1;
     if(o==4)q=1;
     if(x==3&&t==1)p=1;
     if(o==3&&t==1)q=1;  
     
     x=0;o=0;t=0;
  for(i=1;i<=4;i++)
   {
     if(a[i][5-i]=='X')x++;
     if(a[i][5-i]=='O')o++;
     if(a[i][5-i]=='T')t++;
   }
       if(x==4)p=1;
     if(o==4)q=1;
     if(x==3&&t==1)p=1;
     if(o==3&&t==1)q=1;  
  printf("Case #%d: ",ii);
  if(p!=0&&q!=0)printf("Bew");
  else if(p!=0&&q==0)printf("X won");
  else if(p==0&&q!=0)printf("O won");
  else if(p==0&&q==0)
   {
     if(empty==0)printf("Draw");
     else printf("Game has not completed");
   }
  if(ii<=T-1)printf("\n");
}
    
    
    scanf(" ");
    return 0;
}
