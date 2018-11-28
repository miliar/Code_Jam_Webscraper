#include<stdio.h>
#include<fstream.h>
#include <iostream>
using namespace std;
int main()
{
    int t,c,n,but,ol,bl,time,to,tb,temp;
    char bot;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    c=1;
    while(t--)
    {
              cin>>n;
              to=0;tb=0;time=0;
              for(int i=0,ol=1,bl=1;i<n;i++)
              {
                      cin>>bot;
                      cin>>but;
                           if(bot=='O')
                           {
                                       if(but>ol)
                                                 temp=but-ol;
                                       else 
                                                 temp=ol-but;
                                       if(to>temp)
                                       {
                                                  time++;
                                                  tb++;
                                       }
                                       else 
                                       {
                                                 time=time+temp-to+1;
                                                 tb=tb+temp-to+1;
                                       }
                                       to=0;
                                       ol=but;
                           }
                           else
                           {
                                       if(but>bl)
                                                 temp=but-bl;
                                       else 
                                                 temp=bl-but;
                                       if(tb>temp)
                                       {
                                                  time++;
                                                  to++;
                                       }
                                       else 
                                       {
                                                 time=time+temp-tb+1;
                                                 to=to+temp-tb+1;
                                       }
                                       tb=0;
                                       bl=but;
                           }
              }
        printf("Case #%d: %d\n",c,time);
        c++;
        }
        return 0;
}      
