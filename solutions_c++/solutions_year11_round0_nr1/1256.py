#include <stdio.h>
char ope[200][10];
long long num[200];
long long time[200];
long long abs(long long x)
{
    return x>=0?x:-x;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%s%I64d",ope[i],&num[i]);
        long long pos0=1;
        long long pos1=1;
        for (int i=0;i<n;i++)
        {
            if (ope[i][0]=='O')
            {
                int ans=-1;
                for (int j=i-1;j>=0;j--)
                    if (ope[j][0]=='O')
                    {
                        ans=j;
                        break;
                    }
                if (ans==-1)
                    time[i]=abs(num[i]-pos0);
                else
                    time[i]=time[ans]+abs(num[i]-pos0);
                if (i!=0&&time[i]<time[i-1]) time[i]=time[i-1];
                time[i]++;
                pos0=num[i];
            }
            else
            {
                int ans=-1;
                for (int j=i-1;j>=0;j--)
                    if (ope[j][0]=='B')
                    {
                        ans=j;
                        break;
                    }
                if (ans==-1)
                    time[i]=abs(num[i]-pos1);
                else
                    time[i]=time[ans]+abs(num[i]-pos1);
                if (i!=0&&time[i]<time[i-1]) time[i]=time[i-1];
                time[i]++;
                pos1=num[i];
            }
        }
        printf("Case #%d: %I64d\n",ii,time[n-1]);
    }
    return 0;
}
