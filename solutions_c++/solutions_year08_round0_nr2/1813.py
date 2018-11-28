#include <cstdio>
#include <algorithm>
const int inf = 0x3fffffff;
struct rec {
    int time;
    int sign;
}alist[100], blist[100];
inline bool cmp(rec x, rec y)
{
    if(x.time != y.time)
        return x.time < y.time;
    else
        return x.sign > y.sign;
}
inline int count(rec list[], int n)
{
    int i = 0, now = 0, need = 0;
    for(;i < n;i++)
    {
        if(list[i].sign>0)
            now++;
        else if(now>0) now--;
        else need++;
    }
    return need;
}

int main()
{
    int i, j, na, nb, ta, n;
    int casenum, casei;
    int dh, dm, ah, am;
    scanf("%d", &casenum);
    for(casei=1;casei<=casenum;casei++)
    {
        scanf("%d", &ta);
        scanf("%d%d", &na, &nb);
        n = na+nb;
        for(i = 0;i<na;i++)
        {
            scanf("%d:%d%d:%d", &dh, &dm, &ah, &am);
            alist[i].time = dh*60 + dm;
            alist[i].sign = -1;
            blist[i].time = ah*60 + am + ta;
            blist[i].sign = 1;
        }
        for(;i<nb+na;i++)
        {
            scanf("%d:%d%d:%d", &dh, &dm, &ah, &am);
            blist[i].time = dh*60 + dm;
            blist[i].sign = -1;
            alist[i].time = ah*60 + am + ta;
            alist[i].sign = 1;
        }
        std::sort(alist, alist+n, cmp);
        std::sort(blist, blist+n, cmp);
        printf("Case #%d: %d %d\n", casei, count(alist, n), count(blist, n));
    }
}
