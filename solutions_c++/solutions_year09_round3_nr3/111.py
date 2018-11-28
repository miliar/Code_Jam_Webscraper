#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <map>
using namespace std;
const int N = 105;
const int INF = 1e29;
int p,q;
int a[N];
int f[N][N];
typedef pair<int,int> pii;
map<pair<int,int>,int> mp;
#define MP(A,B) make_pair((A),(B))
int dfs(int l,int r)
{
    if(l>r)return 0;
    pii tp;
    tp=MP(l,r);
    if(mp.find(tp)!=mp.end())
    {
        return (mp.find(tp)->second);
    }
    int i;
    int res = INF;
    int tmp;
    bool flag = 0;
    for(i=0;i<q;i++)
    {
        if(a[i]>=l&&a[i]<=r)
        {
            tmp = dfs(l,a[i]-1)+dfs(a[i]+1,r)+r-l;
            if(tmp<res)res = tmp;
            flag=1;
        }
    }
    if(!flag)res = 0;
    mp.insert(MP(tp,res));
   // printf("%d - %d : %d\n",l,r,res);
    return res;
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T,K=1,i,j,k;
    scanf("%d",&T);
    while(T--)
    {
        mp.clear();
        scanf("%d%d",&p,&q);
        for(i = 0;i<q;i++)
        {
            scanf("%d",a+i);
        }
        sort(a,a+q);
        printf("Case #%d: %d\n",K++,dfs(1,p));
    }
    return 0;
}
