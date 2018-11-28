#include<ctype.h>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int N[1001];

int main()
{
    freopen("c.in","r",stdin);
    freopen("c1.out","w",stdout);
    int t,i,j,cas=1,n,ans;
    long long sum;
    scanf("%d",&t);
    while(t--)
    {
        sum=0;
        scanf("%d",&n);ans=0;
        for(i=0;i<n;i++) scanf("%d",&N[i]);
        for(i=0;i<n;i++)
         ans^=N[i];
        if(ans) printf("Case #%d: NO\n",cas++);
        else
        {
            sort(&N[0],&N[n]);
            for(i=1;i<n;i++) sum+=N[i];
            printf("Case #%d: ",cas++);cout<<sum<<endl;
        }

    }


    return 0;
}
