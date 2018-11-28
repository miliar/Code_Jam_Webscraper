#include<iostream>
using namespace std;
const int MAXN=2010;
int money[MAXN],next[MAXN],cnt[MAXN],arr[MAXN];
int g_n,g_r,g_k;
long long tot;
void init()
{
    memset(cnt,0,sizeof(cnt));
    for(int s=0;s<g_n;s++)
    {
        int m=0,t=s;
        while(m+arr[t]<=g_k)
        {
            m+=arr[t++];
        }
        next[s]=t%g_n;
        money[s]=m;
    }
}
void reader()
{
    scanf("%d%d%d",&g_r,&g_k,&g_n);
    tot=0;
    for(int i=0;i<g_n;i++)
    {
        scanf("%d",arr+i);
        arr[i+g_n]=arr[i];
        tot+=arr[i];
    }
}
long long work()
{
    if(tot<=g_k) return tot*g_r;
    init();
    long long res=0;
    int i,p;
    for(i=p=0;i<g_r;i++)
    {
        res+=money[p];
        p=next[p];
    }
    return res;
}
int main()
{
    freopen("1.txt","w",stdout);
    int t,cas;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        reader();
        printf("Case #%d: %I64d\n",cas,work());
    }
    return 0;
}
