#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<stack>
#define SSD(x) (scanf("%d",&x))
#define SSL(x) (scanf("%lld",&x))
#define SSF(x) (scanf("%f",&x))
#define SSS(x) (scanf("%s",x))
#define ABS(x) (x>0?x:-x)
using namespace std;
#define MOD 1000000007
int main()
{
     int t,i,j;
     
     freopen("B-large.in","r",stdin);
     freopen("output.txt","w+",stdout);
     scanf("%d",&t);
     int max,s,p,ans,n,sur;
     for(int t1=1;t1<=t;t1++)
     {
         ans=0;sur=0;
         SSD(s);SSD(p);SSD(max);
         for(i=0;i<s;i++)
         {
             SSD(n);
             if(n>=max)
             {
                     
                 n=(n-max)/2;
                 if(n>=(max-1))
                 {
                     ans++;
                 }
                 else if(n==(max-2))
                 {
                     sur++;
                 }
             }
         }    
         if(sur>p)ans+=p;
         else ans+=sur;
         printf("Case #%d: %d\n",t1,ans);
                   
         

     }
     return 0;
}

