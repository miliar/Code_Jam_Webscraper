#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t,j,n,candy,sum,min,ans,i;
    scanf("%d",&t);
    for(j=1;j<=n;j++)
    {

              scanf("%d",&n);
              scanf("%d",&candy);
              min=candy;
              sum=candy;
              ans = candy;
              for(i=1;i<n;i++)
              {
                              scanf("%d",&candy);
                              sum = sum + candy;
                              ans = ans ^ candy;
                              if(candy < min)
                                        min = candy;
              }
              if(ans == 0)
              {
                     printf("Case #%d: %d\n",j,sum-min);
              
              }
              else
              {
                     printf("Case #%d: NO\n",j);
              
              }
    }
    return 0;
}
              
              
                              
    
    
