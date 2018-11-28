#include <cstdio>
#include <algorithm>
const int inf = 0x3fffffff;
int list[1024];
int main()
{
    int i, j, tmp;
    long long n;
    int p, k, l;
    int casenum, casei;
    scanf("%d", &casenum);
    for(casei=1;casei<=casenum;casei++)
    {
        scanf("%d%d%d", &p, &k, &l);
        for(i=0;i<l;i++)
            scanf("%d", &list[i]);
        std::sort(list, list+l);

        for(i=l-1, j=1, tmp=n=0;i>=0;i--)
        {
            tmp++;
            n+=j*list[i];
            if(tmp==k)
            {
                tmp=0, j++;
                if(j>p)
                    break;
            }
        }
        if(i>0&&list[i-1]!=0)
            printf("Case #%d: Impossible\n", casei);
        else
            printf("Case #%d: %I64d\n", casei, n);
    }
}
