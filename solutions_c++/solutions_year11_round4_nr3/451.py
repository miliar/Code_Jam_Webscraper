#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
int flag[1010],prime[1010],yz[1010][1010],tp[1010];
int use[1010];
int p_cnt;
int cmp1(const void *_a,const void *_b)
{
    int *a=(int*)_a;
    int *b=(int*)_b;
    for (int i=0;i<p_cnt;i++)
    {
        if (a[i]!=b[i]) return a[i]-b[i];
    }
    return 0;
}
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    memset(flag,-1,sizeof(flag));
    p_cnt=0;
    for (int i=2; i<=1000; i++)
    {
        if (flag[i]) prime[p_cnt++]=i;
        for (int j=0; j<p_cnt&&prime[j]<=1000/i; j++)
        {
            flag[prime[j]*i]=0;
            if (i%prime[j]==0) break;
        }
    }
    int t;
    scanf("%d",&t);
    for (int ii=1; ii<=t; ii++)
    {
        int n;
        scanf("%d",&n);
        int total=0;
        long long now=0;
        memset(yz,0,sizeof(yz));
        memset(use,0,sizeof(use));
        for (int i=1;i<=n;i++)
        {
            int num=i;
            for (int j=0;j<p_cnt;j++)
                if (num%prime[j]==0)
                {
                    use[j]=1;
                    while (num%prime[j]==0)
                    {
                        yz[i-1][j]++;
                        num/=prime[j];
                    }
                }
        }
        qsort(yz,n,sizeof(int)*1010,cmp1);
        total=0;
        memset(tp,0,sizeof(tp));
        for (int ii1=0;ii1<n;ii1++)
        {
            if (ii1==0) {total++; continue;}
            bool find=false;
            for (int i=0;i<p_cnt;i++)
            {
                if (tp[i]<yz[ii1][i])
                {
                    tp[i]=yz[ii1][i];
                    find=true;
                }
            }
            if (find) total++;
        }
        int maxx=total;
        total=0;
        for (int i=0;i<p_cnt;i++)
            if (use[i]) total++;
        if (total==0) total++;
        printf("Case #%d: %d\n",ii,maxx-total);
        //qsort(yz,n,sizeof(int)*1000,cmp1);
    }
    return 0;
}

