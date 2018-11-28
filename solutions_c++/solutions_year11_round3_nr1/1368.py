#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

char map[55][55];

int main()
{
       freopen("CC2l.in","r",stdin);
       freopen("CC2l.out","w",stdout);
       int t,cas=1,r,c,i,j;
       bool flag;
       scanf("%d",&t);
       while(t--)
       {
                flag=true;
                printf("Case #%d:\n",cas++);
                scanf("%d%d",&r,&c);
                for(i=0;i<r;i++)
                   scanf("%s",map[i]);
                for(i=0;i<r&&flag;i++)
                {
                     for(j=0;j<c&&flag;j++)
                     {
                          if(map[i][j]=='#')
                          {
                                 map[i][j]='/';
                                 if(i+1>=r)
                                 {
                                      flag=false;
                                      break;
                                 }
                                 else
                                 {
                                     if(map[i+1][j]=='#')
                                     {
                                          map[i+1][j]=(char)(92);
                                     }
                                     else
                                     {
                                         flag=false;
                                         break;
                                     }
                                 }
                                 if(j+1>=c)
                                 {
                                      flag=false;
                                      break;
                                 }
                                 else
                                 {
                                     if(map[i][j+1]=='#')
                                     {
                                          map[i][j+1]=(char)(92);
                                     }
                                     else
                                     {
                                         flag=false;
                                         break;
                                     }
                                 }
                                 if(map[i+1][j+1]=='#')
                                 {
                                     map[i+1][j+1]='/';
                                 }
                                 else
                                 {
                                         flag=false;
                                         break;
                                 }
                          }
                     }
                }
                if(flag==false)
                {
                      printf("Impossible\n");
                }
                else
                {
                     for(i=0;i<r;i++)
                     printf("%s\n",map[i]);
                }
       }
       return 0;
}
