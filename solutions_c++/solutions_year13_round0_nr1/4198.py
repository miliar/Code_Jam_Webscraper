#include<stdio.h>
#include<conio.h>
#include<iostream.h>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("outp.in","w",stdout);
    int t,i,j,k,sum=0,flag=0,r=0;
    char z;
    int a[4][4];
    //fflush(stdin);
   scanf("%d",&t);
  // fflush(stdin);
    for(k=1;k<=t;k++)
    {
                     r=0;
                     flag=0;
                     sum=0;
                    for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cin>>z;
//cout<<z;
if(z=='X')
a[i][j]=1;

else if(z=='O')
a[i][j]=100;

else if(z=='T')
a[i][j]=200;

else
a[i][j]=16;
}
                     }
                     
                     for(i=0;i<4;i++)
                     {
                                     for(j=0;j<4;j++)
                                     {
                                                    // printf("%d ",a[i][j]);
                                       if(a[i][j]==16)
                                       flag=1;
                                       sum=sum+a[i][j];            
                                     }
                                    if(sum==4 || sum==203)
                                    {
                                              printf("Case #%d: X won\n",k);
                                              sum=0;
                                              r=1;
                                              break;
                                    }
                                    
                                    else if(sum==400 || sum==500)
                                    {
                                         printf("Case #%d: O won\n",k);
                                         sum=0;
                                         r=1;
                                         flag=0;
                                         break;
                                    }
                     sum=0;
                     }
                     if(r==1)
                     {
                             sum=0;
                             flag=0;
                             r=0;
                             continue;
                     }
                     for(i=0;i<4;i++)
                     {
                                     for(j=0;j<4;j++)
                                     {
                                       if(a[j][i]==16)
                                       flag=1;
                                       sum=sum+a[j][i];            
                                     }
                                    if(sum==4 || sum==203)
                                    {
                                              printf("Case #%d: X won\n",k);
                                              sum=0;
                                              r=1;
                                              break;
                                    }
                                    
                                    else if(sum==400 || sum==500)
                                    {
                                         printf("Case #%d: O won\n",k);
                                         sum=0;
                                         r=1;
                                         break;
                                    }
                     sum=0;
                     }
                     if(r==1)
                     {
                             sum=0;
                             flag=0;
                             r=0;
                             continue;
                     }
                     for(i=0;i<1;i++)
                     {
                                     for(j=0;j<4;j++)
                                     {
                                                     if(a[j][j]==16)
                                                     flag=1;
                                                     sum=sum+a[j][j];
                                     }
                                     if(sum==4 || sum==203)
                                    {
                                              printf("Case #%d: X won\n",k);
                                              sum=0;
                                              r=1;
                                              break;
                                    }
                                    
                                    else if(sum==400 || sum==500)
                                    {
                                         printf("Case #%d: O won\n",k);
                                         sum=0;
                                         r=1;
                                         break;
                                    }
                     sum=0;
                     }
                     if(r==1)
                     {
                             sum=0;
                             flag=0;
                             r=0;
                             continue;
                     }
                     for(i=0;i<1;i++)
                     {
                                     for(j=0;j<4;j++)
                                     {
                                                     if(a[j][3-j]==16)
                                                     flag=1;
                                                     sum=sum+a[j][3-j];
                                     }
                                     if(sum==4 || sum==203)
                                    {
                                              printf("Case #%d: X won\n",k);
                                              sum=0;
                                              r=1;
                                              break;
                                    }
                                    
                                    else if(sum==400 || sum==500)
                                    {
                                         printf("Case #%d: O won\n",k);
                                         sum=0;
                                         r=1;
                                         break;
                                    }
                     sum=0;
                     }
                     if(r==1)
                     {
                             sum=0;
                             flag=0;
                             r=0;
                             continue;
                     }  
                   //  printf("%d",flag);             
                     if(r!=1)
                     {
                             if(flag==1)
                             printf("Case #%d: Game has not completed\n",k);
                             else
                             printf("Case #%d: Draw\n",k);
                     }
                     flag=0;
                     r=0;
                     sum=0;
    }
getch();
return 0;
}
    
