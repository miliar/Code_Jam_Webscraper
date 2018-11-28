#include<iostream>
#include<cstdio>
int main()
{
    freopen("A1.in","r",stdin);
	freopen("A1.out","w",stdout);
    char str[4][4],temp;
    int t,i,j,x,s,TT,ii,o,xx,oo,ss;
    scanf("%d",&TT);
    for(ii=0;ii<TT;ii++)
    {
         scanf("%c",&temp);
         s=0;xx=0;oo=0;
         for(i=0;i<4;i++)
         {
              for(j=0;j<4;j++){
                   scanf("%c",&str[i][j]);
                  // printf("%d %d %c",i,j,str[i][j]);
              }scanf("%c",&temp);
         }
        /* for(i=0;i<4;i++)
         {
              for(j=0;j<4;j++)
                   printf("%c",str[i][j]);
              printf("\n");
         }*/
         for(i=0;i<4;i++)
         {
              x=0;t=0;o=0;  
              for(j=0;j<4;j++)
              {
                   if(str[i][j]=='X')
                         x++;
                   else if(str[i][j]=='T')
                         t++;
                   else if(str[i][j]=='O')
                          o++;
                   else
                         s++;
              }
              if(x==4)
                  xx=1;
              if(o==4)
                  oo=1;
              if(t==1)
              {
                   if(x==3)
                       xx=1;
                   if(o==3)
                       oo=1;
              }
         }
         for(i=0;i<4;i++)
         {
              x=0;t=0;o=0;  
              for(j=0;j<4;j++)
              {
                   if(str[j][i]=='X')
                         x++;
                   else if(str[j][i]=='T')
                         t++;
                   else if(str[j][i]=='O')
                          o++;
                   else
                         s++;
              }
              if(x==4)
                  xx=1;
              if(o==4)
                  oo=1;
              if(t==1)
              {
                   if(x==3)
                       xx=1;
                   if(o==3)
                       oo=1;
              }
         }
         x=0;t=0;o=0;
         for(i=0;i<4;i++)
         {
              if(str[i][i]=='X')
                         x++;
              else if(str[i][i]=='T')
                         t++;
              else if(str[i][i]=='O')
                          o++;
              else
                         s++;
         }
         if(x==4)
             xx=1;
         if(o==4)
             oo=1;
         if(t==1)
         {
              if(x==3)
                  xx=1;
              if(o==3)
                  oo=1;
         }
          x=0;t=0;o=0;
          for(i=3;i>=0;i--)
         {
              if(str[3-i][i]=='X')
                         x++;
              else if(str[3-i][i]=='T')
                         t++;
              else if(str[3-i][i]=='O')
                          o++;
              else
                         s++;
         }
         if(x==4)
             xx=1;
         if(o==4)
             oo=1;
         if(t==1)
         {
              if(x==3)
                  xx=1;
              if(o==3)
                  oo=1;
         }
         printf("Case #%d: ",ii+1);
         if(oo==1)
             printf("O won\n");
         else if(xx==1)
             printf("X won\n");
         else if(s==0)
             printf("Draw\n");
         else 
             printf("Game has not completed\n");
    }
}
                    
         
    
