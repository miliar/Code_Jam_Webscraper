#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int t,s,p,a[100],count=0,b,c,d,z,n,i,m;
    scanf("%d",&t);
    z=t;
    while(t--)
    {
              count=0;
              scanf("%d %d %d",&n,&s,&p);
              for(i=0;i<n;i++)
              scanf("%d",&a[i]);
              
              for(i=0;i<n;i++)
              {
                              if(a[i]>=p)
                              {
                              if(a[i]<=(3*p))
                              {
                                             a[i]=a[i]-p;
                                             b=a[i]/2;
                                             c=a[i]-b;
                                             if(((b-p)>-2&&(b-p)<2)&&((c-p)>-2&&(c-p)<2)&&((b-c)>-2&&(b-c)<2))
                                             {
                                                                                                          count++;
                                             }
                                             else if(((b-p)>=-2&&(b-p)<=2)&&((c-p)>=-2&&(c-p)<=2)&&((b-c)>=-2&&(b-c)<=2)&&s>0)
                                             {
                                                  count++;
                                                  s--;
                                             }
                                             else
                                             ;
                              }
                              else
                              {
                                  d=p;
                                  while(d<=10)
                                  {
                                              if(a[i]<=(3*d))
                                              {
                                             a[i]=a[i]-d;
                                             b=a[i]/2;
                                             c=a[i]-b;
                                             if(((b-d)>-2&&(b-d)<2)&&((c-d)>-2&&(c-d)<2)&&((b-c)>-2&&(b-c)<2))
                                             {
                                                                                                          count++;
                                             }
                                             else if(((b-d)>=-2&&(b-d)<=2)&&((c-d)>=-2&&(c-d)<=2)&&((b-c)>=-2&&(b-c)<=2)&&s>0)
                                             {
                                                  count++;
                                                  s--;
                                             }
                                             else
                                             ;
                                             break;
                                             }
                                             d++;
                                  }   
                              }
                              }
              }
              printf("Case #%d: %d\n",z-t,count);
    }
    return 0;
}
                                             
                                                  
                                             
                              
                              
              
