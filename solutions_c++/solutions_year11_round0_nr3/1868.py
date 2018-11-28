#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
main()
{
    freopen("xxx.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int t;
    int i,j;
    int sum;
    int n,num[10001];
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        sum=0;
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%d",&num[j]);
            sum^=num[j];
        }
        printf("Case #%d: ",i+1);
        if(sum==0) 
        {
            sort(num,num+n);
            sum=0;
            for(j=n-1;j>=1;j--)
            {
                if(num[j]<0) break;
                sum+=num[j];
            }
            printf("%d\n",sum);
        }
        else printf("NO\n");
    }
    scanf(" ");
}
