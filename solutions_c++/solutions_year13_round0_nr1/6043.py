#include<iostream>
using namespace std;
#include<cstdio>
//#include<conio.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,x;
    scanf("%d\n",&t);
    for(x=0;x<t;x++)
    {
                  char arr[4][4],i,j;
                  char c;
                  int sum=0;
                  for(i=0;i<4;i++)
                  {
                        for(j=0;j<4;j++)
                        {
                               scanf("%c",&arr[i][j]);
                               if(arr[i][j]=='X')
                                 arr[i][j]=1;
                               if(arr[i][j]=='O')
                                 arr[i][j]=0;
                               if(arr[i][j]=='T')
                                 arr[i][j]=10;
                               if(arr[i][j]=='.')
                                 arr[i][j]=100;
                               sum+=arr[i][j];  
                        }    
                        scanf("%c",&c);
                  }  
                  /*for(i=0;i<4;i++)
                  {
                        for(j=0;j<4;j++)
                        {
                               printf("%d   ",arr[i][j]);
                        }
                        printf("\n");
                  }       */  
                  scanf("%c",&c);
                  int temp,flag=0;
                  for(i=0;i<4;i++)
                  {
                        temp=arr[i][0]+arr[i][1]+arr[i][2]+arr[i][3];
                        if(temp==4||temp==13)
                        {
                           printf("Case #%d: X won\n",x+1); 
                           flag=1; 
                           break;
                        }                    
                        if(temp==0||temp==10)
                        {
                           printf("Case #%d: O won\n",x+1);  
                           flag=1;
                           break;
                        }
                  }
                  if(flag)
                    continue;
                  for(i=0;i<4;i++)
                  {
                        temp=arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i];
                        if(temp==4||temp==13)
                        {
                           printf("Case #%d: X won\n",x+1); 
                           flag=1; 
                           break;
                        }                    
                        if(temp==0||temp==10)
                        {
                           printf("Case #%d: O won\n",x+1);  
                           flag=1;
                           break;
                        }
                  }
                  if(flag)
                    continue;
                  temp=arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3];
                  if(temp==4||temp==13)
                  {
                           printf("Case #%d: X won\n",x+1); 
                           flag=1; 
                           continue;
                  }                    
                  if(temp==0||temp==10)
                  {
                           printf("Case #%d: O won\n",x+1);  
                           flag=1;
                           continue;
                  }
                  temp=arr[0][3]+arr[1][2]+arr[2][1]+arr[3][0];
                  if(temp==4||temp==13)
                  {
                           printf("Case #%d: X won\n",x+1); 
                           flag=1; 
                           continue;
                  }                    
                  if(temp==0||temp==10)
                  {
                           printf("Case #%d: O won\n",x+1);  
                           flag=1;
                           continue;
                  }
                  if(sum<100)
                  {
                         printf("Case #%d: Draw\n",x+1);  
                  }
                  else
                  {
                        printf("Case #%d: Game has not completed\n",x+1);
                  }
    }
   // getch();
}
