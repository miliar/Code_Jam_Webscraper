#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<string>
#include<algorithm>
#include<stack>
#include<vector>
using namespace std;

int main()
{
    int tc;
    cin>>tc;
    for(int q = 1; q<=tc;q++)
    {
         long long int a,b,cnt  = 0;
         int l=1;
         scanf("%lld %lld",&a,&b);
         while(pow(10.0,l)<=a)
              l++;
         for(long long int i = a;i<=b; i++)
         {
                 long long int x = i,cpy = i;
                 while(1)
                 {
                             int d = x %10;
                             x = d * (int)pow(10.0,l-1) + x/10;
                             if(x == cpy)
                                  break;
                             if(x <= b && x >= a )
                                 cnt++;
                             
                 }
                 
         }
         printf("Case #%d: %lld\n",q,cnt/2);
    }
    return 0;
}
