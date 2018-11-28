#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;
int srpmax[50],regularmax[50];
int main()
{
    int i,j,k,sum;
    for(i=0;i<=10;i++)
        for(j=i;j<=i+2&&j<=10;j++)
            for(k=j;k<=i+2 && k<=j+2 && k<=10;k++)
            {
                sum=i+j+k;
                if(2 == k-i)
                    srpmax[sum]=k;
                else
                    regularmax[sum]=k;
                //printf("%d + %d + %d = %d\n",i,j,k,sum);
            }
        freopen("B-large.in","r",stdin);
        freopen("B.out","w",stdout);

    int test,kase=0,t,s,p,cnt,total;
    scanf("%d",&test);
    while(test--)
    {
        cnt = 0;
        scanf("%d %d %d",&t,&s,&p);
        for(int i=0;i<t;i++)
        {
            scanf("%d",&total);
            if(regularmax[total]>=p)
                cnt++;
            else if(srpmax[total]>=p && s>0)
            {
                cnt++;
                s--;
            }

        }
        printf("Case #%d: %d\n",++kase,cnt);
    }
    return 0;
}
