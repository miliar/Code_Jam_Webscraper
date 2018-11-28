#include<stdio.h>
int Q[2000];

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    int t,r,k,i,j,l,n,sum,count,acount;
    long long front;
    scanf("%d",&t);
    l=0;
    while(t--)
    {
        l++;
        scanf("%d%d%d",&r,&k,&n);
        for(int i=0;i<n;i++)
            scanf("%d",&Q[i]);

        if(n!=1)
        {
            front=-1;
            acount=0;
            while(r--)
            {
                j=0;
                sum=0;
                while(sum<=k&&j<=n)
                {
                    count=sum;
                    sum+=Q[(++front)%n];
                    j++;
                }
                front--;
                acount+=count;
            }
        }
        else
        {
             acount=Q[0]*r;
        }
        printf("Case #%d: %d\n",l,acount);
    }
    return 0;
}
