#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <math.h>
#include <iostream>
#include <string>
using namespace std;
long long ans;
int a,b;
int an[11000];
long long deal(int k)
{
     int w=0;
     int s=k;
     long long res=0;
     int o=k;
     int sl[30];
     int ns=0;
     while (o!=0)
     {
           o=o/10;
           w++;
     }
     int q=1;
     int i;
     for (i=0;i<w-1;i++)
     q=q*10;
     //printf("%d \n",q);
     //printf("%d ",s);
     for (i=0;i<w-1;i++)
     {
         int c=k%10;
         k=k/10+c*q;
         
         if (c!=0&&a<=k&&k<=b&&k>s)
         {
                                   
                                   int j;
                                   for (j=0;j<ns;j++)
                                   if (sl[j]==k)
                                   break;
                                   if (j<ns)
                                   continue;
                                   sl[ns++]=k;//printf("%d %d\n",s,k);
                                   
         res++;
         }
     }
     //printf("\n");
     //if (s==444)
     //printf("%d %I64d\n",s,res);
     return res;
}
     
int main()
{
    int t;
    freopen("in.in","r",stdin);
    scanf("%d",&t);
    
    freopen("out.out","w",stdout);
    int num=0;
    while (t--)
    {
          int i;
          scanf("%d%d",&a,&b);
          ans=0;
          memset(an,0,sizeof(an));
          for (i=a;i<=b;i++)
          {
              ans+=deal(i);
              //printf("%d %I64d\n",i,ans);
          }
          //for (i=a;i<=b;i++)
          //printf("%d %d\n",i,an[i]);
          printf("Case #%d: ",++num);
          printf("%I64d\n",ans);
    }
}
