#include<iostream>
using namespace std;
const int MAXN=60;
int x[MAXN];
int v[MAXN];
int work(int n,int k,int b,int t)
{
    int sj=0,res=0;
    for(int i=n-1;i>=0;i--)
    {
        if(k==0) break;
        if(t*v[i]>=b-x[i])
        {
            res+=sj;
            k--;
        }
        else
        {
            sj++;
        }
    }
    if(k) return -1;
    else return res;
}
int main()
{
    freopen("sub-6.in","r",stdin);
    freopen("out.txt","w",stdout);
    int c,cas,n,k,b,t,i;
    scanf("%d",&c);
    for(cas=1;cas<=c;cas++)
    {
        scanf("%d%d%d%d",&n,&k,&b,&t);
        for(i=0;i<n;i++) scanf("%d",x+i);
        for(i=0;i<n;i++) scanf("%d",v+i);
        int res=work(n,k,b,t);
        if(res==-1)
            printf("Case #%d: IMPOSSIBLE\n",cas);
        else 
            printf("Case #%d: %d\n",cas,res);
    }
}
