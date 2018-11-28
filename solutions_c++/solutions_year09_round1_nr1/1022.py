#include <cstdio>
#include <cstring>
#define MAXN 65536
char mark[MAXN][12];

bool check(int num, int base)
{
    if(mark[num][base] == -1)
        return false;
    else if(mark[num][base] == 1)
        return true;

    //TBD
    mark[num][base] = -1;
    int tmp = 0, sum = 0;
    int rest = num, next, div=base;
    while(rest > 0)
    {
        next = rest / div;
        tmp = rest - next*div;
        sum += tmp*tmp;
        rest = next;
    }
    if(check(sum, base))
    {
        mark[num][base] = 1;
        return true;
    }
    else
        return false;
}
int solve()
{
    int nbase, base[10];
    int i, j;
    char buf[32];
tt:
    gets(buf);
    if(buf[0] == 0)
        goto tt;
    nbase = sscanf(buf, "%d%d%d%d%d%d%d%d%d%d",
    base, base+1, base+2, base+3, base+4,
    base+5, base+6, base+7, base+8, base+9);
    for(i=2;i<65536;i++)
    {
        for(j=0;j<nbase;j++)
            if(!check(i, base[j]))
                break;
        if(j>=nbase)
            return i;
    }
    return 10000000;
}
void init()
{
    int i;
    for(i=0;i<12;i++)
        mark[1][i] = 1;
}
int main()
{
    int ncase, icase;
    freopen("test.in", "r+", stdin);
    freopen("test.out", "w+", stdout);
    init();
    scanf("%d", &ncase);
    for(icase = 1;icase <=ncase;icase++)
        printf("Case #%d: %d\n", icase, solve());
    return 0;
}
