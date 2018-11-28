#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,j,n,arr[1000],sum,min,ans,i;
    scanf("%d",&t);
    j=1;
    while(t--)
    {

              scanf("%d",&n);
              scanf("%d",&arr[0]);
              min=arr[0];
              sum=arr[0];
              ans = arr[0];
              for(i=1;i<n;i++)
              {
                              scanf("%d",&arr[i]);
                              sum = sum + arr[i];
                              ans = ans ^ arr[i];
                              if(arr[i] < min)
                                        min = arr[i];
              }
              if(ans == 0)
              {
                     printf("Case #%d: %d\n",j,sum-min);
                     j++;
              }
              else
              {
                     printf("Case #%d: NO\n",j);
                     j++;
              }
    }
    return 0;
}
              
              
                              
    
    
