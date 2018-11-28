#include<stdio.h>
#include<fstream.h>
#include <iostream>
using namespace std;
int main()
{
    int t,c,n,button,ol,bl,timer,to,tb,temp;
    char robot;
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    cin>>t;
    c=1;
    while(t--)
    {
              cin>>n;
              to=0;tb=0;timer=0;
              for(int i=0,ol=1,bl=1;i<n;i++)
              {
                      cin>>robot;
                      cin>>button;
                           if(robot=='O')
                           {
                                       if(button>ol)
                                                 temp=button-ol;
                                       else 
                                                 temp=ol-button;
                                       if(to>temp)
                                       {
                                                  timer++;
                                                  tb++;
                                       }
                                       else 
                                       {
                                                 timer=timer+temp-to+1;
                                                 tb=tb+temp-to+1;
                                       }
                                       to=0;
                                       ol=button;
                           }
                           else
                           {
                                       if(button>bl)
                                                 temp=button-bl;
                                       else 
                                                 temp=bl-button;
                                       if(tb>temp)
                                       {
                                                  timer++;
                                                  to++;
                                       }
                                       else 
                                       {
                                                 timer=timer+temp-tb+1;
                                                 to=to+temp-tb+1;
                                       }
                                       tb=0;
                                       bl=button;
                           }
              }
        printf("Case #%d: %d\n",c,timer);
        c++;
        }
        return 0;
}      
