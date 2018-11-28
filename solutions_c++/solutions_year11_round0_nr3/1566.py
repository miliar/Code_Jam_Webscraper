#include"iostream"
#include<stdio.h>
#include<climits>
using namespace std;
int main()
{
    int T,i,j,k,n,re,a,sum,cas=1;

    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
     scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        a=INT_MAX;
        sum=0;
        re=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&k);
            sum+=k;
            re^=k;
            if(k<a)
                a=k;
        }
        printf("Case #%d: ",cas++);
        if(re!=0)
            puts("NO");
        else
            printf("%d\n",sum-a);

    }
    return 0;
}
