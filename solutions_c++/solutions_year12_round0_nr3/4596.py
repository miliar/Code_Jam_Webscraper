#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#define pb(x) push_back(x)
#define rep(i,x,y) for(i=x;i<y;i++)
#define geti(x) scanf("%d",&x)

using namespace std;

int main() {
    int t,i,j,a,b,res,cases=0,l,tmp,n,t1,t2;
    scanf("%d",&t);
    while(t--) {
         cases++;
         scanf("%d %d",&a,&b);
         res=0;
         l=0;
         i = a;
         while(i!=0)
         {
                       i /= 10;
                       l++;
         }
         tmp = 1;
         for(j=0;j<l-1;j++)
         tmp *= 10;
         for(i=a;i<=b;i++)
         {
                  n = i;
                  while(1)
                  {
                           t1 = n%10;
                           t2 = n/10;
                           n = t1*tmp + t2;
                           if(n<=b && n>=a && n>i)
                           res++;
                           if(n==i)
                           break;
                  }
         }
         printf("Case #%d: %d\n",cases,res);
    }
    return 0;
}





