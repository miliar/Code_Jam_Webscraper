#include<cstdio>
using namespace std;
int main()
{
  int n,i,j,f,prev_o,prev_b,buf_o,buf_b,temp,t,g[100],diff,pre_b=0,pre_o=0;
  char s[100];
  freopen("A-large.in","r",stdin);
 freopen("AKN_NRN","w",stdout);
  scanf("%d",&n);
  for(i=0;i<n;i++)
  {
                  scanf("%d",&f);
                  for(j=0;j<f;j++)
                  scanf(" %c %d",&s[j],&g[j]);
               /*   for(j=0,temp=0,t=0,prev_b=1,prev_o=1,buf_b=0,buf_o=0;j<f;j++)
                  {                                          
                                  switch(s[j])
                                  {
                                              case 'B':
                                                   
                                                   if(prev_b>g[j])
                                                   diff=prev_b-g[j]+1;
                                                   else
                                                   diff=g[j]-prev_b+1;
                                                   prev_b=g[j];
                                                   if(j-1>=0 && s[j-1]!='B')
                                                   {
                                                             diff-=buf_b;

                                                             if(diff<0)
                                                             diff=0;
                                                             if(temp>=diff)
                                                             {
                                                                           t=t+temp+1;
                                                                           buf_o=1;
                                                                           }
                                                                           else
                                                                           {
                                                                               t+=(diff+buf_b);
                                                                               buf_o=diff;
                                                                               }
                                                                               temp=0;
                                                                               buf_b=0;
                                                                               }
                                                                               else
                                                                               {
                                                                                   temp+=diff;
                                                                                   buf_o+=diff;
                                                                                   
                                                                                   }
                                                                                   break;
                                           case 'O':
                                                        if(prev_o>g[j])
                                                   diff=prev_o-g[j]+1;
                                                   else
                                                   diff=g[j]-prev_o+1;
                                                   prev_o=g[j];
                                                   if(j-1>=0 && s[j-1]!='O')
                                                   {
                                                             diff-=buf_o;
                                                             if(diff<0)
                                                             diff=0;
                                                             if(temp>=diff)
                                                             {
                                                                           t=t+temp+1;
                                                                           buf_b=1;
                                                                           }
                                                                           else
                                                                           {
                                                                               t+=(diff+buf_o);
                                                                               buf_b=diff;
                                                                               }
                                                                               temp=0;
                                                                               buf_o=0;
                                                                               }
                                                                               else
                                                                               {
                                                                                   temp+=diff;
                                                                                   buf_b+=diff;
                                                                                   }
                                                                                   }
                                                                                   }
                                    if(temp>0)
                                    t+=temp;
                                    printf("Case #%d: %d\n",i+1,t);    */          
                                    for(j=0,pre_b=0,pre_o=0,prev_b=1,prev_o=1,diff=0,t=0;j<f;j++)
                                    {
                                                                 while(s[j]=='B' && j<f)
                                                                 {
                                                                                 if(g[j]>prev_b)
                                                                                 diff= g[j]-prev_b+1;
                                                                                 else
                                                                                 diff=prev_b-g[j]+1;
                                                                                 prev_b=g[j];
                                                                                 if(j-1>=0 && s[j-1]!='B')
                                                                                 {
                                                                                           if(diff<=pre_b)
                                                                                           {
                                                                                                        t+=1;
                                                                                                        pre_o=1;
                                                                                                        }
                                                                                          else
                                                                                          {
                                                                                              t+=(diff-pre_b);
                                                                                              pre_o=diff-pre_b;
                                                                                              }
                                                                                              pre_b=0;
                                                                                              }
                                                                                              else
                                                                                              {
                                                                                                  t+=diff;
                                                                                                  pre_o+=diff;
                                                                                                  }
                                                                                                  j++;
                                                                                             }              
                                                                 while(s[j]=='O' && j<f)
                                                                 {
                                                                                 if(g[j]>prev_o)
                                                                                 diff= g[j]-prev_o+1;
                                                                                 else
                                                                                 diff=prev_o-g[j]+1;
                                                                                 prev_o=g[j];
                                                                                 if(j-1>=0 && s[j-1]!='O')
                                                                                 {
                                                                                           if(diff<=pre_o)
                                                                                           {
                                                                                                        t+=1;
                                                                                                        pre_b=1;
                                                                                                        }
                                                                                          else
                                                                                          {
                                                                                              t+=(diff-pre_o);
                                                                                              pre_b=diff-pre_o;
                                                                                              }
                                                                                              pre_o=0;
                                                                                              }
                                                                                              else
                                                                                              {
                                                                                                  t+=diff;
                                                                                                  pre_b+=diff;
                                                                                                  }
                                                                                                  j++;
                                                                                             }
                                                                                             j--;                  
                                    }
                                    printf("Case #%d: %d\n",(i+1),t);
                                    }                                                                         
                                                                                   
}
