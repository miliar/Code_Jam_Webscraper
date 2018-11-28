#include<stdio.h>
#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include<bitset>

using namespace std;



int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int n,i,j,sum1,sum2,esum1,esum2,a[1500],test;
    int ans,k,cas;

    scanf("%d",&k);

    for(cas=1;cas<=k;cas++)
    {
    scanf("%d",&n);

    for(i=0;i<n;i++)
     scanf("%d",&a[i]);

    sort(a,a+n);
    //printf("%d\n",a[0]);
     test=0;
    for(i=0;i<n-1;i++)
    {
        sum1=0;sum2=0;esum1=0;esum2=0;

        for(j=0;j<=i;j++)
         {sum1+=a[j];
         esum1^=a[j];
         }

        for(j=i+1;j<n;j++)
         {sum2+=a[j];
         esum2^=a[j];
         }


        if(esum1==esum2)
        {
            ans=sum2;
            if(sum1>sum2)
            ans=sum1;
            test=1;
            break;
        }

    }

     printf("Case #%d: ",cas);
    if(test)
     printf("%d\n",ans);
    else
     printf("NO\n");
    }
    }
