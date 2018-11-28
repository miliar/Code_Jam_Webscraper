#include<iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int time[100010];
int len[1000010];
int a[1010];
int cmp(int a, int b)
{
    return a>b;
}
int main()
{
    freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\B-large.in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int pp,test;
    long long sum,ans,tot;
    bool ok;
    int p;
    int i,j;
    scanf("%d",&test);
    for (pp=1; pp<=test; pp++)
    {
        long long L,t,N,C;
        scanf("%lld%lld%lld%lld",&L,&t,&N,&C);
        for(i=0;i<C;i++)
        scanf("%d",&a[i]);
        p=0;
        tot=0;
        ok=false;
        for(i=0;i<N;i++)
        {
            len[i]=a[p];
            p++;
            p%=C;
            tot+=len[i];
        }
        sum=ans=0;
        long long need=t/2;
        p=0;
        for(i=0;i<N;i++)
        {
            sum+=len[i];
            if(sum>=need)
            {
                time[i]=sum-need;
                for(j=i+1;j<N;j++)
                    time[j]=len[j];
                sort(time+i,time+N,cmp);
                if(N-i<=L)
                {
                    long long temp=0;
                    for(j=i;j<N;j++)
                    temp+=time[j];
                    ans=(tot-temp)*2+temp;
                }
                else
                {
                    long long temp;
                    temp=0;
                    for(j=0;j<L;j++)
                    temp+=time[i+j];
                    ans=(tot-temp)*2+temp;
                }
                ok =true;
                break;
            }
        }
        if(!ok)
        ans=tot*2;
        printf("Case #%d: %lld\n",pp,ans);
    }
}

