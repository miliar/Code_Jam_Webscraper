#include <stdio.h>
#include <string.h>
char s[1100];
char ts[1100];
int p[20], mrk[20],  ans, n;

int count()
{
    int i,ret=1;
    
    for (i=1;ts[i];++i)
    if (ts[i]!=ts[i-1]) ++ret;
    return ret;
}

void conv()
{
    int i,j;
    for (i=j=0; s[i]; ++i)
    {
        ts[i]=s[j+p[(i%n)]];
        if (i%n==n-1) j+=n;
    }    
}

void search(int w)
{
    if (w>=n)
    {
        conv();
        int t=count();
        if (t<ans) ans=t;
        return ;        
    }
    for (int i=0;i<n;++i)
    if (!mrk[i])
    {
        mrk[i]=true;
        p[w]=i;
        search(w+1);
        mrk[i]=false;
    }
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int ca, cases=0, i, j;
    scanf("%d", &ca);
    while (ca--)
    {
        scanf("%d", &n);
        scanf("%s", s);
        ans=0x3ffffff;
        ts[strlen(s)]=0;
        memset(mrk,0,sizeof(mrk));
        search(0);
        printf("Case #%d: %d\n", ++cases, ans);
        
    }
    return 0;
}
