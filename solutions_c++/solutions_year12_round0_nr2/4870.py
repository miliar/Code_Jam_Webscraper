#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main()
{
    int t,n,i,j,s,a[102],p,ans;

    cin>>t;
    for(j=0;j<t;j++)
    {
    ans=0;
    cin>>n>>s>>p;
    for(i=0;i<n;i++)
     {
         cin>>a[i];
         if(a[i]>=3*p-2)
                ans++;
         else if(s)
        {
            if((a[i]>=(3*p-4))&&(3*p-4)>=0)
            {
                s--;ans++;
            }
        }
     }

    printf("Case #%d: %d\n",j+1,ans);
    }
    return 0;
}
