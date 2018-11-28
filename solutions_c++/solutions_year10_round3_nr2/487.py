#include<iostream>
using namespace std;

int cas,l,p,c;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    for(int cnt=1;cnt<=cas;cnt++)
    {
         printf("Case #%d: ",cnt);
         
         scanf("%d%d%d",&l,&p,&c);
         int ct=0;
         while(l<p) 
         {
             l*=c;
             ct++;
         } 
       //  printf("%d\n",ct);
         
         for(int i=0;;i++) 
             if((1<<i)>=ct)
             {
                  printf("%d\n",i);
                  break;
             }
         
    }
    
    
    return 0;
} 
