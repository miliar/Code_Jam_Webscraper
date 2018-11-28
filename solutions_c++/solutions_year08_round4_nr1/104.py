#include <stdio.h>
int g[10001], c[10001], v[10001];

int ch[10001];
int list[10001];
int m, d; 
int f(int r, int d)
{
    int i,j;
    if (r*2>m)
    {
        if (d==v[r]) return 0; else return -1;
    }
    int l0=f(r*2, 0);
    int l1=f(r*2, 1);
    int r0=f(r*2+1, 0);
    int r1=f(r*2+1, 1);
    int ret=1000000;
    if (g[r]==0) // or
    {
        if (d==0 && l0!=-1 && r0!=-1) ret<?=l0+r0;  
        if (d==1 && l0!=-1 && r1!=-1) ret<?=l0+r1;
        if (d==1 && l1!=-1 && r0!=-1) ret<?=l1+r0;
        if (d==1 && l1!=-1 && r1!=-1) ret<?=l1+r1;
    } else //and
    {
        if (d==0 && l0!=-1 && r0!=-1) ret<?=l0+r0;  
        if (d==0 && l0!=-1 && r1!=-1) ret<?=l0+r1;
        if (d==0 && l1!=-1 && r0!=-1) ret<?=l1+r0;
        if (d==1 && l1!=-1 && r1!=-1) ret<?=l1+r1;
    }
    //change
    if (c[r]==1)
    {
    if (g[r]==1) // or
    {
        if (d==0 && l0!=-1 && r0!=-1) ret<?=l0+r0+1;  
        if (d==1 && l0!=-1 && r1!=-1) ret<?=l0+r1+1;
        if (d==1 && l1!=-1 && r0!=-1) ret<?=l1+r0+1;
        if (d==1 && l1!=-1 && r1!=-1) ret<?=l1+r1+1;
    } else //and
    {
        if (d==0 && l0!=-1 && r0!=-1) ret<?=l0+r0+1;  
        if (d==0 && l0!=-1 && r1!=-1) ret<?=l0+r1+1;
        if (d==0 && l1!=-1 && r0!=-1) ret<?=l1+r0+1;
        if (d==1 && l1!=-1 && r1!=-1) ret<?=l1+r1+1;
    }
    }
    if (ret==1000000) ret=-1;
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int ca, cases=0, t,i;
    scanf("%d", &ca);
    while (ca--)
    {
        scanf("%d%d", &m, &d);
        for (i=1;i<=(m-1)/2;++i)
            scanf("%d%d", &g[i], &c[i]);
        for (;i<=m;++i)
            scanf("%d", &v[i]);
        
        t=f(1, d);
        printf("Case #%d: ", ++cases);
        if (t==-1) printf("IMPOSSIBLE\n"); else 
        printf("%d\n", t);
        
    }
    return 0;
}
