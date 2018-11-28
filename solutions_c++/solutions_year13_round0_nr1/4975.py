#include<stdio.h>
#include<string.h>

main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt.out","w",stdout);
  
  char st[10][10];
  int t,T,a[101][101],x,y,X,i,j,s;
  
  scanf("%d",&T);
  for(t=1;t<=T;t++)
  {
    for(i=0;i<4;i++)
      scanf("%s",&st[i]);
    printf("Case #%d: ",t);  
    X=0;
    for(i=0;i<4;i++)
      for(j=0;j<4;j++)
        if(st[i][j]=='O')a[i][j]=1;
          else if(st[i][j]=='T')a[i][j]=100;
            else if(st[i][j]=='X')a[i][j]=0;
              else {a[i][j]=10000;X=1;}
    x=0;y=0;
    for(i=0;i<4;i++)
    {
      s=a[i][0]+a[i][1]+a[i][2]+a[i][3];
      if(s==0 || s==100){x=1;break;}
      if(s==4 || s==103){y=1;break;}
    }
    for(i=0;i<4;i++)
    {
      s=a[0][i]+a[1][i]+a[2][i]+a[3][i];
      if(s==0 || s==100){x=1;break;}
      if(s==4 || s==103){y=1;break;}
    }
    s=a[0][0]+a[1][1]+a[2][2]+a[3][3];
      if(s==0 || s==100)x=1;
      if(s==4 || s==103)y=1;
    s=a[3][0]+a[2][1]+a[1][2]+a[0][3];
      if(s==0 || s==100)x=1;
      if(s==4 || s==103)y=1;
    if(x==1)printf("X won\n");
    else if(y==1)printf("O won\n");
          else if(X==1)printf("Game has not completed\n");
            else printf("Draw\n");
  }
}
