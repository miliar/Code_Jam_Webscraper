#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
int main()
{
    long long t,i,num[1000]={},min,n,xr,c=0,sum=0;
    scanf("%lld",&t);
    while(t--)
    {
              sum=0;
              c++;
              xr=0;
              scanf("%lld",&n);
              for(i=0;i<n;i++)
              {
                              scanf("%lld",&num[i]);
                              xr^=num[i];
              }
              if(xr!=0)
              printf("Case #%lld: NO\n",c);
              else
              {
                  min=num[0];
                  for(i=0;i<n;i++)
                  {
                                  if(num[i] < min)
                                  min = num[i];
                                  sum+=num[i];
                  }
                  printf("Case #%lld: %lld\n",c,(sum-min));
              }
    }
    return 0;
} 
