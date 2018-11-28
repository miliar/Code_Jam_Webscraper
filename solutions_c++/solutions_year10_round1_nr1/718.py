#include<iostream>
#include<stdio.h>
using namespace std;


char str[55][55];
int n,k;

int shift[][2]={{0,1},{1,0},{1,1},{-1,1}};
bool solve(char tag)
{
    for(int i=0;i<n;i++)
      for(int j=0;j<n;j++)
      {
           if(str[i][j]==tag)
           {
               int x=i,y=j;
               for(int t=0;t<4;t++)
               {
                    int len=0;
                    x=i,y=j;
                    while(x>=0&&x<n&&y>=0&&y<n)
                    {
                         if(str[x][y]==tag)
                            len++;
                         else
                            break;
                         x+=shift[t][0];
                         y+=shift[t][1];
                    }
                    if(len>=k)
                    {
                   //   cout<<i<<","<<j<<endl;
                       return true;
                    }
               }
           }
      }
      return false;
}
int main(void)
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=1;
    while(T--)
    {
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++)
          scanf("%s",str[i]);
        
        for(int i=0;i<n;i++)
          for(int j=n-1;j>=0;j--)
          {
              if(str[i][j]!='.')
              {
                  int tmp=j;
                  while(tmp+1<n&&str[i][tmp+1]=='.')
                  {
                     swap(str[i][tmp],str[i][tmp+1]);
                     tmp++;
                  }
              }
          }
       // for(int i=0;i<n;i++)
      //     printf("%s\n",str[i]);
        bool rf,bf;
        rf=solve('R');
        bf=solve('B');
        printf("Case #%d: ",cas++);
        if(rf&&bf)
            printf("Both\n");
        else if(rf)
            printf("Red\n");
        else if(bf)
            printf("Blue\n");
        else
            printf("Neither\n");
    }
    return 0;
}
