#include<cstdio>
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
              char temp;
              int a[4][4]={0},check=100,flag=0,sum;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              scanf("%c",&temp);
                              if(temp<33){j--;continue;}
                              if(temp=='.'){a[i][j]=0;check=0;}
                              else if(temp=='X')a[i][j]=1;
                              else if(temp=='O')a[i][j]=-1;
                              else if(temp=='T')a[i][j]=10;
                      }
              }
              for(int i=0;i<4;i++)
              {
                      sum=a[i][0]+a[i][1]+a[i][2]+a[i][3];
                      if(sum==4||sum==13){check=1;flag=1;break;}
                      else if(sum==-4||sum==7){check=-1;flag=1;break;}
              }
              if(flag==0)
              {
                      for(int i=0;i<4;i++)
                      {
                              sum=a[0][i]+a[1][i]+a[2][i]+a[3][i];
                              if(sum==4||sum==13){check=1;flag=1;break;}
                              else if(sum==-4||sum==7){check=-1;flag=1;break;}
                      }
              }
              if(flag==0)
              {
                         sum=a[0][0]+a[1][1]+a[2][2]+a[3][3];
                         if(sum==4||sum==13){check=1;flag=1;}
                         else if(sum==-4||sum==7){check=-1;flag=1;}
                         sum=a[3][0]+a[2][1]+a[1][2]+a[0][3];
                         if(sum==4||sum==13){check=1;flag=1;}
                         else if(sum==-4||sum==7){check=-1;flag=1;}
              }
              if(flag==1)
              {
                         if(check==1)
                         {
                                     printf("Case #%d: X won\n",k);
                         }
                         if(check==-1)
                         {
                                     printf("Case #%d: O won\n",k);
                         }
              }
              if(flag==0)
              {
                         if(check==100)
                         {
                                     printf("Case #%d: Draw\n",k);
                         }
                         else if(check==0)
                         {
                                     printf("Case #%d: Game has not completed\n",k);
                         }
              }
    }
}
                         
                              
              
              
                   
