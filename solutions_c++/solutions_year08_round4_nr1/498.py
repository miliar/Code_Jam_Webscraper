#include <cstdio>
#include <cstring>
#include <cstdlib>
const int maxn = 10010;
const int oo = 1000000;
int f[maxn][2];
int opt[maxn],value[maxn],change[maxn];
int i,j,k,t,m,n,v;

int work(int root,int v)
{
    if (root > n)
        return oo+1;
    if (f[root][v] != oo)
        return f[root][v];
    int min = oo+1;
    if (v)
    {
        if (opt[root])
        {
            min <?= work(root*2,1) + work(root*2+1,1);
            if (change[root])
            {
                min <?= work(root*2,1) + work(root*2+1,0)+1;
                min <?= work(root*2,0) + work(root*2+1,1)+1;    
            }
        }
        else 
        {
            min <?= work(root*2,1) + work(root*2+1,1);
            min <?= work(root*2,0) + work(root*2+1,1);
            min <?= work(root*2,1) + work(root*2+1,0);
        }
    }
    else 
    {
        if (opt[root])
        {
            min <?= work(root*2,1) + work(root*2+1,0);
            min <?= work(root*2,0) + work(root*2+1,0);
            min <?= work(root*2,0) + work(root*2+1,1);
        }
        else 
        {
            min <?= work(root*2,0) + work(root*2+1,0);
            if (change[root])
            {
                min <?= 1 + work(root*2,1) + work(root*2+1,0);
                min <?= 1 + work(root*2,0) + work(root*2+1,1);
            }
        }
    }            
    f[root][v] = min;
    return min;    
}


int main()
{
    freopen("A-l.in","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        scanf("%d%d",&n,&v);
        for (i = 1; i <= n; ++i)
        {
            f[i][0] = oo;
            f[i][1] = oo;
        }
        for (i = 1;i <= (n-1)/2; ++i)
            scanf("%d%d",opt+i,change+i);
        for (; i <= n; ++i)
        {
            scanf("%d",value + i);
            f[i][value[i]] = 0;
            f[i][1-value[i]] = oo + 1;
        }
        printf("Case #%d: ",T);
        if (work(1,v) < oo)
            printf("%d\n",f[1][v]);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
