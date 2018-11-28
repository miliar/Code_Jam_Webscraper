#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

char map[105][105];

double win[105],owp[105],oowp[105];
int css[105],gwin[105];

int main()
{
      freopen("1BAl0.in","r",stdin);
      freopen("1BAl0.out","w",stdout);
      int t,cas=1,n,i,j;
      double cs,cw;
      double sowp;
      scanf("%d",&t);
      while(t--)
      {
           printf("Case #%d:\n",cas++);
           scanf("%d",&n);
           for(i=0;i<n;i++)
           scanf("%s",map[i]);
           memset(css,0,sizeof(css));
           memset(gwin,0,sizeof(gwin));
           for(i=0;i<n;i++)
           {
               for(j=0;j<n;j++)
               {
                     if(map[i][j]!='.')
                     {
                         css[i]++;
                         if(map[i][j]=='1')
                         gwin[i]++;
                     }
               }
               win[i]=1.0*gwin[i]/1.0/css[i];
           }
           for(i=0;i<n;i++)
           {
                 sowp=0;
                 cs=0;
                 for(j=0;j<n;j++)
                 {
                       if(map[i][j]!='.')
                       {
                          cs++;
                          if(map[i][j]=='0')
                          {
                                sowp+=((gwin[j]-1)/1.0/(css[j]-1));
                          }
                          else
                          sowp+=(gwin[j]/1.0/(css[j]-1));
                       }
                 }
                 owp[i]=sowp/1.0/cs;
           }
           for(i=0;i<n;i++)
           {
                                    cs=0;
                      sowp=0;
                 for(j=0;j<n;j++)
                 {
                      if(map[i][j]!='.')
                      {
                          cs++;
                          sowp+=owp[j];
                      }
                 }
                 oowp[i]=sowp/1.0/cs;
           }
           for(i=0;i<n;i++)
           {
                printf("%lf\n",0.25*win[i]+0.5*owp[i]+0.25*oowp[i]);
           }
      }
      return 0;
}
