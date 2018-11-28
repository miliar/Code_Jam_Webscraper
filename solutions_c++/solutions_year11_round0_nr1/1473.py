#include<iostream>
#include<algorithm>
using namespace std;
int type[110],pos[110];
int abs(int x)
{
     if(x>0)
     return x;
     return -x;
     }
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);

     char str[10];
     int t,n;
     int i,j;

     scanf("%d",&t);
     for(i=1;i<=t;i++)
     {
          scanf("%d",&n);
          for(j=0;j<n;j++)
          {
               scanf("%s",str);
               if(str[0]=='O')
               type[j]=1;
               else
               type[j]=2;

               scanf("%d",&pos[j]);
               }

          int pos1=1,pos2=1;
          int time1=0,time2=0;
          for(j=0;j<n;j++)
          {
               if(type[j]==1)
               {
                    time1=max(time1+abs(pos1-pos[j]),time2)+1;
                    pos1=pos[j];
                    //printf("%d\n",time1);
                    }
               else
               {
                    time2=max(time2+abs(pos2-pos[j]),time1)+1;
                    pos2=pos[j];
                    //printf("%d\n",time2);
                    }
               }

          printf("Case #%d: %d\n",i,max(time1,time2));
          }
     }
