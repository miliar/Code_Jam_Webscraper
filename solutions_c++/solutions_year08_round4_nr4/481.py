#include <cstdio>
#include <cstring>
const int maxn = 1010; 
int p[10];
char s[maxn],tmp[maxn];
bool flag[10];
int n,k,i,j,ans,t,l;

void check()
{
    for (i = 0; i < l; i += k)
        for (j = 1; j <= k; ++j)
            tmp[i+j-1] = s[i+p[j]-1];
    t = 1;
    for (i = 1; i < l; ++i)
        if (tmp[i] != tmp[i-1])
            t++;
    if (ans > t)
        ans = t;
}

void dfs(int dep)
{
    if (dep > k)
    {
        check();
        return;
    }
    for (int r = 1; r <= k; ++r)
    if (!flag[r])
    {
        flag[r] = true;
        p[dep] = r;
        dfs(dep + 1);
        flag[r] = false;
    }
}

int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        ans = 10000;
        scanf("%d",&k);
        scanf("%s",s);
        l = strlen(s);
        memset(flag,0,sizeof(flag));
        dfs(1);
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
