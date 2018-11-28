#include<cstdio>
#include<iostream>
#include <cstring>
using namespace std;
const int Maxn=110;
int source[Maxn];
int n,s,p;
int solve()
{
    int res=0;
    for(int i=0; i<n; ++i)
    {
        scanf("%d",&source[i]);
        int b=source[i]-p;
        if(b<0)continue;
        int c=b/2;
        if(c>=p-1)res++;
        if(c==p-2&&s>0)
        {
            res++;
            s--;
        }
    }
    return res;
}

void Solve()
{
      int t;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas)
    {
        scanf("%d%d%d",&n,&s,&p);
        printf("Case #%d: %d\n",cas,solve());
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    Solve();
    return 0;
}
